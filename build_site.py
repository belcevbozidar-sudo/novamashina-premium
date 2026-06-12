# -*- coding: utf-8 -*-
# Генератор на страниците на novamashina.bg (огледална структура на novakola.bg)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

EUR = "€"

# ---------------------------------------------------------------- ИКОНИ (inline SVG)
I = {
 'logo': '''<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg"><rect x="2" y="14" width="60" height="48" rx="12" fill="#4dbc4d"/><rect x="2" y="14" width="60" height="12" rx="6" fill="#006b3f"/><rect x="28" y="6" width="8" height="16" rx="3" fill="#006b3f"/><g transform="translate(9,24)"><rect x="2" y="12" width="26" height="12" rx="3" fill="#fff"/><rect x="24" y="4" width="14" height="20" rx="3" fill="#eafbea"/><rect x="27" y="7" width="8" height="8" rx="2" fill="#4dbc4d"/><circle cx="10" cy="28" r="6.5" fill="#0e4d2c"/><circle cx="10" cy="28" r="3" fill="#fff"/><circle cx="32" cy="26" r="8.5" fill="#0e4d2c"/><circle cx="32" cy="26" r="4" fill="#fff"/><rect x="6" y="6" width="3.5" height="8" fill="#0e4d2c"/></g></svg>''',
 'spark': '''<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2l1.8 5.6L19 9l-5.2 1.4L12 16l-1.8-5.6L5 9l5.2-1.4L12 2z" fill="#4dbc4d"/><path d="M19 14l.9 2.6L22 17l-2.1.7L19 20l-.9-2.3L16 17l2.1-.4L19 14z" fill="#4dbc4d"/><path d="M5 15l.7 2L8 17.6l-2.3.8L5 20l-.7-1.6L2 17.6 4.3 17 5 15z" fill="#4dbc4d"/></svg>''',
 'send': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M3 11.5L21 3l-8.5 18-2.3-7.2L3 11.5z" fill="none" stroke="#4dbc4d" stroke-width="2" stroke-linejoin="round"/></svg>''',
 'info': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" fill="none" stroke="#969696" stroke-width="1.6"/><rect x="11.1" y="10" width="1.8" height="7" rx=".9" fill="#969696"/><circle cx="12" cy="7" r="1.2" fill="#969696"/></svg>''',
 'compare': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M7 7h11M15 4l3 3-3 3M17 17H6M9 14l-3 3 3 3" fill="none" stroke="#4dbc4d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>''',
 'heart': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 20s-7.5-4.8-9.3-9.1C1.3 7.6 3.3 4.5 6.6 4.5c2 0 3.6 1.1 4.4 2.7l1 .1c.8-1.7 2.4-2.8 4.4-2.8 3.3 0 5.3 3.1 3.9 6.4C18.5 15.2 12 20 12 20z" fill="none" stroke="#4dbc4d" stroke-width="1.8"/></svg>''',
 'share': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="6" cy="12" r="2.6" fill="none" stroke="#4dbc4d" stroke-width="1.8"/><circle cx="17.5" cy="5.5" r="2.6" fill="none" stroke="#4dbc4d" stroke-width="1.8"/><circle cx="17.5" cy="18.5" r="2.6" fill="none" stroke="#4dbc4d" stroke-width="1.8"/><path d="M8.4 10.8l6.7-4M8.4 13.2l6.7 4" stroke="#4dbc4d" stroke-width="1.8"/></svg>''',
 'fuel': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><rect x="4" y="3" width="10" height="18" rx="2" fill="none" stroke="#6c6c6c" stroke-width="1.7"/><rect x="6.5" y="5.5" width="5" height="4" rx="1" fill="#6c6c6c"/><path d="M14 9h2.4a1.6 1.6 0 011.6 1.6V17a1.5 1.5 0 003 0v-6l-2-2" fill="none" stroke="#6c6c6c" stroke-width="1.7" stroke-linecap="round"/></svg>''',
 'power': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M7 21h10M9 21V10a3 3 0 016 0v11M12 3v4M8 5l1.5 2.5M16 5l-1.5 2.5" fill="none" stroke="#6c6c6c" stroke-width="1.7" stroke-linecap="round"/></svg>''',
 'gear': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="8.6" fill="none" stroke="#6c6c6c" stroke-width="1.7"/><text x="12" y="15.5" text-anchor="middle" font-family="Arial" font-weight="bold" font-size="9.5" fill="#6c6c6c">М</text></svg>''',
 'pin': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 21s-6.4-5.4-7.7-9.6C3.3 8 6 4 12 4s8.7 4 7.7 7.4C18.4 15.6 12 21 12 21z" fill="none" stroke="#6c6c6c" stroke-width="1.7"/><circle cx="12" cy="10.5" r="2.4" fill="#6c6c6c"/></svg>''',
 'clock': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9" fill="none" stroke="#6c6c6c" stroke-width="1.7"/><path d="M12 6.5V12l3.6 2.4" fill="none" stroke="#6c6c6c" stroke-width="1.7" stroke-linecap="round"/></svg>''',
 'cal': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><rect x="3.5" y="5" width="17" height="16" rx="2.5" fill="none" stroke="#6c6c6c" stroke-width="1.7"/><path d="M3.5 9.5h17M8 3v4M16 3v4" stroke="#6c6c6c" stroke-width="1.7" stroke-linecap="round"/></svg>''',
 'tractor-badge': '''<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect x="4" y="14" width="18" height="9" rx="2.5" fill="#fff"/><rect x="19" y="8" width="10" height="15" rx="2.5" fill="#fff" opacity=".85"/><rect x="21.5" y="10.5" width="5" height="5.5" rx="1.2" fill="#4dbc4d"/><circle cx="10" cy="26.5" r="4.6" fill="#fff"/><circle cx="25.5" cy="25.5" r="6" fill="#fff"/><circle cx="10" cy="26.5" r="2" fill="#4dbc4d"/><circle cx="25.5" cy="25.5" r="2.6" fill="#4dbc4d"/><rect x="7" y="9" width="2.6" height="6" fill="#fff"/></svg>''',
 'recycle-badge': '''<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M20 7a13 13 0 0111.5 7l-3.4 1.9A9 9 0 0020 11z" fill="#fff"/><path d="M33 22a13 13 0 01-9.5 10.6l-1-3.8A9 9 0 0029 22z" fill="#fff"/><path d="M9 28A13 13 0 017.2 15.5l3.8 1.2A9 9 0 0012 25z" fill="#fff"/><polygon points="29,12 34,16 28,18" fill="#fff"/><polygon points="24,34 18,33 22,28" fill="#fff"/><polygon points="6,24 8,18 12,23" fill="#fff"/></svg>''',
 'flag': '''<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M10 36V6" stroke="#2f8a2f" stroke-width="3" stroke-linecap="round"/><path d="M12 7c6-3 10 3 17 0v12c-7 3-11-3-17 0z" fill="#4dbc4d"/></svg>''',
 'medal': '''<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="16" r="9" fill="none" stroke="#2f8a2f" stroke-width="2.6"/><circle cx="20" cy="16" r="4.5" fill="#4dbc4d"/><path d="M14 23l-4 11 7-4M26 23l4 11-7-4" fill="none" stroke="#2f8a2f" stroke-width="2.6" stroke-linejoin="round"/></svg>''',
 'shield': '''<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M20 4l13 5v9c0 9-5.6 15.4-13 18C12.6 33.4 7 27 7 18V9z" fill="#2f8a2f"/><path d="M13.5 19.5l4.5 4.5 8.5-9" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>''',
 'person': '''<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><circle cx="20" cy="13" r="7" fill="#4dbc4d"/><path d="M6 36c1.5-8 7-12 14-12s12.5 4 14 12z" fill="#4dbc4d"/></svg>''',
 'farm': '''<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><path d="M6 18L20 7l14 11" fill="none" stroke="#2f8a2f" stroke-width="2.8" stroke-linecap="round"/><rect x="10" y="18" width="20" height="15" fill="#4dbc4d"/><rect x="17" y="24" width="6" height="9" fill="#fff"/></svg>''',
 'leaseret': '''<svg viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg"><rect x="6" y="14" width="16" height="8" rx="2" fill="#2f8a2f"/><rect x="19" y="9" width="9" height="13" rx="2" fill="#2f8a2f"/><circle cx="11" cy="25" r="4" fill="#2f8a2f"/><circle cx="25" cy="24" r="5" fill="#2f8a2f"/><path d="M30 12a9 9 0 014 7l3-1M10 31a9 9 0 01-4-7l-3 1" fill="none" stroke="#4dbc4d" stroke-width="2.4" stroke-linecap="round"/></svg>''',
 'search': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="#4dbc4d" stroke-width="2"/><path d="M15.5 15.5L21 21" stroke="#4dbc4d" stroke-width="2" stroke-linecap="round"/></svg>''',
 'ext': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M14 5h5v5M19 5l-8 8M19 13.5V19H5V5h5.5" fill="none" stroke="#4dbc4d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>''',
 'phone': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M5 4h4l2 5-2.5 1.5a12 12 0 005 5L15 13l5 2v4a2 2 0 01-2 2A15 15 0 013 6a2 2 0 012-2z" fill="none" stroke="#4dbc4d" stroke-width="1.8" stroke-linejoin="round"/></svg>''',
 'mail': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="5.5" width="18" height="13" rx="2" fill="none" stroke="#4dbc4d" stroke-width="1.8"/><path d="M4 7l8 6 8-6" fill="none" stroke="#4dbc4d" stroke-width="1.8"/></svg>''',
 'pin-g': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 21s-6.4-5.4-7.7-9.6C3.3 8 6 4 12 4s8.7 4 7.7 7.4C18.4 15.6 12 21 12 21z" fill="none" stroke="#4dbc4d" stroke-width="1.8"/><circle cx="12" cy="10.5" r="2.4" fill="#4dbc4d"/></svg>''',
 'fb': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="11" fill="#4dbc4d"/><path d="M13.4 19v-6h2l.4-2.4h-2.4V9.2c0-.7.3-1.2 1.3-1.2h1.2V5.9c-.3 0-1 0-1.8 0-1.9 0-3.1 1.1-3.1 3.1v1.6H9V13h2v6z" fill="#fff"/></svg>''',
 'ig': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><rect x="2.5" y="2.5" width="19" height="19" rx="5.5" fill="none" stroke="#4dbc4d" stroke-width="2"/><circle cx="12" cy="12" r="4.4" fill="none" stroke="#4dbc4d" stroke-width="2"/><circle cx="17.4" cy="6.6" r="1.4" fill="#4dbc4d"/></svg>''',
 'checkc': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" fill="none" stroke="#4dbc4d" stroke-width="1.8"/><path d="M7.5 12.5l3 3 6-7" fill="none" stroke="#4dbc4d" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>''',
 'calc-ico': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><rect x="5" y="3" width="14" height="18" rx="2.5" fill="none" stroke="#fff" stroke-width="1.8"/><rect x="8" y="6" width="8" height="3.4" rx="1" fill="#fff"/><g fill="#fff"><circle cx="9" cy="13" r="1.2"/><circle cx="12" cy="13" r="1.2"/><circle cx="15" cy="13" r="1.2"/><circle cx="9" cy="17" r="1.2"/><circle cx="12" cy="17" r="1.2"/><circle cx="15" cy="17" r="1.2"/></g></svg>''',
 'firm': '''<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="8" r="4" fill="#4dbc4d"/><path d="M4 20c1-4.4 4-7 8-7s7 2.6 8 7z" fill="#4dbc4d"/></svg>''',
 'mach-new': '''<svg viewBox="0 0 28 28" xmlns="http://www.w3.org/2000/svg"><rect x="2" y="10" width="13" height="7" rx="2" fill="#4dbc4d"/><rect x="13" y="6" width="8" height="11" rx="2" fill="#0e4d2c"/><circle cx="7" cy="20" r="3.4" fill="#333"/><circle cx="18.5" cy="19.5" r="4.4" fill="#333"/><path d="M23 8l1 2.8 2.8 1-2.8 1L23 16l-1-3.2-2.8-1 2.8-1z" fill="#4dbc4d"/></svg>''',
 'mach-used': '''<svg viewBox="0 0 28 28" xmlns="http://www.w3.org/2000/svg"><rect x="2" y="10" width="13" height="7" rx="2" fill="#6c6c6c"/><rect x="13" y="6" width="8" height="11" rx="2" fill="#444"/><circle cx="7" cy="20" r="3.4" fill="#333"/><circle cx="18.5" cy="19.5" r="4.4" fill="#333"/><path d="M22 6a6.5 6.5 0 012.8 5l2-.7" fill="none" stroke="#4dbc4d" stroke-width="1.8" stroke-linecap="round"/></svg>''',
 'mach-lease': '''<svg viewBox="0 0 28 28" xmlns="http://www.w3.org/2000/svg"><rect x="2" y="10" width="13" height="7" rx="2" fill="#e8762d"/><rect x="13" y="6" width="8" height="11" rx="2" fill="#9e4a14"/><circle cx="7" cy="20" r="3.4" fill="#333"/><circle cx="18.5" cy="19.5" r="4.4" fill="#333"/></svg>''',
 'mach-all': '''<svg viewBox="0 0 28 28" xmlns="http://www.w3.org/2000/svg"><rect x="1" y="11" width="12" height="6.5" rx="2" fill="#4dbc4d"/><rect x="11" y="7" width="7" height="10" rx="2" fill="#0e4d2c"/><circle cx="6" cy="20" r="3" fill="#333"/><circle cx="16" cy="19.5" r="3.8" fill="#333"/><rect x="18" y="9" width="9" height="5" rx="1.5" fill="#caebca"/><circle cx="21" cy="17" r="2.4" fill="#666"/><circle cx="25" cy="17" r="2.4" fill="#666"/></svg>''',
}

# ---------------------------------------------------------------- ДАННИ: МАШИНИ
MACHINES = [
 dict(id=1, slug='john-deere-6r-150', brand='John Deere', model='6R 150', title='John Deere 6R 150',
      cat='Трактор', state='new', img='tractor-green.jpg', price=152900, monthly=1254,
      fuel='Дизел', hp='150 к.с.', trans='AutoPowr 50 км/ч', loc='гр. Стара Загора', year='2026 г.', hours=None,
      dealer='Агротех България ООД', offer='NMN100214', views=842, engine='6.8 л, 6 цил.', tank='ДДС вкл.',
      desc='Купи нов John Deere 6R 150 на лизинг с атрактивна месечна вноска от €1 254 / 2 453 лв. и цена на машината €152 900 / 299 047 лв.'),
 dict(id=2, slug='claas-lexion-5400', brand='CLAAS', model='LEXION 5400', title='CLAAS LEXION 5400',
      cat='Комбайн', state='new', img='combine-yellow.jpg', price=389000, monthly=3190,
      fuel='Дизел', hp='313 к.с.', trans='CMATIC', loc='гр. Добрич', year='2026 г.', hours=None, engine='8.9 л, 6 цил.',
      offer='NMN100377', views=1174, dealer='Агро Лидер ООД', tank='ДДС вкл.',
      desc='Купи нов CLAAS LEXION 5400 на лизинг с атрактивна месечна вноска от €3 190 / 6 239 лв. и цена на машината €389 000 / 760 818 лв.'),
 dict(id=3, slug='new-holland-t6-180', brand='New Holland', model='T6.180', title='New Holland T6.180',
      cat='Трактор', state='used', img='tractor-blue.jpg', price=78500, monthly=644,
      fuel='Дизел', hp='175 к.с.', trans='Electro Command', loc='гр. Русe', year='2021 г.', hours='4 200 мч', engine='6.7 л, 6 цил.',
      offer='NMN100455', views=689, dealer='Фермер Машини ЕООД', tank='ДДС вкл.',
      desc='Купи употребяван New Holland T6.180 на лизинг с атрактивна месечна вноска от €644 / 1 260 лв. и цена на машината €78 500 / 153 533 лв.'),
 dict(id=4, slug='case-ih-puma-165', brand='Case IH', model='Puma 165', title='Case IH Puma 165',
      cat='Трактор', state='used', img='tractor-red.jpg', price=64900, monthly=532,
      fuel='Дизел', hp='165 к.с.', trans='Full Powershift', loc='гр. Плевен', year='2019 г.', hours='6 800 мч', engine='6.7 л, 6 цил.',
      offer='NMN100502', views=914, dealer='Агрикола Трейд ООД', tank='ДДС вкл.',
      desc='Купи употребяван Case IH Puma 165 на лизинг с атрактивна месечна вноска от €532 / 1 040 лв. и цена на машината €64 900 / 126 933 лв.'),
 dict(id=5, slug='fendt-724-vario', brand='Fendt', model='724 Vario', title='Fendt 724 Vario',
      cat='Трактор', state='new', img='tractor-lime.jpg', price=248700, monthly=2039,
      fuel='Дизел', hp='246 к.с.', trans='Vario безстепенна', loc='гр. София', year='2026 г.', hours=None, engine='6.1 л, 6 цил.',
      offer='NMN100618', views=1532, dealer='Силоз Агро ЕООД', tank='ДДС вкл.',
      desc='Купи нов Fendt 724 Vario на лизинг с атрактивна месечна вноска от €2 039 / 3 988 лв. и цена на машината €248 700 / 486 415 лв.'),
 dict(id=6, slug='amazone-cirrus-6003', brand='Amazone', model='Cirrus 6003-2', title='Amazone Cirrus 6003-2',
      cat='Сеялка', state='new', img='seeder.jpg', price=112300, monthly=921,
      fuel='Прикачна', hp='6 м работна ширина', trans='ISOBUS', loc='гр. Пловдив', year='2026 г.', hours=None, engine='—',
      offer='NMN100704', views=455, dealer='Земеделска Техника ЕООД', tank='ДДС вкл.',
      desc='Купи нова сеялка Amazone Cirrus 6003-2 на лизинг с атрактивна месечна вноска от €921 / 1 801 лв. и цена €112 300 / 219 640 лв.'),
 dict(id=7, slug='massey-ferguson-8s-205', brand='Massey Ferguson', model='8S.205', title='Massey Ferguson 8S.205',
      cat='Трактор', state='new', img='tractor-orange.jpg', price=198400, monthly=1627,
      fuel='Дизел', hp='205 к.с.', trans='Dyna-7', loc='гр. Бургас', year='2026 г.', hours=None, engine='7.4 л, 6 цил.',
      offer='NMN100791', views=698, dealer='БГ Агро Машини ООД', tank='ДДС вкл.',
      desc='Купи нов Massey Ferguson 8S.205 на лизинг с атрактивна месечна вноска от €1 627 / 3 182 лв. и цена на машината €198 400 / 388 037 лв.'),
 dict(id=8, slug='claas-tucano-580', brand='CLAAS', model='TUCANO 580', title='CLAAS TUCANO 580',
      cat='Комбайн', state='used', img='combine-green.jpg', price=145000, monthly=1189,
      fuel='Дизел', hp='299 к.с.', trans='Хидростатична', loc='гр. Сливен', year='2020 г.', hours='2 350 мч', engine='8.7 л, 6 цил.',
      offer='NMN100846', views=1043, dealer='Комбайн Сервиз ООД', tank='ДДС вкл.',
      desc='Купи употребяван CLAAS TUCANO 580 на лизинг с атрактивна месечна вноска от €1 189 / 2 326 лв. и цена €145 000 / 283 595 лв.'),
]

def calculate_initial_monthly(price, state):
    pv = price * 0.20
    os = price * 0.10
    financed = price - pv
    interest_rate = 0.035 if state == 'new' else 0.045
    r = interest_rate / 12
    n = 60
    if r > 0:
        pv_factor = 0.0
        for t in range(1, n + 1):
            pv_factor += 1.0 / ((1.0 + r) ** t)
        pmt = (financed - os / ((1.0 + r) ** n)) / pv_factor
    else:
        pmt = (financed - os) / n
    return int(round(pmt))

for m in MACHINES:
    m['monthly'] = calculate_initial_monthly(m['price'], m['state'])

def fmt(n):
    return f"{n:,}".replace(",", " ")

# ---------------------------------------------------------------- ХЕДЪР / ФУТЪР
def header(active=''):
    def cls(k): return ' class="active"' if k == active else ''
    return f'''
<header class="site-header">
  <div class="container">
    <div class="header-top">
      <a class="logo" href="index.html">
        {I['logo']}
        <span>
          <span class="logo-text">NOVA <span>MASHINA</span><small style="font-size:15px">.BG</small></span>
          <div class="logo-sub">селскостопанска техника на лизинг</div>
        </span>
      </a>
      <div class="header-top-right">
        <a class="btn-ai" href="#ai">{I['spark'].replace('#4dbc4d', '#ffffff')} AI Асистент</a>
        <div class="auth-links"><a href="#">Вход</a><span>|</span><a href="#">Регистрация</a></div>
        <a class="compare-link" href="#">{I['compare']} Сравни оферти</a>
        <div class="powered-by"><div class="pb-label">Powered by</div><div class="pb-brand">ЗЛАТЕКС</div></div>
      </div>
    </div>
    <div class="header-nav">
      <nav class="main-nav">
        <a href="index.html"{cls('home')}>Начало</a>
        <a href="catalog.html"{cls('catalog')}>Машини на лизинг</a>
        <a href="calculator.html"{cls('calc')}>Лизингов калкулатор</a>
        <a href="budget-calculator.html"{cls('budget')}>Бюджетен калкулатор</a>
        <a href="dealers.html"{cls('dealers')}>Търговци</a>
        <a href="news.html"{cls('news')}>Новини</a>
        <a href="about.html"{cls('about')}>За нас</a>
        <a href="contacts.html"{cls('contacts')}>Контакти</a>
      </nav>
      <div class="nav-right">
        <div class="currency-toggle">
          <button type="button" class="cur-eur active" onclick="setCurrency('EUR')">Евро</button>
          <button type="button" class="cur-bgn" onclick="setCurrency('BGN')">Лева</button>
        </div>
        <a class="btn-add" href="#"><span class="plus">+</span> Добави<br>обява</a>
      </div>
    </div>
  </div>
</header>'''

FOOTER = f'''
<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <a class="logo" href="index.html">
        {I['logo']}
        <span>
          <span class="logo-text">NOVA <span>MASHINA</span><small style="font-size:15px">.BG</small></span>
          <div class="logo-sub">селскостопанска техника на лизинг</div>
        </span>
      </a>
      <div class="powered-by"><div class="pb-label">Powered by</div><div class="pb-brand" style="font-size:24px">ЗЛАТЕКС</div></div>
    </div>
    <div class="footer-grid">
      <div class="f-col f-contacts">
        <h5>Контакти</h5>
        <div class="f-item">{I['pin-g']}<span>Централа на ЗЛАТЕКС ООД<br>гр. Стара Загора, бул. Никола Петков 55</span></div>
        <div class="f-item">{I['phone']}<span>+359 88 510 4040<br>+359 42 600 046</span></div>
        <div class="f-item">{I['mail']}<span>contact@novamashina.bg</span></div>
        <div class="socials">
          <a href="#" aria-label="Facebook">{I['fb']}</a>
          <a href="#" aria-label="Instagram">{I['ig']}</a>
        </div>
      </div>
      <div class="f-col f-links">
        <h5>Полезни връзки</h5>
        <a href="#">Вход за потребители</a>
        <a href="#">Вход за дилъри</a>
        <a href="#">Регистрация на оферта</a>
        <a href="#">Златекс Лизинг</a>
        <a href="#">Застрахователен брокер</a>
      </div>
      <div class="f-col f-ai">
        <div class="ai-box">
          <div class="ai-box-badge">
            <span class="ai-dot-pulse"></span>
            <span>АгроAI Онлайн</span>
          </div>
          <h5>Попитайте нашия AI Асистент</h5>
          <p>Намерете бързо точната машина и най-изгодните лизингови условия.</p>
          <a class="ai-link" href="#ai">Задай въпрос {I['spark']}</a>
        </div>
      </div>
      <div class="f-col newsletter">
        <h5>Бюлетин</h5>
        <p class="nl-desc">Абонирайте се за най-новите и изгодни оферти на пазара.</p>
        <div class="nl-form">
          <input type="text" placeholder="Вашето име">
          <input type="email" placeholder="Имейл адрес">
          <button class="btn-send" type="button">Абониране</button>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Нова Машина</span>
      <div class="fb-links"><a href="#">Общи условия</a><a href="#">Права и условия за ползване</a></div>
      <span>Уеб сайт от ЗЛАТЕКС ООД</span>
    </div>
  </div>
</footer>'''

def page(title, body, active='', extra_head=''):
    return f'''<!DOCTYPE html>
<html lang="bg">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="NovaMashina.bg – Сайт No.1 за лизинг на селскостопанска техника. Нови и употребявани трактори, комбайни, сеялки, пръскачки, ремаркета и инвентар.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<link rel="icon" type="image/svg+xml" href="img/cat-tractors.svg">
{extra_head}
</head>
<body>
{header(active)}
{body}
{FOOTER}
<script src="js/main.js"></script>
</body>
</html>'''

# ---------------------------------------------------------------- ПРОДУКТОВА КАРТА
def offer_card(m, link=True):
    badge = ('<div class="badge new">' + I['tractor-badge'] + '<span>НОВА</span></div>') if m['state'] == 'new' \
        else ('<div class="badge used">' + I['recycle-badge'] + '<span>УПОТРЕБЯВАНА</span></div>')
    corner = ''
    if m.get('lease_ret'):
        corner = '<div class="lease-corner"><span>Лизингова машина</span></div>'
    specs = []
    if m['hours']:
        specs.append(f'<div class="spec">{I["clock"]}<span>{m["hours"]}</span></div>')
        specs.append(f'<div class="spec">{I["cal"]}<span>{m["year"]}</span></div>')
    specs.append(f'<div class="spec">{I["fuel"]}<span>{m["fuel"]}</span></div>')
    specs.append(f'<div class="spec">{I["power"]}<span>{m["hp"]}</span></div>')
    specs.append(f'<div class="spec">{I["gear"]}<span>{m["trans"]}</span></div>')
    specs.append(f'<div class="spec">{I["pin"]}<span>{m["loc"]}</span></div>')
    href = f'product-{m["id"]}.html'
    title_tag = f'<a href="{href}" style="color:inherit">{m["title"]}</a>' if link else m['title']
    return f'''
<article class="offer-card">
  <a class="offer-media" href="{href}">
    {badge}{corner}
    <img src="img/{m['img']}" alt="{m['title']}">
    <div class="ribbon">
      <div class="monthly">
        <div class="m-price"><span class="money" data-eur="{m['monthly']}">€{fmt(m['monthly'])}</span> <small>/мес</small></div>
        <div class="m-note">без ДДС средна вноска</div>
      </div>
      <div class="total">
        <div class="t-label">ЦЕНА:</div>
        <div class="t-price money" data-eur="{m['price']}">€{fmt(m['price'])}</div>
      </div>
    </div>
  </a>
  <h3 class="offer-title">{title_tag}</h3>
  <div class="offer-specs {'two' if not m['hours'] else ''}">{''.join(specs)}</div>
  <div class="offer-actions">
    <a href="#">{I['compare']} Сравни</a><span class="sep"></span><a href="#">{I['heart']} Любими</a>
  </div>
</article>'''

# ---------------------------------------------------------------- ФОРМА ЗА ТЪРСЕНЕ
SEARCH_FORM = f'''
<div class="search-card" id="search">
  <div class="search-grid">
    <div class="field">
      <label>Избери марка:</label>
      <div class="select-wrap"><select><option>Марка</option><option>John Deere</option><option>CLAAS</option><option>New Holland</option><option>Case IH</option><option>Fendt</option><option>Massey Ferguson</option><option>Deutz-Fahr</option><option>Kubota</option><option>Valtra</option><option>Zetor</option><option>Amazone</option><option>Lemken</option><option>Väderstad</option><option>Hardi</option></select></div>
    </div>
    <div class="field">
      <label>Избери модел:</label>
      <div class="select-wrap"><select><option>Модел</option></select></div>
    </div>
    <div class="field">
      <label>Месечна вноска (€):</label>
      <div class="range-pair">
        <div class="range-input"><span class="prefix">от</span><input type="text" value="0"><div class="range-note">0.00лв</div></div>
        <div class="range-input"><span class="prefix">до</span><input type="text" value="8500"><div class="range-note">16 624.56лв</div></div>
      </div>
    </div>
    <div class="field">
      <label>Първоначална вноска (€):</label>
      <div class="range-pair">
        <div class="range-input"><span class="prefix">от</span><input type="text" value="1000"></div>
        <div class="range-input"><span class="prefix">до</span><input type="text" value="142000"></div>
      </div>
    </div>
  </div>
  <div class="search-bottom">
    <div class="field">
      <label>1-ва регистрация</label>
      <div class="range-input"><span class="prefix">след</span><input type="text" value="2016"></div>
    </div>
    <div class="field">
      <label>Моточасове</label>
      <div class="range-input"><span class="prefix">до</span><input type="text" value="10000"></div>
    </div>
    <div class="search-actions">
      <a class="btn-show" href="catalog.html" style="color:#fff">Покажи</a>
      <span class="more-params">⊕ още параметри</span>
    </div>
    <div class="checks">
      <label class="check"><input type="checkbox" checked><span class="box"></span> Нови</label>
      <label class="check"><input type="checkbox" checked><span class="box"></span> Употребявани</label>
      <label class="check"><input type="checkbox"><span class="box"></span> Трактори</label>
      <label class="check"><input type="checkbox"><span class="box"></span> Комбайни</label>
      <label class="check"><input type="checkbox"><span class="box"></span> Сеялки</label>
      <label class="check"><input type="checkbox"><span class="box"></span> Пръскачки</label>
      <label class="check"><input type="checkbox"><span class="box"></span> Ремаркета</label>
      <label class="check"><input type="checkbox"><span class="box"></span> Инвентар</label>
    </div>
  </div>
  <div class="powered-mini">Powered by <b>ЗЛАТЕКС Лизинг</b></div>
</div>'''

# ---------------------------------------------------------------- НАЧАЛНА СТРАНИЦА
new_cards = ''.join(offer_card(m) for m in MACHINES if m['state'] == 'new')
used_machs = [dict(m) for m in MACHINES if m['state'] == 'used']
used_machs[0]['lease_ret'] = True
used_cards = ''.join(offer_card(m) for m in used_machs)

index_body = f'''
<section class="hero">
  <img class="hero-bg" src="img/hero-field.jpg" alt="">
  <svg class="hero-badge" viewBox="0 0 130 130"><circle cx="65" cy="65" r="60" fill="#0e2d14"/><circle cx="65" cy="65" r="60" fill="none" stroke="#4dbc4d" stroke-width="3" stroke-dasharray="6 7"/><text x="65" y="50" text-anchor="middle" font-family="Comfortaa" font-weight="700" font-size="13" fill="#4dbc4d">ПРОЛЕТНА</text><text x="65" y="70" text-anchor="middle" font-family="Comfortaa" font-weight="700" font-size="13" fill="#fff">КАМПАНИЯ</text><text x="65" y="90" text-anchor="middle" font-family="Comfortaa" font-weight="700" font-size="11" fill="#4dbc4d">-3,33% ЛИХВА</text></svg>
  <div class="hero-inner">
    <h1 class="hero-title">Вземи John Deere 6R 150<br>с 3,33% лихва и подаръци до<br>30.6.2026г.</h1>
  </div>
</section>

<div class="ai-search" id="ai">
  <div class="ai-search-row">
    <span class="ai-sparkle">{I['spark']}</span>
    <div class="ai-input-wrap">
      <input type="text" id="aiInput" placeholder="Попитай нашия AI асистент за машина или лизингови условия...">
      <button class="ai-send" type="button">{I['send']}</button>
    </div>
  </div>
</div>

{SEARCH_FORM}

<section class="cats">
  <div class="cats-track">
    <a class="cat-card" href="catalog.html"><img src="img/cat-tractors.svg" alt="Трактори"><div class="cat-name">Трактори</div><div class="cat-count">412 активни оферти</div></a>
    <a class="cat-card" href="catalog.html"><img src="img/cat-combines.svg" alt="Комбайни"><div class="cat-name">Комбайни</div><div class="cat-count">126 активни оферти</div></a>
    <a class="cat-card" href="catalog.html"><img src="img/cat-seeders.svg" alt="Сеялки"><div class="cat-name">Сеялки</div><div class="cat-count">98 активни оферти</div></a>
    <a class="cat-card" href="catalog.html"><img src="img/cat-sprayers.svg" alt="Пръскачки"><div class="cat-name">Пръскачки</div><div class="cat-count">74 активни оферти</div></a>
    <a class="cat-card" href="catalog.html"><img src="img/cat-trailers.svg" alt="Ремаркета"><div class="cat-name">Ремаркета</div><div class="cat-count">63 активни оферти</div></a>
    <a class="cat-card" href="catalog.html"><img src="img/cat-inventar.svg" alt="Инвентар"><div class="cat-name">Инвентар</div><div class="cat-count">187 активни оферти</div></a>
  </div>
</section>

<section class="section container">
  <h2 class="section-title">Топ оферти за нова техника на лизинг</h2>
  <p class="section-sub">Специални предложения за налични машини с бърза доставка</p>
  <div class="offers-grid">
    {new_cards}
    <article class="promo-card">
      <img class="promo-bg" src="img/promo-fleet.jpg" alt="">
      <div class="promo-tag">{I['spark'].replace('#4dbc4d', '#ffffff')}<span>СПЕЦИАЛНИ<br>УСЛОВИЯ</span></div>
      <div class="promo-overlay">
        <h3>Немско инженерство на нова цена: Вземи своя нов Fendt от NovaMashina.bg с вноска от 950 €!</h3>
        <p>Специални условия: лихва 3,65% и атрактивни вноски до 30.06.2026 г</p>
      </div>
    </article>
    <article class="promo-card">
      <img class="promo-bg" src="img/promo-harvest.jpg" alt="">
      <div class="promo-overlay">
        <h3>Готови за жътва: Лимитирана серия CLAAS GO! Edition при ексклузивни условия от NovaMashina.bg</h3>
        <p>Месечна вноска от €1 990 и промоционална плаваща лихва 3.5%</p>
      </div>
    </article>
  </div>
  <div class="cta-center"><a class="btn-cta" href="catalog.html">Нова техника на лизинг</a></div>
</section>

<section class="section container">
  <h2 class="section-title">Употребявана техника на лизинг</h2>
  <p class="section-sub">Проверени, обслужени и върнати от лизинг машини с гаранция</p>
  <div class="offers-grid">
    {used_cards}
  </div>
  <div class="cta-center"><a class="btn-cta dark" href="catalog.html">Употребявана техника на лизинг</a></div>
</section>

<section class="two-sided container">
  <h2 class="two-sided-title">Търсиш или продаваш машина?<br><span class="brand">NovaMashina.bg</span> е твоето място</h2>
  <div class="two-sided-card">
    <div class="side">
      <h4>За купувачи</h4>
      <div class="lead">Само сигурни и проверени обяви за техника. Намери бързо машината, която търсиш.</div>
      <p>Разгледай хиляди оферти за нови и употребявани машини от официални представители и доверени търговци в цялата страна.</p>
      <a class="btn-cta" href="catalog.html">Разгледай обявите</a>
    </div>
    <svg class="two-sided-art" viewBox="0 0 220 160"><ellipse cx="110" cy="120" rx="100" ry="26" fill="#eef7ee"/><g transform="translate(40,30)"><rect x="10" y="36" width="80" height="34" rx="9" fill="#3f9e3f"/><rect x="78" y="12" width="44" height="58" rx="9" fill="#1f6b2d"/><rect x="84" y="20" width="32" height="26" rx="5" fill="#cfe3ef"/><circle cx="36" cy="78" r="20" fill="#2b2b2b"/><circle cx="36" cy="78" r="11" fill="#777"/><circle cx="100" cy="72" r="26" fill="#2b2b2b"/><circle cx="100" cy="72" r="14" fill="#777"/><rect x="20" y="14" width="9" height="20" rx="4" fill="#333"/></g><path d="M150 50 l24 -18 24 18" fill="none" stroke="#4dbc4d" stroke-width="5" stroke-linecap="round"/></svg>
    <div class="side">
      <h4>За продавачи</h4>
      <div class="lead">Публикувай обявата си тук, където клиентите търсят своята нова машина.</div>
      <p>Достигни до хиляди земеделски стопани и агрофирми. Публикуването е бързо, лесно и с пълно съдействие от нашия екип.</p>
      <a class="btn-cta dark" href="#">Добави обява</a>
    </div>
  </div>
</section>

<section class="seek-wrap">
  <div class="seek-card">
    <h3>Най-търсени марки</h3>
    <div class="seek-grid">
      <a href="catalog.html">John Deere</a><a href="catalog.html">CLAAS</a><a href="catalog.html">New Holland</a><a href="catalog.html">Case IH</a>
      <a href="catalog.html">Fendt</a><a href="catalog.html">Massey Ferguson</a><a href="catalog.html">Deutz-Fahr</a><a href="catalog.html">Kubota</a>
      <a href="catalog.html">Valtra</a><a href="catalog.html">Zetor</a><a href="catalog.html">Amazone</a><a href="catalog.html">Lemken</a>
      <a href="catalog.html">Väderstad</a><a href="catalog.html">Hardi</a><a href="catalog.html">Kverneland</a><a href="catalog.html">Pöttinger</a>
    </div>
  </div>
  <div class="seek-card">
    <h3>Най-търсени модели</h3>
    <div class="seek-grid cols-4">
      <a href="catalog.html">John Deere 6R</a><a href="catalog.html">CLAAS LEXION</a><a href="catalog.html">New Holland T6</a><a href="catalog.html">Case IH Puma</a>
      <a href="catalog.html">Fendt 724 Vario</a><a href="catalog.html">John Deere 8R</a><a href="catalog.html">CLAAS TUCANO</a><a href="catalog.html">Deutz-Fahr 6 Series</a>
      <a href="catalog.html">Massey Ferguson 8S</a><a href="catalog.html">Kubota M7</a><a href="catalog.html">CLAAS ARION</a><a href="catalog.html">New Holland CX</a>
      <a href="catalog.html">Amazone Cirrus</a><a href="catalog.html">Lemken Juwel</a><a href="catalog.html">Väderstad Rapid</a><a href="catalog.html">Hardi Aeon</a>
    </div>
  </div>
</section>'''

# ---------------------------------------------------------------- КАТАЛОГ
catalog_cards = []
order = [0, 2, 1, 3, 4, 7, 5, 6]
for i in order:
    catalog_cards.append(offer_card(MACHINES[i]))
catalog_cards.insert(2, f'''
<article class="promo-card">
  <img class="promo-bg" src="img/promo-fleet.jpg" alt="">
  <svg class="hero-badge" style="position:absolute;top:14px;right:14px;width:96px;height:96px" viewBox="0 0 130 130"><circle cx="65" cy="65" r="60" fill="#0e2d14"/><circle cx="65" cy="65" r="60" fill="none" stroke="#4dbc4d" stroke-width="3" stroke-dasharray="6 7"/><text x="65" y="56" text-anchor="middle" font-family="Comfortaa" font-weight="700" font-size="14" fill="#4dbc4d">ПРОЛЕТНА</text><text x="65" y="78" text-anchor="middle" font-family="Comfortaa" font-weight="700" font-size="14" fill="#fff">КАМПАНИЯ</text></svg>
  <div class="promo-overlay">
    <h3>Новият Deutz-Fahr 6160 вече е в NovaMashina.bg!</h3>
    <p>С месечна вноска от 1 152 €/2 253 лв. и отстъпка от цената</p>
  </div>
</article>''')

catalog_body = f'''
<main class="page container">
  {SEARCH_FORM.replace('id="search"', 'id="search" style="width:100%;margin-top:0"')}
  <h1 class="page-title green" style="margin-top:48px">Оферти за нова и употребявана техника на лизинг</h1>
  <p class="page-sub">Изберете своята машина от Нова Машина</p>
  <div class="catalog-toolbar">
    <div class="cat-tabs">
      <span class="cat-tab">{I['mach-new']} Нови</span>
      <span class="cat-tab">{I['mach-used']} Употребявани</span>
      <span class="cat-tab">{I['mach-lease']} Лизингови</span>
      <span class="cat-tab active">{I['mach-all']} Всички</span>
    </div>
    <div class="sort-links">
      <a href="#" class="active">Най-нови оферти ↑↓</a>
      <a href="#">Месечна вноска ↑↓</a>
      <a href="#">Цена ↑↓</a>
    </div>
  </div>
  <div class="offers-grid" style="margin-top:26px">
    {''.join(catalog_cards)}
  </div>
  <div class="cta-center"><a class="btn-cta" href="#search">Зареди още оферти</a></div>
</main>'''

# ---------------------------------------------------------------- ПРОДУКТОВИ СТРАНИЦИ
def product_page(m):
    state_label = 'НОВА<br>МАШИНА' if m['state'] == 'new' else 'УПОТРЕБЯВАНА'
    badge_cls = 'new' if m['state'] == 'new' else 'used'
    badge_ico = I['tractor-badge'] if m['state'] == 'new' else I['recycle-badge']
    hours_row = f'<div class="tech-row"><span class="k">Моточасове</span><span class="v">{m["hours"]}</span></div>' if m['hours'] else ''
    year_row = f'<div class="tech-row"><span class="k">Първа регистрация</span><span class="v">{m["year"]}</span></div>'
    price_bgn = fmt(round(m['price'] * 1.95583))
    features_cab = ['Кабина с пневматично окачване', 'Климатична инсталация', 'Седалка с въздушно окачване',
                    'LED работни светлини', 'Камера за заден ход', 'Мултифункционален джойстик',
                    'Дисплей с ISOBUS терминал', 'Автоматично управление GPS Ready', 'Радио с Bluetooth',
                    'Пътническа седалка', 'Регулируема кормилна колона', 'Тонирани стъкла']
    features_tech = ['Преден товарач — подготовка', 'Предна навесна система', 'Преден ВОМ',
                     'Хидравлични изводи — 4 двойки', 'Пневматична спирачна система', 'Теглич с автоматично захващане',
                     'Гуми с двойни колела — опция', 'Резервоар с голям обем', 'Автоматично смазване',
                     'Сензор за натоварване на навесната система', 'Електронно управление на двигателя', 'Круиз контрол']
    features_other = ['Гаранция от официален представител', 'Пълна сервизна история', 'Възможност за демонстрация',
                      'Доставка до клиента', 'Обучение на оператора', 'Разширена гаранция — опция',
                      'Застраховка Каско за машини', 'Финансиране чрез ЗЛАТЕКС Лизинг']
    li = lambda items: ''.join(f'<li>{x}</li>' for x in items)
    return f'''
<main class="page container">
  <div class="breadcrumb">
    <a href="index.html">Nova Mashina</a> / <a href="catalog.html">Машини на лизинг</a> / <a href="catalog.html">{m['brand']}</a> / <span>{m['title']}</span>
  </div>
  <div class="product-layout">
    <div>
      <div class="product-head">
        <h1>{m['title']}</h1>
        <div class="product-tools">
          <a href="#">{I['compare']} Добави за<br>сравнение</a>
          <a href="#">{I['heart']} Добави в<br>любими</a>
          <a href="#">{I['share']} Сподели с<br>приятели</a>
        </div>
      </div>
      <div class="gallery">
        <div class="badge {badge_cls}" style="top:14px">{badge_ico}<span>{state_label}</span></div>
        <div class="main-img"><img id="galMain" src="img/{m['img']}" alt="{m['title']}"></div>
        <button class="gal-nav prev" onclick="galPrev()"><svg viewBox="0 0 18 18"><path d="M12 2L5 9l7 7" fill="none" stroke="#333" stroke-width="2.4" stroke-linecap="round"/></svg></button>
        <button class="gal-nav next" onclick="galNext()"><svg viewBox="0 0 18 18"><path d="M6 2l7 7-7 7" fill="none" stroke="#333" stroke-width="2.4" stroke-linecap="round"/></svg></button>
      </div>
      <div class="thumbs" id="thumbs">
        <div class="th active" onclick="galSet(0)"><img src="img/{m['img']}" alt=""></div>
        <div class="th" onclick="galSet(1)"><img src="img/promo-fleet.jpg" alt=""></div>
        <div class="th" onclick="galSet(2)"><img src="img/hero-field.jpg" alt=""></div>
        <div class="th" onclick="galSet(3)"><img src="img/promo-harvest.jpg" alt=""></div>
      </div>
      <p class="disclaimer">Показаните изображения са илюстративни и информативни. Нова Машина запазва правото си на промяна на цените, цветовете и техническата информация на моделите.</p>
      <div class="offer-meta">
        <div class="om"><label>Оферта № (ID)</label><div>{m['offer']}</div></div>
        <div class="om"><label>Локация</label><div>{m['loc'].replace('гр. ', '')}</div></div>
        <div class="om"><label>Търговец</label><div><a href="dealers.html">{m['dealer']}</a></div></div>
      </div>
      <div class="views">Видяна <b>{m['views']}</b> пъти</div>

      <div class="block-label">Технически данни</div>
      <div class="tech-grid">
        <div class="tech-row"><span class="k">Двигател</span><span class="v">{m['engine']}</span></div>
        <div class="tech-row"><span class="k">Категория</span><span class="v">{m['cat']}</span></div>
        <div class="tech-row"><span class="k">Мощност</span><span class="v">{m['hp']}</span></div>
        <div class="tech-row"><span class="k">Трансмисия</span><span class="v">{m['trans']}</span></div>
        <div class="tech-row"><span class="k">Гориво</span><span class="v">{m['fuel']}</span></div>
        {year_row}
        {hours_row}
        <div class="tech-row"><span class="k">Състояние</span><span class="v">{'Нова' if m['state'] == 'new' else 'Употребявана'}</span></div>
      </div>

      <div class="block-label">Обща информация</div>
      <p class="lead-green">{m['desc']}</p>

      <h3 class="feat-h">Кабина и комфорт</h3>
      <ul class="feat-cols">{li(features_cab)}</ul>
      <h3 class="feat-h">Двигател и хидравлика</h3>
      <ul class="feat-cols">{li(features_tech)}</ul>
      <h3 class="feat-h">Други</h3>
      <ul class="feat-cols">{li(features_other)}</ul>

      <div class="inquiry">
        <h3>Запитване за {m['title']}</h3>
        <div class="inquiry-grid">
          <input type="text" placeholder="Име и фамилия">
          <textarea placeholder="Вашето съобщение…"></textarea>
          <input type="email" placeholder="Email адрес">
          <input type="tel" placeholder="Телефонен номер">
        </div>
        <label class="consent"><input type="checkbox"> Съгласен съм да получавам новини и имейл съобщения от NovaMashina.bg на посочения от мен адрес.</label>
        <button class="btn-send" type="button" style="margin-top:20px;padding:14px 38px">Изпрати</button>
      </div>
    </div>

    <aside class="side-sticky">
      <div class="price-box">
        <div class="pb-main">
          <div class="big"><span class="money" data-eur="{m['monthly']}">€{fmt(m['monthly'])}</span> / мес.</div>
          <div class="note">без ДДС, средна вноска за периода</div>
        </div>
        <a class="pb-cta" href="budget-calculator.html">{I['calc-ico']} Изчисли колко можеш да си позволиш <span>›</span></a>
      </div>

      <div class="calc-card" id="prodCalcCard" data-price="{m['price']}" data-state="{m['state']}" data-brand="{m['brand']}" data-model="{m['model']}">
        
        <!-- STEP 1: CALCULATIONS -->
        <div id="pcStep1" class="calc-step active">
          <h3>Калкулирай своя лизинг</h3>
          <div class="cc-sub">Според твоите предпочитания</div>
          <div class="cc-price-label">Стойност на машината</div>
          <div class="cc-price"><span class="money" data-eur="{m['price']}">€{fmt(m['price'])}</span> без ДДС<small>{price_bgn} лв. без ДДС</small></div>
          
          <div class="cc-field">
            <label>Първоначална вноска (ПВ)</label>
            <div class="cc-combo">
              <div class="select-wrap">
                <select id="ccDown">
                  <option value="10">10%</option>
                  <option value="15">15%</option>
                  <option value="20" selected>20%</option>
                  <option value="25">25%</option>
                  <option value="30">30%</option>
                  <option value="35">35%</option>
                  <option value="40">40%</option>
                  <option value="45">45%</option>
                  <option value="50">50%</option>
                </select>
              </div>
              <div class="cc-out" id="ccDownOut">€0</div>
            </div>
          </div>
          
          <div class="cc-field cc-single">
            <label>Срок на лизинга</label>
            <div class="select-wrap">
              <select id="ccTerm">
                <option value="12">12 месеца</option>
                <option value="24">24 месеца</option>
                <option value="36">36 месеца</option>
                <option value="48">48 месеца</option>
                <option value="60" selected>60 месеца</option>
                <option value="72" disabled>72 месеца (неактивен)</option>
                <option value="84" disabled>84 месеца (неактивен)</option>
                <option value="96" disabled>96 месеца (неактивен)</option>
                <option value="108" disabled>108 месеца (неактивен)</option>
                <option value="120" disabled>120 месеца (неактивен)</option>
              </select>
            </div>
          </div>
          
          <div class="cc-field cc-single">
            <label>ДДС схема</label>
            <div class="select-wrap">
              <select id="ccVat">
                <option value="deferred" selected>6.1. Разсрочено ДДС</option>
                <option value="advance">6.2. Авансово ДДС</option>
                <option value="financed">6.3. Финансирано ДДС</option>
              </select>
            </div>
          </div>
          
          <div class="cc-duo">
            <div class="du"><label>Остатъчна стойност (ОС)</label><div class="val" id="ccResidualPctVal" style="font-weight:700">10%</div></div>
            <div class="du" style="text-align:right"><label>ОС Сума</label><div class="val" id="ccResidualOut" style="font-weight:700">€0</div></div>
          </div>
          
          <div class="cc-duo">
            <div class="du"><label>Лихва</label><div class="val" id="ccInterestRateVal">3.5%</div></div>
            <div class="du" style="text-align:right"><label>Такса финансиране</label><div class="val" id="ccFundingFeeVal">€0</div></div>
          </div>
          
          <div class="schedule-section" style="margin-top:12px;padding-top:10px;border-top:1px solid rgba(0,0,0,0.05)">
            <label style="font-weight:700;font-size:13px;color:var(--text);display:block;margin-bottom:6px">7. Погасителни вноски</label>
            <div class="schedule-type-row" style="font-size:13px">
              <label class="radio"><input type="radio" name="ccSchedule" value="monthly" checked onclick="toggleCcMonths(false)"><span class="dot"></span> Ежемесечни</label>
              <label class="radio"><input type="radio" name="ccSchedule" value="seasonal" onclick="toggleCcMonths(true)"><span class="dot"></span> Сезонни</label>
            </div>
            <div class="months-grid" id="ccMonthsGrid" style="grid-template-columns: repeat(4, 1fr); gap: 4px; margin-top: 6px;">
              <!-- JS months grid -->
            </div>
          </div>
          
          <div class="ins-title" style="margin-top:12px">Застраховка (ЗК УНИКА)</div>
          <div class="cc-field cc-single">
            <label>Годишно Каско</label>
            <div class="cc-combo">
              <input type="text" id="ccCascoVal" readonly style="border:1px solid #ddd;border-radius:8px;padding:8px;font-weight:700;background:#f9f9f9;font-size:13px;width:100%" value="€0">
            </div>
          </div>
          <div class="cc-field cc-single" style="margin-top:8px">
            <label>Плащане Каско</label>
            <div class="select-wrap">
              <select id="ccInsPayment">
                <option value="once" selected>Еднократно</option>
                <option value="four">На 4 вноски</option>
              </select>
            </div>
          </div>
          
          <button class="btn-outline btn-offer" type="button" onclick="goToCcStep(2)" style="margin-top:16px">Получи оферта</button>
          <div class="apply-powered">Powered by <b>ЗЛАТЕКС Лизинг</b></div>
        </div>
        
        <!-- STEP 2: CUSTOMER DETAILS -->
        <div id="pcStep2" class="calc-step">
          <h3>Данни за кандидатстване</h3>
          <p style="font-size:13px;color:var(--text-soft);margin-bottom:14px">Изберете тип лице и попълнете формата за оферта.</p>
          
          <div class="client-toggle">
            <button class="client-btn active" id="ccClientPhys" type="button" onclick="setCcClientType('physical')">Физ. лице</button>
            <button class="client-btn" id="ccClientLegal" type="button" onclick="setCcClientType('legal')">Юр. лице</button>
          </div>
          
          <!-- Physical Form -->
          <div id="ccFormPhysical" class="client-form-block">
            <div class="cf-field" style="margin-bottom:8px"><label style="font-size:12px">Три имена</label><input type="text" id="ccPhysName" placeholder="Име и фамилия" style="font-size:13px;padding:8px 10px;width:100%;border:1px solid #ddd;border-radius:6px"></div>
            <div class="cf-field" style="margin-bottom:8px"><label style="font-size:12px">ЕГН</label><input type="text" id="ccPhysEgn" placeholder="ЕГН" style="font-size:13px;padding:8px 10px;width:100%;border:1px solid #ddd;border-radius:6px"></div>
            <div class="cf-field" style="margin-bottom:8px"><label style="font-size:12px">Телефон</label><input type="tel" id="ccPhysPhone" placeholder="Телефон" style="font-size:13px;padding:8px 10px;width:100%;border:1px solid #ddd;border-radius:6px"></div>
            <div class="cf-field" style="margin-bottom:8px"><label style="font-size:12px">Имейл</label><input type="email" id="ccPhysEmail" placeholder="Имейл" style="font-size:13px;padding:8px 10px;width:100%;border:1px solid #ddd;border-radius:6px"></div>
            <div class="cf-field" style="margin-bottom:8px"><label style="font-size:12px">Адрес</label><input type="text" id="ccPhysAddress" placeholder="Пълен адрес" style="font-size:13px;padding:8px 10px;width:100%;border:1px solid #ddd;border-radius:6px"></div>
          </div>
          
          <!-- Legal Form -->
          <div id="ccFormLegal" class="client-form-block" style="display:none">
            <div class="cf-field" style="margin-bottom:8px"><label style="font-size:12px">Име на фирмата</label><input type="text" id="ccLegalName" placeholder="Фирма ЕООД" style="font-size:13px;padding:8px 10px;width:100%;border:1px solid #ddd;border-radius:6px"></div>
            <div class="cf-field" style="margin-bottom:8px"><label style="font-size:12px">ЕИК / Булстат</label><input type="text" id="ccLegalEik" placeholder="ЕИК" style="font-size:13px;padding:8px 10px;width:100%;border:1px solid #ddd;border-radius:6px"></div>
            <div class="cf-field" style="margin-bottom:8px"><label style="font-size:12px">Лице за контакт</label><input type="text" id="ccLegalContact" placeholder="Лице за контакт" style="font-size:13px;padding:8px 10px;width:100%;border:1px solid #ddd;border-radius:6px"></div>
            <div class="cf-field" style="margin-bottom:8px"><label style="font-size:12px">Телефон</label><input type="tel" id="ccLegalPhone" placeholder="Телефон" style="font-size:13px;padding:8px 10px;width:100%;border:1px solid #ddd;border-radius:6px"></div>
            <div class="cf-field" style="margin-bottom:8px"><label style="font-size:12px">Имейл</label><input type="email" id="ccLegalEmail" placeholder="Имейл" style="font-size:13px;padding:8px 10px;width:100%;border:1px solid #ddd;border-radius:6px"></div>
            <div class="cf-field" style="margin-bottom:8px"><label style="font-size:12px">Адрес на регистрация</label><input type="text" id="ccLegalAddress" placeholder="Адрес по регистрация" style="font-size:13px;padding:8px 10px;width:100%;border:1px solid #ddd;border-radius:6px"></div>
          </div>
          
          <div style="display:flex;gap:10px;margin-top:16px">
            <button class="btn-outline" type="button" onclick="goToCcStep(1)" style="flex:1">Назад</button>
            <button class="btn-apply" type="button" onclick="submitCcInquiry()" style="flex:2;margin-top:0">Изпрати</button>
          </div>
        </div>
        
        <!-- STEP 3: SUCCESS STATE -->
        <div id="pcStep3" class="calc-step">
          <div style="text-align:center;padding:24px 10px">
            <div style="width:50px;height:50px;background:var(--green-light);color:var(--green);border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:24px;font-weight:700;margin-bottom:14px">✓</div>
            <h4 style="font-family:var(--font-head);color:var(--green-dark);margin-bottom:8px">Офертата е изпратена!</h4>
            <p style="color:var(--text-soft);font-size:13px;line-height:1.5;margin-bottom:16px">Благодарим Ви! Заявката е приета успешно. Консултант ще се свърже с Вас скоро.</p>
            <button class="btn-outline" type="button" onclick="resetCcForm()" style="width:100%">Назад</button>
          </div>
        </div>
        
      </div>
      <p class="side-note">Изложената информация в NovaMashina.bg е осигурена от ЗЛАТЕКС Лизинг и партньорските дилърски центрове. Калкулацията е индикативна и не представлява обвързваща оферта.</p>
    </aside>
  </div>
</main>'''

# ---------------------------------------------------------------- ТЪРГОВЦИ
DEALERS = [
 ('Агротех България ООД', 'София, Пловдив, Стара Загора', 'medal', 'АГРОТЕХ', 312),
 ('Силоз Агро ЕООД', 'София, Радиново, Варна, Бургас, Русе', 'flag', 'СИЛОЗ АГРО', 287),
 ('Агро Лидер ООД', 'Добрич, Варна', 'flag', 'АГРО ЛИДЕР', 215),
 ('Земеделска Техника ЕООД', 'Пловдив, Пазарджик', 'medal', 'ЗЕМЕДЕЛСКА ТЕХНИКА', 174),
 ('Фермер Машини ЕООД', 'Русе, Велико Търново', 'flag', 'ФЕРМЕР МАШИНИ', 145),
 ('Агрикола Трейд ООД', 'Плевен', 'shield', 'АГРИКОЛА', 120),
 ('БГ Агро Машини ООД', 'Бургас, Сливен, Ямбол', 'flag', 'БГ АГРО', 114),
 ('Комбайн Сервиз ООД', 'Сливен', 'shield', 'КОМБАЙН СЕРВИЗ', 111),
 ('Тракторекс ЕООД', 'Враца, Монтана', 'medal', 'ТРАКТОРЕКС', 101),
 ('Агро Франс 3000 ООД', 'София', 'flag', 'АГРО ФРАНС 3000', 97),
]
dealer_rows = ''.join(f'''
<div class="dealer-row">
  <div class="d-flag">{I[d[2]]}</div>
  <div>
    <h4>{d[0]}</h4>
    <div class="d-loc">{I['pin']}<span>{d[1]}</span></div>
  </div>
  <div class="dealer-logo"><span>{d[3]}</span></div>
  <div class="dealer-cta">
    <div class="d-count">{d[4]} активни оферти</div>
    <a href="catalog.html">Разгледай {I['ext']}</a>
  </div>
</div>''' for d in DEALERS)

dealers_body = f'''
<main class="page container">
  <div class="breadcrumb"><a href="index.html">Nova Mashina</a> / <span>Търговци</span></div>
  <div class="dealer-stats">
    <a class="stat-card" href="#dealers-list">{I['flag']}<h3>Официални представители</h3><div class="sc-count">486 активни оферти</div></a>
    <a class="stat-card" href="#dealers-list">{I['medal']}<h3>Доверени търговци</h3><div class="sc-count">214 активни оферти</div></a>
    <a class="stat-card" href="#dealers-list">{I['shield']}<h3>Проверени търговци</h3><div class="sc-count">158 activeни оферти</div></a>
    <a class="stat-card" href="#dealers-list">{I['person']}<h3>Частни лица</h3><div class="sc-count">92 активни оферти</div></a>
    <a class="stat-card" href="#dealers-list">{I['farm']}<h3>Машини от стопанства</h3><div class="sc-count">57 активни оферти</div></a>
    <a class="stat-card" href="#dealers-list">{I['leaseret']}<h3>Машини върнати от лизинг</h3><div class="sc-count">23 активни оферти</div></a>
  </div>
  <h1 class="page-title" id="dealers-list" style="margin-top:60px">Търговци</h1>
  <div class="dealer-search-row">
    <div class="dealer-search"><input type="text" placeholder="Търсене по име на търговец">{I['search']}</div>
    <div class="sort-links"><a href="#" class="active">По азбучен ред ↑↓</a><a href="#">По брой оферти ↑↓</a></div>
  </div>
  <div class="dealer-list">{dealer_rows}</div>
</main>'''

# ---------------------------------------------------------------- ЛИЗИНГОВ КАЛКУЛАТОР
calculator_body = f'''
<main class="page container">
  <h1 class="page-title">Лизингов калкулатор</h1>
  <p class="page-sub" style="color:#4dbc4d">Избери лизингов план за машина и кандидатствай сега</p>
  
  <div class="calcpage-layout">
    <div class="calculator-container">
      
      <!-- STEP 1: CALCULATIONS -->
      <div id="lcStep1" class="calc-step active">
        <div class="calc-tabs">
          <span class="calc-tab active" id="tabNew" onclick="setLcState('new')">{I['mach-new']} Нова машина</span>
          <span class="calc-tab" id="tabUsed" onclick="setLcState('used')">{I['mach-used']} Употребявана машина</span>
        </div>
        
        <div class="calc-form">
          <div class="cf-grid">
            <div class="cf-field"><label>Марка</label><input type="text" id="lcBrand" placeholder="Напр. John Deere"></div>
            <div class="cf-field"><label>Модел</label><input type="text" id="lcModel" placeholder="Напр. 6R 150"></div>
            <div class="cf-field">
              <label>Цена – EUR без ДДС</label>
              <input type="number" id="lcPrice" value="100000">
              <div class="cf-note" id="lcPriceBgn">Цена в лв: 195 583 лв. без ДДС</div>
            </div>
            
            <div class="cf-field">
              <label>Първоначална вноска (ПВ)</label>
              <div class="cc-combo">
                <div class="select-wrap">
                  <select id="lcDown">
                    <option value="10">10%</option>
                    <option value="15">15%</option>
                    <option value="20" selected>20%</option>
                    <option value="25">25%</option>
                    <option value="30">30%</option>
                    <option value="35">35%</option>
                    <option value="40">40%</option>
                    <option value="45">45%</option>
                    <option value="50">50%</option>
                  </select>
                </div>
                <div class="cc-out" id="lcDownOut">€20 000</div>
              </div>
            </div>
            
            <div class="cf-field">
              <label>Срок на лизинга</label>
              <div class="select-wrap">
                <select id="lcTerm">
                  <option value="12">12 месеца</option>
                  <option value="24">24 месеца</option>
                  <option value="36">36 месеца</option>
                  <option value="48">48 месеца</option>
                  <option value="60" selected>60 месеца</option>
                  <option value="72" disabled>72 месеца (неактивен)</option>
                  <option value="84" disabled>84 месеца (неактивен)</option>
                  <option value="96" disabled>96 месеца (неактивен)</option>
                  <option value="108" disabled>108 месеца (неактивен)</option>
                  <option value="120" disabled>120 месеца (неактивен)</option>
                </select>
              </div>
            </div>
            
            <div class="cf-field">
              <label>ДДС схема</label>
              <div class="select-wrap">
                <select id="lcVat">
                  <option value="deferred" selected>6.1. Разсрочено ДДС</option>
                  <option value="advance">6.2. Авансово ДДС</option>
                  <option value="financed">6.3. Финансирано ДДС</option>
                </select>
              </div>
            </div>
            
            <div class="cf-field">
              <label>Остатъчна стойност (ОС)</label>
              <div class="cc-combo">
                <input type="text" id="lcResidualPct" readonly style="width:70px;text-align:center;border:1px solid #ddd;border-radius:8px;padding:8px;font-weight:700" value="10%">
                <div class="cc-out" id="lcResidualOut">€10 000</div>
              </div>
            </div>
            
            <div class="cf-field">
              <label>Лихвен процент</label>
              <input type="text" id="lcInterestRate" readonly style="border:1px solid #ddd;border-radius:8px;padding:12px;font-weight:700;background:#f9f9f9" value="3.5%">
            </div>
          </div>
          
          <div class="schedule-section" style="border-top:1px solid #eee;margin-top:20px;padding-top:16px">
            <label style="font-weight:700;font-size:14px;color:var(--text)">9. Погасителни вноски</label>
            <div class="schedule-type-row">
              <label class="radio"><input type="radio" name="lcSchedule" value="monthly" checked onclick="toggleLcMonths(false)"><span class="dot"></span> 9.1. Ежемесечни</label>
              <label class="radio"><input type="radio" name="lcSchedule" value="seasonal" onclick="toggleLcMonths(true)"><span class="dot"></span> 9.2. Сезонни (мин. 3 месеца)</label>
            </div>
            
            <div class="months-grid" id="lcMonthsGrid">
              <!-- JS will render months here as clickable tags -->
            </div>
          </div>
          
          <div class="insurance-section" style="border-top:1px solid #eee;margin-top:20px;padding-top:16px">
            <label style="font-weight:700;font-size:14px;color:var(--text);margin-bottom:8px;display:block">11. Застраховка (ЗК УНИКА)</label>
            <div class="cf-grid">
              <div class="cf-field">
                <label>Плащане Каско</label>
                <div class="select-wrap">
                  <select id="lcInsPayment">
                    <option value="once" selected>Еднократно</option>
                    <option value="four">На 4 вноски</option>
                  </select>
                </div>
              </div>
              <div class="cf-field">
                <label>Годишно Каско</label>
                <input type="text" id="lcCascoVal" readonly style="border:1px solid #ddd;border-radius:8px;padding:12px;font-weight:700;background:#f9f9f9" value="€0">
              </div>
            </div>
          </div>
          
          <div class="fee-section" style="border-top:1px solid #eee;margin-top:20px;padding-top:16px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px">
            <div>
              <label style="font-weight:700;font-size:13px;color:var(--text-soft)">12. Такса финансиране (1% от ФС)</label>
              <div id="lcFundingFeeVal" style="font-size:16px;font-weight:800;color:var(--text)">€800</div>
            </div>
            <div style="text-align:right">
              <label style="font-weight:700;font-size:15px;color:var(--green-dark)">10. Вноска (без ДДС)</label>
              <div style="font-size:26px;font-weight:800;color:var(--green)" id="lcFinalMonthly">€0</div>
            </div>
          </div>
          
          <button class="btn-continue" type="button" onclick="goToLcStep(2)" style="margin-top:24px">Продължи</button>
          <div class="powered-mini">Powered by <b>ЗЛАТЕКС Лизинг</b></div>
        </div>
      </div>
      
      <!-- STEP 2: CUSTOMER DETAILS -->
      <div id="lcStep2" class="calc-step">
        <div class="calc-form">
          <h3 style="margin-bottom:16px;font-family:var(--font-head);color:var(--green-dark)">Данни за кандидатстване</h3>
          <p style="font-size:14px;color:var(--text-soft);margin-bottom:20px">Моля изберете тип лице и попълнете формата.</p>
          
          <div class="client-toggle">
            <button class="client-btn active" id="lcClientPhys" type="button" onclick="setLcClientType('physical')">Физическо лице</button>
            <button class="client-btn" id="lcClientLegal" type="button" onclick="setLcClientType('legal')">Юридическо лице</button>
          </div>
          
          <!-- Physical Person Form -->
          <div id="lcFormPhysical" class="client-form-block">
            <div class="cf-grid">
              <div class="cf-field" style="grid-column: span 2"><label>Три имена</label><input type="text" id="lcPhysName" placeholder="Име, Презиме, Фамилия"></div>
              <div class="cf-field"><label>ЕГН</label><input type="text" id="lcPhysEgn" placeholder="ЕГН"></div>
              <div class="cf-field"><label>Телефон</label><input type="tel" id="lcPhysPhone" placeholder="Телефон"></div>
              <div class="cf-field" style="grid-column: span 2"><label>Имейл</label><input type="email" id="lcPhysEmail" placeholder="Имейл"></div>
              <div class="cf-field" style="grid-column: span 2"><label>Адрес</label><input type="text" id="lcPhysAddress" placeholder="Пълен адрес"></div>
            </div>
          </div>
          
          <!-- Legal Entity Form -->
          <div id="lcFormLegal" class="client-form-block" style="display:none">
            <div class="cf-grid">
              <div class="cf-field" style="grid-column: span 2"><label>Име на фирмата</label><input type="text" id="lcLegalName" placeholder="Фирма ООД/ЕООД"></div>
              <div class="cf-field"><label>ЕИК / Булстат</label><input type="text" id="lcLegalEik" placeholder="ЕИК"></div>
              <div class="cf-field"><label>Лице за контакт</label><input type="text" id="lcLegalContact" placeholder="Име на представител"></div>
              <div class="cf-field"><label>Телефон</label><input type="tel" id="lcLegalPhone" placeholder="Телефон"></div>
              <div class="cf-field"><label>Имейл</label><input type="email" id="lcLegalEmail" placeholder="Имейл"></div>
              <div class="cf-field" style="grid-column: span 2"><label>Адрес на регистрация</label><input type="text" id="lcLegalAddress" placeholder="Адрес по регистрация"></div>
            </div>
          </div>
          
          <div style="display:flex;gap:14px;margin-top:24px">
            <button class="btn-outline" type="button" onclick="goToLcStep(1)" style="flex:1">Назад</button>
            <button class="btn-continue" type="button" onclick="submitLcInquiry()" style="flex:2;margin-top:0">Изпрати запитване</button>
          </div>
        </div>
      </div>
      
      <!-- STEP 3: SUCCESS STATE -->
      <div id="lcStep3" class="calc-step">
        <div class="calc-form" style="text-align:center;padding:40px 30px">
          <div style="width:70px;height:70px;background:var(--green-light);color:var(--green);border-radius:50%;display:inline-flex;align-items:center;justify-content:center;font-size:36px;font-weight:700;margin-bottom:20px">✓</div>
          <h3 style="font-family:var(--font-head);color:var(--green-dark);margin-bottom:12px">Заявката е изпратена успешно!</h3>
          <p style="color:var(--text-soft);font-size:15px;line-height:1.6;margin-bottom:24px">Благодарим Ви! Вашата оферта е регистрирана. Наш консултант от ЗЛАТЕКС Лизинг ще се свърже с Вас в най-кратък срок.</p>
          <button class="btn-continue" type="button" onclick="resetLcForm()" style="margin-top:0">Ново изчисление</button>
        </div>
      </div>
      
    </div>
    
    <aside class="calc-side">
      <h3>Желаната нова машина е само на няколко клика разстояние</h3>
      <div class="how">Как да кандидатствам за лизинг бързо и лесно?</div>
      <div class="check-item">{I['checkc']}<span>Въведи ОБЩА СТОЙНОСТ на лизинга и нашата система ще пресметне всички останали параметри.</span></div>
      <div class="check-item">{I['checkc']}<span>Управлявай Първоначална вноска, Срок на лизинга и Остатъчна стойност до получаване на желаната Месечна вноска.</span></div>
      <div class="check-item">{I['checkc']}<span>Кандидатствай онлайн и очаквай обаждане от наш консултант с предварително одобрение.</span></div>
      <div class="check-item">{I['checkc']}<span>Избери машината си спокойно — одобрението важи за всяка оферта в платформата.</span></div>
    </aside>
  </div>
</main>'''

# ---------------------------------------------------------------- БЮДЖЕТЕН КАЛКУЛАТОР
budget_body = f'''
<main class="page container">
  <div class="budget-hero">
    <h1 class="page-title">Предварително одобрение за лизинг спрямо твоя бюджет</h1>
    <p class="page-sub">Намери идеалния баланс и подкарай новата си машина с усмивка</p>
    <img class="budget-art" src="img/budget-hero.jpg" alt="">
    <p class="budget-lead">Покупката на земеделска машина е важен момент, който бележи нов етап в твоето стопанство. Но за да е празник, инвестицията трябва да е съобразена с възможностите на фермата. Бюджетният калкулатор на NovaMashina.bg ти помага да прецениш точно каква месечна вноска можеш да си позволиш — без излишен риск и без изненади.</p>
  </div>
  <div class="budget-row">
    <img src="img/budget-side.jpg" alt="">
    <div>
      <div class="budget-item">{I['cal'].replace('#6c6c6c', '#4dbc4d')}<div><h4>Текущи месечни вноски</h4><p>Тук влизат твоите активни кредити, ипотеки или други лизинги, които изплащаш в момента.</p></div></div>
      <div class="budget-item">{I['compare']}<div><h4>Кредитни карти и лимити</h4><p>Дори да не ги ползваш изцяло, лимитите по кредитни карти и овърдрафти са част от твоя финансов профил и ние ги отчитаме за максимална точност.</p></div></div>
      <div class="budget-item">{I['mach-new']}<div><h4>Твоята нова вноска</h4><p>Прогнозната месечна сума за машината, която си избрал. Можеш да експериментираш с различни срокове, докато откриеш сумата, която ти пасва идеално.</p></div></div>
      <div class="budget-item">{I['power'].replace('#6c6c6c', '#4dbc4d')}<div><h4>Общи месечни разходи</h4><p>Сборът от всички тези елементи ти дава ясна представа за твоите ангажименти, за да знаеш точно с какъв ресурс разполагаш за всичко останало.</p></div></div>
    </div>
  </div>
  <div class="budget-form">
    <h3>Изчисли своя бюджет</h3>
    <div class="bf-grid">
      <div class="cf-field"><label>Месечен доход на стопанството (€)</label><input type="number" id="bfIncome" value="8000"></div>
      <div class="cf-field"><label>Текущи месечни вноски (€)</label><input type="number" id="bfLoans" value="1200"></div>
      <div class="cf-field"><label>Лимити по кредитни карти (€)</label><input type="number" id="bfCards" value="5000"></div>
    </div>
    <div class="bf-result">Можеш да си позволиш месечна вноска до:<span class="big" id="bfResult">€2 550</span></div>
    <button class="btn-continue" type="button">Кандидатствай за предварително одобрение</button>
    <div class="powered-mini">Powered by <b>ЗЛАТЕКС Лизинг</b></div>
  </div>
</main>'''

# ---------------------------------------------------------------- НОВИНИ
NEWS = [
 ('Петъчна топ оферта: Вземи John Deere 6R 150 с 3,33% лихва и подаръци!', 'Промоционални условия от NovaMashina.bg до 30.6.2026 г.', '05/06/2026', 'news-1.jpg'),
 ('Жътвата идва с CLAAS: Ексклузивни оферти и подаръци с NovaMashina.bg', 'Твоето лято на пълни обороти — с комбайн от ново поколение.', '01/06/2026', 'news-2.jpg'),
 ('Немско инженерство на нова цена: Вземи своя нов Fendt с вноска от 950 €!', 'Специални условия: лихва 3,65% и атрактивни вноски до 30.06.2026 г', '29/05/2026', 'news-3.jpg'),
 ('Пазарът на агротехника през април 2026 г.', 'Агро прелом 2026: Ренесанс на прецизното земеделие и нови марки в България.', '26/05/2026', 'news-4.jpg'),
 ('Полски правила: Какво (наистина) трябва да знаем преди сеитба?', 'Пет златни правила за пролетната кампания.', '18/05/2026', 'news-5.jpg'),
 ('Подготви машината за зимата: пълен чеклист от сервизните ни партньори', 'Съхранение, консервация и профилактика на техниката.', '12/05/2026', 'news-6.jpg'),
]
news_cards = ''.join(f'''
<a class="news-card" href="#">
  <img src="img/{n[3]}" alt="">
  <div class="nc-body">
    <h3>{n[0]}</h3>
    <p>{n[1]}</p>
    <span class="nc-date">{n[2]}</span>
  </div>
</a>''' for n in NEWS)

news_body = f'''
<main class="page container">
  <h1 class="page-title">Новини от Нова Машина</h1>
  <p class="page-sub">Актуална и полезна информация за всеки, който планира покупка на земеделска техника</p>
  <div class="news-grid">{news_cards}</div>
  <div class="cta-center"><a class="btn-cta" href="#">Зареди още новини</a></div>
</main>'''

# ---------------------------------------------------------------- ЗА НАС
about_body = f'''
<main class="page container">
  <div class="about-hero">
    <div>
      <h1>Нова Машина е платформа на ЗЛАТЕКС, която прави избора и закупуването на земетелска техника лесно, бързо и удобно</h1>
      <p>Предлагаме ви лесен и удобен дигитален асистент в избора на Вашата Нова Машина. В тази динамично променяща се среда, където дистанционните услуги вече са ежедневие, ние ви даваме възможността да изберете, тествате и купите на лизинг своята мечтана нова машина изцяло дистанционно.</p>
    </div>
    <img src="img/about-1.jpg" alt="">
  </div>
  <div class="about-row">
    <img src="img/about-2.jpg" alt="">
    <div>
      <h2>Желаната Нова Машина е само на няколко клика разстояние</h2>
      <p>Платформата е интуитивна и лесна за използване, като с няколко клика задавате критериите си за мечтаната машина и веднага получавате списък с най-подходящите оферти, от които можете да избирате, както и да заявите демонстрация в стопанството. По този начин ви даваме възможност да изберете своята Нова Машина и да я вземете при най-добрите условия за лизинг.</p>
      <a class="btn-cta" href="catalog.html">Нова техника на лизинг</a>
    </div>
  </div>
  <div class="about-row">
    <div>
      <h2>Финансиране, застраховка и регистрация — на едно място</h2>
      <p>Чрез ЗЛАТЕКС Лизинг получавате пълно съдействие: индивидуален лизингов план, застраховка на техниката, регистрация и доставка до стопанството. Нашите консултанти са до вас на всяка стъпка — от избора до първата бразда.</p>
      <a class="btn-cta dark" href="calculator.html">Лизингов калкулатор</a>
    </div>
    <img src="img/budget-side.jpg" alt="">
  </div>
</main>'''

# ---------------------------------------------------------------- КОНТАКТИ
contacts_body = f'''
<div class="contacts-wrap">
  <div class="map-bg"><img src="img/map.svg" alt="Карта"></div>
  <div class="contact-card">
    <h1>Свържете се с нас</h1>
    <div class="contact-grid">
      <input type="text" placeholder="Име и фамилия">
      <textarea placeholder="Вашето съобщение…"></textarea>
      <input type="email" placeholder="Email адрес">
      <input type="tel" placeholder="Телефонен номер">
    </div>
    <label class="consent"><input type="checkbox"> Съгласен съм да получавам новини и имейл съобщения от NovaMashina.bg на посочения от мен адрес.</label>
    <label class="consent"><input type="checkbox"> Съгласен съм да получавам маркетингова информация и промоционални предложения от NovaMashina.bg и нашите партньори.</label>
    <button class="btn-send" type="button" style="margin-top:22px;padding:14px 38px">Изпрати</button>
    <div class="contact-info-row">
      <div class="ci">{I['pin-g']}<span>Централа на ЗЛАТЕКС ООД<br>гр. Стара Загора, 6000, бул. Никола Петков 55</span></div>
      <div class="ci">{I['phone']}<span>+359 88 510 4040<br>+359 42 600 046</span></div>
      <div class="ci">{I['mail']}<span>contact@novamashina.bg</span></div>
    </div>
  </div>
</div>'''

# ---------------------------------------------------------------- FAQ
FAQS = [
 ('Какво е оперативен лизинг?', 'Оперативният лизинг е форма на дългосрочен наем, при която използвате машината срещу фиксирана месечна вноска, без да я придобивате в собственост. В края на договора връщате техниката или я подменяте с нова. Подходящ е само за юридически лица и често включва обслужване и застраховка в месечната вноска.'),
 ('Какво е финансов лизинг?', 'Финансовият лизинг е финансиране, при което след заплащане на всички вноски и остатъчната стойност машината става ваша собственост. Подходящ е както за земеделски производители, така и за агрофирми, а ДДС може да бъде разсрочено или платено еднократно.'),
 ('Какво е първоначална вноска?', 'Първоначалната вноска е процент от цената на машината, който заплащате при сключване на договора. В NovaMashina.bg тя обикновено е между 15% и 45% — колкото по-висока е, толкова по-ниска е месечната ви вноска.'),
 ('Какво е остатъчна стойност?', 'Остатъчната стойност е сума, чието плащане се отлага за края на лизинговия период. Тя намалява месечните вноски, а в края на договора можете да я платите и да придобиете машината, да я рефинансирате или да върнете техниката.'),
 ('Как да кандидатствам за лизинг?', 'Изберете машина от платформата или използвайте лизинговия калкулатор, настройте параметрите по ваше желание и натиснете „Кандидатствай сега“. Наш консултант от ЗЛАТЕКС Лизинг ще се свърже с вас за предварително одобрение — обикновено в рамките на един работен ден.'),
 ('Мога ли да взема употребявана техника на лизинг?', 'Да. Всички употребявани машини в платформата са проверени и обслужени от официални представители и доверени търговци. Лизинговите условия се изчисляват според годината на производство и моточасовете на машината.'),
 ('Какви документи са ми необходими?', 'За земеделски производители: регистрация по Наредба 3, последна данъчна декларация и анкетна карта. За фирми: финансови отчети за последните две години. Нашият екип ще ви съдейства с пълния списък според конкретния случай.'),
]
faq_items = ''.join(f'''
<div class="faq-item">
  <button class="faq-q" onclick="this.parentElement.classList.toggle('open')">{q}<span class="chev"></span></button>
  <div class="faq-a"><div class="faq-a-inner">{a}</div></div>
</div>''' for q, a in FAQS)

faq_body = f'''
<main class="page">
  <h1 class="page-title">Често задавани въпроси</h1>
  <div class="faq-list">{faq_items}</div>
</main>'''

# ---------------------------------------------------------------- ЗАПИС
pages = {
 'index.html': ('Нова Машина – Сайт No.1 за лизинг на селскостопанска техника', index_body, 'home'),
 'catalog.html': ('Оферти за нова и употребявана техника на лизинг', catalog_body, 'catalog'),
 'dealers.html': ('Търговци – Нова Машина', dealers_body, 'dealers'),
 'calculator.html': ('Лизингов калкулатор – Нова Машина', calculator_body, 'calc'),
 'budget-calculator.html': ('Бюджетен калкулатор за лизинг – Нова Машина', budget_body, 'budget'),
 'news.html': ('Новини – Ексклузивни оферти за лизинг на техника', news_body, 'news'),
 'about.html': ('За Нова Машина', about_body, 'about'),
 'contacts.html': ('Контакти – Нова Машина', contacts_body, 'contacts'),
 'faq.html': ('Често задавани въпроси – Нова Машина', faq_body, 'about'),
}
for m in MACHINES:
    state = 'Нов' if m['state'] == 'new' else 'Употребяван'
    pages[f'product-{m["id"]}.html'] = (f'{state} {m["title"]}, {m["fuel"]} | {m["offer"]}', product_page(m), 'catalog')

for fname, (title, body, active) in pages.items():
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(page(title, body, active))

print('Generated', len(pages), 'pages')
