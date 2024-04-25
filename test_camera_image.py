import cv2

# Open the default camera (usually the webcam)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera")
else:
    # Capture a single frame
    ret, frame = cap.read()

    if ret:
        # Display the captured frame in a window
        cv2.imshow("Captured Frame", frame)

        # Wait until any key is pressed to close the window
        cv2.waitKey(0)

        # Close the window
        cv2.destroyAllWindows()
    else:
        print("Error: Could not read frame")

# Release the camera
cap.release()
