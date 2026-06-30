# -*- coding: utf-8 -*-
import os
from PIL import Image

def optimize():
    img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
    if not os.path.exists(img_dir):
        print("Image directory not found.")
        return

    print("Starting image optimization...")
    files = os.listdir(img_dir)
    total_saved = 0

    for filename in files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(img_dir, filename)
            
            # Don't delete or overwrite logo.png/logo.webp if we want to keep a version,
            # but we can convert it to logo.webp!
            name, ext = os.path.splitext(filename)
            new_filename = f"{name}.webp"
            new_file_path = os.path.join(img_dir, new_filename)

            try:
                orig_size = os.path.getsize(file_path)
                with Image.open(file_path) as img:
                    # Convert to RGB if it is RGBA and we are saving to JPEG/WEBP
                    if img.mode in ('RGBA', 'LA') and ext.lower() in ('.jpg', '.jpeg'):
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        background.paste(img, mask=img.split()[3])
                        img = background
                    
                    img.save(new_file_path, 'WEBP', quality=80)
                
                new_size = os.path.getsize(new_file_path)
                saved = orig_size - new_size
                total_saved += saved
                print(f"Optimized: {filename} ({orig_size/1024:.1f} KB) -> {new_filename} ({new_size/1024:.1f} KB) | Saved: {saved/1024:.1f} KB ({saved/orig_size*100:.1f}%)")
                
                # Delete the original file
                os.remove(file_path)
            except Exception as e:
                print(f"Error optimizing {filename}: {e}")

    print(f"Optimization completed. Total storage saved: {total_saved/1024/1024:.2f} MB")

if __name__ == '__main__':
    optimize()
