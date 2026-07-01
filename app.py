# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import secrets
import re
from datetime import datetime, timedelta, timezone
from flask import Flask, request, render_template, redirect, url_for, make_response, session, flash, send_from_directory, jsonify
from convex import ConvexClient
import urllib.request
from build_site import load_machines_from_db, load_settings_from_db, page, get_index_body, get_catalog_body, product_page, get_about_body, get_contacts_body

base_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'))
app.secret_key = os.environ.get('FLASK_SECRET_KEY', secrets.token_hex(32))

CONVEX_URL = os.environ.get('CONVEX_URL', 'https://fearless-sparrow-233.eu-west-1.convex.cloud')

def get_convex_client():
    return ConvexClient(CONVEX_URL)

def get_client_ip():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()
    return request.remote_addr

def check_login_lockout(ip):
    client = get_convex_client()
    # Trigger cleanup of very old attempts in background
    try:
        client.mutation("loginAttempts:cleanupOldAttempts")
    except Exception:
        pass

    # Get attempts in the last 1 hour
    attempts = client.query("loginAttempts:getAttempts", {"ipAddress": ip})
    
    if len(attempts) >= 3:
        # The attempts are sorted descending, so the oldest of the last 3 is the last one in the list
        oldest_attempt_time = attempts[-1]["attemptTime"] / 1000.0  # Convert ms to sec
        now = datetime.now(timezone.utc).timestamp()
        elapsed = now - oldest_attempt_time
        remaining = 3600 - elapsed
        if remaining > 0:
            return True, int(remaining)
    return False, 0

def record_failed_attempt(ip):
    client = get_convex_client()
    client.mutation("loginAttempts:recordAttempt", {"ipAddress": ip})

def clear_failed_attempts(ip):
    client = get_convex_client()
    client.mutation("loginAttempts:clearAttempts", {"ipAddress": ip})

def check_auth():
    if 'user_id' in session:
        return True
    
    token = request.cookies.get('remember_token')
    if token:
        client = get_convex_client()
        # Cleanup expired sessions
        try:
            client.mutation("sessions:cleanupExpiredSessions")
        except Exception:
            pass

        session_doc = client.query("sessions:getSession", {"token": token})
        if session_doc:
            session['user_id'] = session_doc['userId']
            
            # Refresh token expiry (14 days)
            new_expiry_ms = int((datetime.now(timezone.utc) + timedelta(days=14)).timestamp() * 1000)
            client.mutation("sessions:updateSessionExpiry", {"token": token, "expiresAt": new_expiry_ms})
            return True
            
    return False

def rebuild_static_site():
    webhook_url = os.environ.get('VERCEL_DEPLOY_WEBHOOK')
    if webhook_url:
        try:
            req = urllib.request.Request(webhook_url, data=b'', method='POST')
            with urllib.request.urlopen(req) as response:
                print("Vercel redeploy triggered successfully:", response.read().decode())
            return True
        except Exception as e:
            print("Error triggering Vercel redeploy webhook:", e)
            return False
    else:
        try:
            result = subprocess.run([sys.executable, 'build_site.py'], capture_output=True, text=True, check=True)
            print("Static site rebuilt successfully:", result.stdout)
            return True
        except Exception as e:
            print("Error rebuilding static site:", e)
            return False

def trigger_rebuild_async():
    pass

from io import BytesIO
import json
from PIL import Image

def upload_image_to_convex(file_obj):
    if not file_obj or file_obj.filename == '':
        return None
    
    try:
        # Open uploaded image with Pillow
        with Image.open(file_obj) as img:
            # Convert RGBA to RGB
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[3])
                img = background
            
            # Save optimized WebP to memory buffer
            buffer = BytesIO()
            img.save(buffer, format='WEBP', quality=80)
            optimized_data = buffer.getvalue()
        
        # Get upload URL from Convex
        client = get_convex_client()
        upload_url = client.mutation("products:generateUploadUrl")
        
        # POST file to Convex storage
        req = urllib.request.Request(
            upload_url,
            data=optimized_data,
            headers={'Content-Type': 'image/webp'},
            method='POST'
        )
        
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            storage_id = result['storageId']
            
        # Return public URL
        return f"{CONVEX_URL}/api/storage/{storage_id}"
    except Exception as e:
        print("Error uploading image to Convex storage:", e)
        return None

