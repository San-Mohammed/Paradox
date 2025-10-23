# src/face_detection.py
import cv2
import face_recognition
import numpy as np
import os

def detect_faces_realtime():
    """Detect faces in real-time using macOS camera"""
    
    # Initialize camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("❌ Error: Could not open camera")
        return
    
    print("🎥 Camera opened successfully!")
    print("📱 Press 'q' to quit, 's' to save current frame")
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("❌ Error: Could not read frame")
            break
        
        # Resize frame for better performance (optional)
        frame = cv2.resize(frame, (640, 480))
        
        # Convert BGR to RGB (face_recognition uses RGB)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Find face locations
        face_locations = face_recognition.face_locations(rgb_frame)
        
        # Draw rectangles around faces
        for (top, right, bottom, left) in face_locations:
            # Draw rectangle
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            
            # Add text
            cv2.putText(frame, f"Face {len(face_locations)}", (left, top - 10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Add info text
        cv2.putText(frame, f"Faces detected: {len(face_locations)}", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Display the frame
        cv2.imshow('UKH Face Detection - Real-time', frame)
        
        # Handle key presses - Fix the key detection
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:  # 'q' or ESC key
            print("👋 Quitting...")
            break
        elif key == ord('s'):
            # Save current frame
            if not os.path.exists("test_images"):
                os.makedirs("test_images")
            filename = f"test_images/captured_frame_{len(face_locations)}_faces.jpg"
            cv2.imwrite(filename, frame)
            print(f"📸 Frame saved as {filename}")
    
    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    print("✅ Camera released and windows closed")

if __name__ == "__main__":
    detect_faces_realtime()