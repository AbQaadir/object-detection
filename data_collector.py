import os
import cv2
import time
import uuid

# Define the path to the directory where the images will be saved
IMAGES_PATH = 'CollectedImages'
labels = [
    'hello', 'thanks', 'yes', 'no', 'iloveyou', 'goodbye', 'please'
]

num_images = 15

for label in labels:
    # Create a directory for each label
    os.makedirs(os.path.join(IMAGES_PATH, label), exist_ok=True)
    print(f'Collecting images for {label}...')
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print(f"Error: Unable to open camera for label {label}")
        continue
    
    time.sleep(5)

    for img_num in range(num_images):
        print(f'Collecting image {img_num}')
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Failed to capture image")
            continue
        
        imgname = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