def slugify(text):
    translit = {
        'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ж':'zh','з':'z','и':'i','й':'y','к':'k','л':'l','м':'m',
        'н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sht',
        'ъ':'u','ь':'y','ю':'yu','я':'ya',
        'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ж':'Zh','З':'Z','И':'I','Й':'Y','К':'K','Л':'L','М':'M',
        'Н':'N','О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H','Ц':'Ts','Ч':'Ch','Ш':'Sh','Щ':'Sht',
        'Ъ':'U','Ь':'Y','Ю':'Yu','Я':'Ya'
    }
    for k, v in translit.items():
        text = text.replace(k, v)
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text)
    return text.strip('-')

# ----------------- PUBLIC ROUTES -----------------

@app.route('/<path:path>')
def serve_static_pages(path):
    for folder in ['css', 'js', 'img']:
        if path.startswith(folder + '/'):
            return send_from_directory('.', path)
    return make_response("Страницата не е намерена (404)", 404)

# ----------------- ADMIN ROUTES -----------------

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if check_auth():
        return redirect(url_for('admin_dashboard'))
    
    ip = get_client_ip()
    locked, remaining_seconds = check_login_lockout(ip)
    if locked:
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        error_msg = f"Твърде много неуспешни опити. Достъпът е блокиран. Моля, опитайте отново след {minutes} мин. и {seconds} сек."
        return render_template('login.html', error=error_msg)

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = 'remember' in request.form

        client = get_convex_client()
        user = client.query("users:getByUsername", {"username": username})

        login_success = False
        if user:
            pw_hash = user['passwordHash']
            # Support PBKDF2 from generate_password_hash
            from werkzeug.security import check_password_hash
            login_success = check_password_hash(pw_hash, password)
        
        if login_success:
            clear_failed_attempts(ip)
            session['user_id'] = user['_id']
            
            response = make_response(redirect(url_for('admin_dashboard')))
            
            if remember:
                token = secrets.token_hex(32)
                expiry_ms = int((datetime.now(timezone.utc) + timedelta(days=14)).timestamp() * 1000)
                
                client.mutation("sessions:createSession", {
                    "token": token,
                    "userId": user['_id'],
                    "expiresAt": expiry_ms
                })
                
                response.set_cookie('remember_token', token, max_age=14*24*3600, httponly=True, samesite='Lax')
            
            return response
        else:
            record_failed_attempt(ip)
            locked, remaining_seconds = check_login_lockout(ip)
            if locked:
                minutes = remaining_seconds // 60
                seconds = remaining_seconds % 60
                error_msg = f"Твърде много неуспешни опити. Достъпът е блокиран. Моля, опитайте отново след {minutes} мин. и {seconds} сек."
            else:
                error_msg = "Грешно потребителско име или парола."
            return render_template('login.html', error=error_msg)

    return render_template('login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('user_id', None)
    
    token = request.cookies.get('remember_token')
    response = make_response(redirect(url_for('admin_login')))
    if token:
        try:
            client = get_convex_client()
            client.mutation("sessions:deleteSession", {"token": token})
        except Exception:
            pass
        response.delete_cookie('remember_token')
        
    flash("Успешно излязохте от профила.", "info")
    return response

@app.route('/admin/dashboard')
def admin_dashboard():
    if not check_auth():
        return redirect(url_for('admin_login'))
    
    client = get_convex_client()
    raw_products = client.query("products:list")
    
    products = []
    for p in raw_products:
        m = dict(p)
        m['id'] = m['_id']
        products.append(m)
        
    stats = {
        'total': len(products),
        'new': sum(1 for p in products if p['state'] == 'new'),
        'used': sum(1 for p in products if p['state'] == 'used'),
        'total_views': sum(p.get('views', 0) for p in products)
    }
    
    return render_template('dashboard.html', products=products, stats=stats)

@app.route('/admin/add-product', methods=['GET', 'POST'])
def add_product():
    if not check_auth():
        return redirect(url_for('admin_login'))
        
    if request.method == 'POST':
        brand = request.form.get('brand', '').strip()
        model = request.form.get('model', '').strip()
        title = f"{brand} {model}"
        cat = request.form.get('cat', '').strip()
        state = request.form.get('state', '').strip()
        
        try:
            imgs = json.loads(request.form.get('sorted_imgs', '[]'))
        except Exception:
            imgs = []
        img = imgs[0] if imgs else 'tractor-green.webp'
        
        price = int(float(request.form.get('price', 0)))
        fuel = request.form.get('fuel', '').strip()
        hp = request.form.get('hp', '').strip()
        trans = request.form.get('trans', '').strip()
        loc = request.form.get('loc', '').strip()
        year = request.form.get('year', '').strip()
        hours = request.form.get('hours', '').strip() or None
        engine = request.form.get('engine', '').strip()
        offer = request.form.get('offer', '').strip()
        dealer = request.form.get('dealer', '').strip()
        tank = request.form.get('tank', '').strip() or 'ДДС вкл.'
        desc = request.form.get('desc', '').strip()
        lease_ret = 'lease_ret' in request.form
        
        slug = slugify(title)
        
        # Calculate monthly rate
        pv = price * 0.20
        os_val = price * 0.10
        financed = price - pv
        interest_rate = 0.035 if state == 'new' else 0.045
        r = interest_rate / 12
        n = 60
        if r > 0:
            pv_factor = sum(1.0 / ((1.0 + r) ** t) for t in range(1, n + 1))
            monthly = int(round((financed - os_val / ((1.0 + r) ** n)) / pv_factor))
        else:
            monthly = int(round((financed - os_val) / n))
            
        client = get_convex_client()
        client.mutation("products:add", {
            "slug": slug, "brand": brand, "model": model, "title": title, "cat": cat, 
            "state": state, "img": img, "price": price, "monthly": monthly, "fuel": fuel, 
            "hp": hp, "trans": trans, "loc": loc, "year": year, "hours": hours, 
            "engine": engine, "offer": offer, "dealer": dealer, "tank": tank, 
            "desc": desc, "lease_ret": lease_ret, "imgs": imgs
        })
        
        trigger_rebuild_async()
        flash(f"Продуктът '{title}' беше добавен успешно!", "success")
        return redirect(url_for('admin_dashboard'))
        
    return render_template('product_form.html', action="Добавяне", product=None)

@app.route('/admin/edit-product/<string:id>', methods=['GET', 'POST'])
def edit_product(id):
    if not check_auth():
        return redirect(url_for('admin_login'))
        
    client = get_convex_client()
    product = client.query("products:get", {"id": id})
    
    if not product:
        flash("Продуктът не беше намерен.", "danger")
        return redirect(url_for('admin_dashboard'))
        
    if request.method == 'POST':
        brand = request.form.get('brand', '').strip()
        model = request.form.get('model', '').strip()
        title = f"{brand} {model}"
        cat = request.form.get('cat', '').strip()
        state = request.form.get('state', '').strip()
        try:
            imgs = json.loads(request.form.get('sorted_imgs', '[]'))
        except Exception:
            imgs = []
        img = imgs[0] if imgs else (product.get('img') or 'tractor-green.webp')
        
        price = int(float(request.form.get('price', 0)))
        fuel = request.form.get('fuel', '').strip()
        hp = request.form.get('hp', '').strip()
        trans = request.form.get('trans', '').strip()
        loc = request.form.get('loc', '').strip()
        year = request.form.get('year', '').strip()
        hours = request.form.get('hours', '').strip() or None
        engine = request.form.get('engine', '').strip()
        offer = request.form.get('offer', '').strip()
        dealer = request.form.get('dealer', '').strip()
        tank = request.form.get('tank', '').strip() or 'ДДС вкл.'
        desc = request.form.get('desc', '').strip()
        lease_ret = 'lease_ret' in request.form
        
        slug = slugify(title)
        
        # Recalculate monthly
        pv = price * 0.20
        os_val = price * 0.10
        financed = price - pv
        interest_rate = 0.035 if state == 'new' else 0.045
        r = interest_rate / 12
        n = 60
        if r > 0:
            pv_factor = sum(1.0 / ((1.0 + r) ** t) for t in range(1, n + 1))
            monthly = int(round((financed - os_val / ((1.0 + r) ** n)) / pv_factor))
        else:
            monthly = int(round((financed - os_val) / n))
            
        client.mutation("products:update", {
            "id": id, "slug": slug, "brand": brand, "model": model, "title": title, "cat": cat, 
            "state": state, "img": img, "price": price, "monthly": monthly, "fuel": fuel, 
            "hp": hp, "trans": trans, "loc": loc, "year": year, "hours": hours, 
            "engine": engine, "offer": offer, "dealer": dealer, "tank": tank, 
            "desc": desc, "lease_ret": lease_ret, "views": int(product.get('views')) if product.get('views') is not None else 0,
            "imgs": imgs
        })
        
        trigger_rebuild_async()
        flash(f"Продуктът '{title}' беше редактиран успешно!", "success")
        return redirect(url_for('admin_dashboard'))
        
    p_dict = dict(product)
    p_dict['id'] = p_dict['_id']
    return render_template('product_form.html', action="Редактиране", product=p_dict)

@app.route('/admin/delete-product/<string:id>', methods=['POST'])
def delete_product(id):
    if not check_auth():
        return redirect(url_for('admin_login'))
        
    client = get_convex_client()
    product = client.query("products:get", {"id": id})
    
    if product:
        title = product['title']
        client.mutation("products:remove", {"id": id})
        
        # Soft delete removes it from the catalog, so we delete its static file
        product_file = f"product-{id}.html"
        if os.path.exists(product_file):
            try:
                os.remove(product_file)
            except OSError as e:
                print(f"Error deleting file {product_file}: {e}")
                
        trigger_rebuild_async()
        flash(f"Продуктът '{title}' беше изтрит успешно!", "success")
    else:
        flash("Продуктът не беше намерен.", "danger")
        
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/upload-image-ajax', methods=['POST'])
def upload_image_ajax():
    if not check_auth():
        return jsonify({"error": "Unauthorized"}), 401
        
    file_obj = request.files.get('file')
    if not file_obj:
        return jsonify({"error": "No file uploaded"}), 400
        
    url = upload_image_to_convex(file_obj)
    if url:
        return jsonify({"url": url})
    return jsonify({"error": "Failed to upload image"}), 500

@app.route('/admin/settings', methods=['GET', 'POST'])
def admin_settings():
    if not check_auth():
        return redirect(url_for('admin_login'))
        
    client = get_convex_client()
    
    if request.method == 'POST':
        import json
        
        try:
            hero_slides = json.loads(request.form.get('hero_slides_json', '[]'))
        except Exception:
            hero_slides = []
            
        try:
            categories = json.loads(request.form.get('categories_json', '[]'))
        except Exception:
            categories = []
            
        fendt_title = request.form.get('fendt_title', '').strip()
        fendt_subtitle = request.form.get('fendt_subtitle', '').strip()
        fendt_img = request.form.get('fendt_img', '').strip()
        
        about_sec1Title = request.form.get('about_sec1Title', '').strip()
        about_sec1Desc = request.form.get('about_sec1Desc', '').strip()
        about_sec1Img = request.form.get('about_sec1Img', '').strip()
        about_sec2Title = request.form.get('about_sec2Title', '').strip()
        about_sec2Desc = request.form.get('about_sec2Desc', '').strip()
        about_sec2Img = request.form.get('about_sec2Img', '').strip()
        about_sec3Title = request.form.get('about_sec3Title', '').strip()
        about_sec3Desc = request.form.get('about_sec3Desc', '').strip()
        about_sec3Img = request.form.get('about_sec3Img', '').strip()
        
        contacts_officeTitle = request.form.get('contacts_officeTitle', '').strip()
        contacts_officeAddress = request.form.get('contacts_officeAddress', '').strip()
        contacts_workingHoursTitle = request.form.get('contacts_workingHoursTitle', '').strip()
        contacts_workingHoursDesc = request.form.get('contacts_workingHoursDesc', '').strip()
        contacts_phoneTitle = request.form.get('contacts_phoneTitle', '').strip()
        contacts_phoneNum = request.form.get('contacts_phoneNum', '').strip()
        contacts_phoneDesc = request.form.get('contacts_phoneDesc', '').strip()
        contacts_networksTitle = request.form.get('contacts_networksTitle', '').strip()
        contacts_networksDesc = request.form.get('contacts_networksDesc', '').strip()
        
        cities_str = request.form.get('contacts_cities_str', '').strip()
        cities = [c.strip() for c in cities_str.split(',') if c.strip()]
        
        payload = {
            "heroSlides": hero_slides,
            "categories": categories,
            "fendtPromo": {
                "title": fendt_title,
                "subtitle": fendt_subtitle,
                "img": fendt_img
            },
            "aboutPage": {
                "sec1Title": about_sec1Title,
                "sec1Desc": about_sec1Desc,
                "sec1Img": about_sec1Img,
                "sec2Title": about_sec2Title,
                "sec2Desc": about_sec2Desc,
                "sec2Img": about_sec2Img,
                "sec3Title": about_sec3Title,
                "sec3Desc": about_sec3Desc,
                "sec3Img": about_sec3Img
            },
            "contactsPage": {
                "officeTitle": contacts_officeTitle,
                "officeAddress": contacts_officeAddress,
                "workingHoursTitle": contacts_workingHoursTitle,
                "workingHoursDesc": contacts_workingHoursDesc,
                "phoneTitle": contacts_phoneTitle,
                "phoneNum": contacts_phoneNum,
                "phoneDesc": contacts_phoneDesc,
                "networksTitle": contacts_networksTitle,
                "networksDesc": contacts_networksDesc,
                "cities": cities
            }
        }
        
        client.mutation("settings:update", payload)
        flash("Настройките на сайта бяха запазени успешно!", "success")
        return redirect(url_for('admin_settings'))
        
    settings = client.query("settings:get")
    return render_template('settings_form.html', settings=settings)

@app.route('/')
@app.route('/index.html')
def ssr_home():
    machines = load_machines_from_db()
    settings = load_settings_from_db()
    body = get_index_body(machines, settings)
    html_content = page('Нова Машина – Сайт No.1 за лизинг на селскостопанска техника', body, 'home')
    return html_content

@app.route('/about')
@app.route('/about.html')
def ssr_about():
    settings = load_settings_from_db()
    body = get_about_body(settings)
    html_content = page('За Нова Машина', body, 'about')
    return html_content

@app.route('/contacts')
@app.route('/contacts.html')
def ssr_contacts():
    settings = load_settings_from_db()
    body = get_contacts_body(settings)
    html_content = page('Контакти – Нова Машина', body, 'contacts')
    return html_content

@app.route('/catalog')
@app.route('/catalog.html')
def ssr_catalog():
    machines = load_machines_from_db()
    body = get_catalog_body(machines)
    html_content = page('Оферти за нова и употребявана техника на лизинг', body, 'catalog')
    return html_content

@app.route('/product/<string:id>')
@app.route('/product-<string:id>.html')
def ssr_product(id):
    machines = load_machines_from_db()
    prod = next((m for m in machines if m['id'] == id), None)
    if not prod:
        return page('Машината не е намерена', '<h1>Офертата не е намерена</h1><p>Изглежда тази машина вече не е активна или е изтрита.</p>', 'catalog'), 404
        
    state = 'Нов' if prod['state'] == 'new' else 'Употребяван'
    title = f'{state} {prod["title"]}, {prod["fuel"]} | {prod["offer"]}'
    body = product_page(prod)
    html_content = page(title, body, 'catalog')
    return html_content

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
