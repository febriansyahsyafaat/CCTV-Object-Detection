import json
import os

json_file = 'hasil.json'
output_dir = 'dataset/labels'
os.makedirs(output_dir, exist_ok=True)

class_map = {"car": 0, "bus": 1, "truck": 2}

with open(json_file, 'r') as f:
    data = json.load(f)

print(f"Memproses {len(data)} data...")

for item in data:
    if 'file_upload' in item:
        
        raw_name = item['file_upload'].split('-')[-1]
        txt_name = os.path.splitext(raw_name)[0] + ".txt"
        
        with open(os.path.join(output_dir, txt_name), 'w') as f_out:
            if 'annotations' in item and item['annotations']:
                for ann in item['annotations'][0].get('result', []):
                    if ann['type'] == 'rectanglelabels':
                        val = ann['value']
                        label_name = val['rectanglelabels'][0]
                        class_id = class_map.get(label_name, 0)
                        
                        x_center = (val['x'] + val['width'] / 2) / 100
                        y_center = (val['y'] + val['height'] / 2) / 100
                        w = val['width'] / 100
                        h = val['height'] / 100
                        
                        f_out.write(f"{class_id} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}\n")

print("✅ BERHASIL! File .txt sekarang sudah ada isinya.")
