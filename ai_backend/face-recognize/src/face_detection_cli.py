# src/face_recognition_cli.py
import cv2
import face_recognition
import numpy as np
import os
import pickle
from datetime import datetime

class FaceRecognitionCLI:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.face_database = {}
        
    def add_face_to_database(self, image_path, person_name):
        """Add a face to the recognition database"""
        try:
            # Load image
            image = cv2.imread(image_path)
            if image is None:
                print(f"❌ Could not load image: {image_path}")
                return False
            
            # Convert BGR to RGB
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Find face locations
            face_locations = face_recognition.face_locations(rgb_image)
            
            if len(face_locations) == 0:
                print(f"❌ No face found in {image_path}")
                return False
            
            if len(face_locations) > 1:
                print(f"⚠️ Multiple faces found in {image_path}, using the first one")
            
            # Get face encoding
            face_encoding = face_recognition.face_encodings(rgb_image, face_locations)[0]
            
            # Add to database
            self.known_face_encodings.append(face_encoding)
            self.known_face_names.append(person_name)
            
            print(f"✅ Added {person_name} to face database")
            return True
            
        except Exception as e:
            print(f"❌ Error adding face: {str(e)}")
            return False
    
    def recognize_faces_realtime(self):
        """Recognize faces in real-time"""
        
        if len(self.known_face_encodings) == 0:
            print("❌ No faces in database. Please add faces first.")
            return
        
        # Initialize camera
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Error: Could not open camera")
            return
        
        print("🎥 Camera opened successfully!")
        print("📱 Press 'q' to quit, 's' to save current frame")
        print(f"👥 Known faces: {', '.join(self.known_face_names)}")
        
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            
            if not ret:
                print("❌ Error: Could not read frame")
                break
            
            # Resize frame for better performance
            frame = cv2.resize(frame, (640, 480))
            
            # Convert BGR to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Find face locations and encodings
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            
            # Recognize faces
            for face_encoding, face_location in zip(face_encodings, face_locations):
                # Compare with known faces
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                
                # Get the best match
                best_match_index = np.argmin(face_distances)
                
                if matches[best_match_index]:
                    confidence = 1 - face_distances[best_match_index]
                    name = self.known_face_names[best_match_index]
                    
                    # Draw rectangle and label
                    top, right, bottom, left = face_location
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(frame, f"{name} ({confidence:.2f})", (left, top - 10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                else:
                    # Unknown face
                    top, right, bottom, left = face_location
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(frame, "Unknown", (left, top - 10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            
            # Add info text
            cv2.putText(frame, f"Faces detected: {len(face_locations)}", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            
            # Display the frame
            cv2.imshow('UKH Face Recognition - Real-time', frame)
            
            # Handle key presses
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:  # 'q' or ESC key
                print("👋 Quitting...")
                break
            elif key == ord('s'):
                # Save current frame
                if not os.path.exists("test_images"):
                    os.makedirs("test_images")
                filename = f"test_images/recognition_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                cv2.imwrite(filename, frame)
                print(f"📸 Frame saved as {filename}")
        
        # Cleanup
        cap.release()
        cv2.destroyAllWindows()
        print("✅ Camera released and windows closed")
    
    def test_recognition_with_image(self, image_path):
        """Test face recognition with a single image"""
        
        if len(self.known_face_encodings) == 0:
            print("❌ No faces in database. Please add faces first.")
            return
        
        try:
            # Load image
            image = cv2.imread(image_path)
            if image is None:
                print(f"❌ Could not load image: {image_path}")
                return
            
            # Convert BGR to RGB
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Find face locations and encodings
            face_locations = face_recognition.face_locations(rgb_image)
            face_encodings = face_recognition.face_encodings(rgb_image, face_locations)
            
            print(f"🔍 Found {len(face_locations)} face(s) in {image_path}")
            
            # Recognize faces
            for i, (face_encoding, face_location) in enumerate(zip(face_encodings, face_locations)):
                # Compare with known faces
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                
                # Get the best match
                best_match_index = np.argmin(face_distances)
                
                if matches[best_match_index]:
                    confidence = 1 - face_distances[best_match_index]
                    name = self.known_face_names[best_match_index]
                    print(f"✅ Face {i+1}: {name} (confidence: {confidence:.2f})")
                    
                    # Draw rectangle and label
                    top, right, bottom, left = face_location
                    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(image, f"{name} ({confidence:.2f})", (left, top - 10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                else:
                    print(f"❓ Face {i+1}: Unknown")
                    
                    # Draw rectangle and label
                    top, right, bottom, left = face_location
                    cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(image, "Unknown", (left, top - 10), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            
            # Save result
            output_path = f"test_images/recognition_result_{os.path.basename(image_path)}"
            cv2.imwrite(output_path, image)
            print(f"💾 Result saved as: {output_path}")
            
        except Exception as e:
            print(f"❌ Error processing image: {str(e)}")

def main():
    """Main function for CLI interface"""
    recognizer = FaceRecognitionCLI()
    
    print("🎯 UKH Face Recognition CLI")
    print("=" * 40)
    
    while True:
        print("\n📋 Options:")
        print("1. Add face to database")
        print("2. Start real-time recognition")
        print("3. Test recognition with image")
        print("4. Show database status")
        print("5. Exit")
        
        choice = input("\n🔢 Enter your choice (1-5): ").strip()
        
        if choice == "1":
            image_path = input("📁 Enter image path: ").strip()
            person_name = input("👤 Enter person name: ").strip()
            recognizer.add_face_to_database(image_path, person_name)
            
        elif choice == "2":
            recognizer.recognize_faces_realtime()
            
        elif choice == "3":
            image_path = input("📁 Enter image path: ").strip()
            recognizer.test_recognition_with_image(image_path)
            
        elif choice == "4":
            print(f"👥 Database contains {len(recognizer.known_face_names)} faces:")
            for i, name in enumerate(recognizer.known_face_names, 1):
                print(f"  {i}. {name}")
                
        elif choice == "5":
            print("👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()