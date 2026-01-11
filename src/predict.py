from ultralytics import YOLO
import os

# 1. Load model
model = YOLO('best.pt') 

# 2. Ambil satu gambar dari dataset buat ngetes
# Kita ambil gambar pertama di folder images
img_path = 'dataset/images/train_img_0.jpg'

if os.path.exists(img_path):
    results = model.predict(source=img_path, save=True, conf=0.3)
    print(f"✅ Berhasil! Hasil deteksi ada di folder: runs/detect/predict")
else:
    print("❌ Gambar gak ketemu bro, coba cek nama filenya di folder dataset/images")
