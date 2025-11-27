import os

# --- CONFIGURATION ---

# 1. ROOT PATH OF YOUR YOLOv5 DATA STRUCTURE
YOLO_DATA_ROOT = "/Users/SRJ/Desktop/Consciousness-detection-/yolov5_data"

# 2. CLASS MAPPING
# Ensure these class names match the names in your filenames (e.g., 'DROWSY', 'NATURAL')
CLASS_MAP = {
    'NATURAL': 0,  # Assuming 'NATURAL' means 'awake'
    'DROWSY': 1   # Assuming 'DROWSY' means 'drowsy'
}

# 3. FULL-FRAME BOUNDING BOX COORDINATES
# Since the image is already cropped to the object, the box covers the entire image (0.5, 0.5, 1.0, 1.0)
FULL_FRAME_BOX = "0.5 0.5 1.0 1.0" 

# --- EXECUTION ---

print(f"Starting automatic label generation in: {YOLO_DATA_ROOT}\n")

# Process both 'train' and 'val' splits
for split in ['train', 'val']:
    
    # Define image and label directories for the current split
    image_dir = os.path.join(YOLO_DATA_ROOT, 'images', split)
    label_dir = os.path.join(YOLO_DATA_ROOT, 'labels', split)
    
    # Check if the directories exist
    if not os.path.exists(image_dir):
        print(f"Skipping {split}: Image directory not found at {image_dir}")
        continue
        
    print(f"Processing {split} set in {image_dir}...")
    
    label_count = 0
    
    # Iterate through all files in the image directory
    for filename in os.listdir(image_dir):
        # We only care about image files
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            
            # --- 1. DETERMINE CLASS ID FROM FILENAME ---
            class_id = -1
            class_name = None
            
            # Find the class name (key) in the filename
            for name, ID in CLASS_MAP.items():
                if name.upper() in filename.upper():
                    class_id = ID
                    class_name = name
                    break
            
            if class_id == -1:
                print(f"Warning: Could not determine class for file: {filename}. Skipping.")
                continue

            # --- 2. GENERATE LABEL FILE PATH ---
            # Remove the extension (.jpg, .png) and replace it with .txt
            base_name = os.path.splitext(filename)[0]
            label_filename = base_name + '.txt'
            label_path = os.path.join(label_dir, label_filename)
            
            # --- 3. WRITE YOLO LABEL CONTENT ---
            # Content is: class_id x_center y_center width height
            yolo_content = f"{class_id} {FULL_FRAME_BOX}"
            
            with open(label_path, 'w') as f:
                f.write(yolo_content)
                
            label_count += 1
            
    print(f"-> Successfully created {label_count} label files for the {split} set in {label_dir}")

print("\n✅ Automated label generation complete!")
print("Your data is now ready for training.")