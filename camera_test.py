import cv2

def test_cameras():
    # Test cameras from index 0 to 2
    for i in range(3):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"Camera index {i} is available")
            ret, frame = cap.read()
            if ret:
                print(f"Successfully read frame from camera {i}")
            else:
                print(f"Could not read frame from camera {i}")
            cap.release()
        else:
            print(f"Camera index {i} is not available")

if __name__ == "__main__":
    test_cameras() 