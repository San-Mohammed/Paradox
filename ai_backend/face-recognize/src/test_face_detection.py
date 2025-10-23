# src/test_face_detection.py
import cv2
import face_recognition
import os

def test_with_sample_images():
    """Test face detection with sample images"""
    
    # Check if test_images directory exists
    if not os.path.exists("test_images"):
        os.makedirs("test_images")
        print("📁 Created test_images directory")
    
    # List of sample images to test
    sample_images = [
        "test_images/your_face.jpeg",  # You can add your own image here
        # Add more test images as needed
    ]
    
    for image_path in sample_images:
        if os.path.exists(image_path):
            print(f"🔍 Testing image: {image_path}")
            
            # Load image
            image = cv2.imread(image_path)
            if image is None:
                print(f"❌ Could not load image: {image_path}")
                continue
            
            # Convert BGR to RGB
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Find face locations
            face_locations = face_recognition.face_locations(rgb_image)
            
            print(f"✅ Found {len(face_locations)} face(s) in {image_path}")
            
            # Draw rectangles around faces
            for (top, right, bottom, left) in face_locations:
                cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
            
            # Save result
            output_path = f"test_images/result_{os.path.basename(image_path)}"
            cv2.imwrite(output_path, image)
            print(f"💾 Result saved as: {output_path}")
        else:
            print(f"⚠️ Image not found: {image_path}")

if __name__ == "__main__":
    test_with_sample_images()