from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.pt')

    model.train(
        data='data.yaml',      
        epochs=50,             
        imgsz=360,             
        batch=16,              
        device='mps',          
        name='cctv_training',  
        project='runs/detect'  
    )

    print("Training Selesai! Cek folder runs/detect/cctv_training/weights/best.pt")

if __name__ == '__main__':
    main()