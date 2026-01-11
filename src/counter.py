from ultralytics import YOLO

model = YOLO('best.pt')
results = model.predict(source='dataset/images', conf=0.4)

for r in results:
    counts = r.boxes.cls.unique()
    print(f"File: {r.path}")
    for c in r.boxes.cls:
        print(f" - Terdeteksi: {model.names[int(c)]}")
    print(f"Total Objek: {len(r.boxes)}\n")
