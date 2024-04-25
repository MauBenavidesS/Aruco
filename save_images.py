import cv2
import os

# Create a folder to save captured images
output_folder = "captured_images"
os.makedirs(output_folder, exist_ok=True)

# Initialize webcam
cap = cv2.VideoCapture(10)  # 0 corresponds to the default camera (you can change it if you have multiple cameras)

# Counter for image filenames
image_counter = 0

# Function to capture and save images
def capture_and_save_image():
    global image_counter
    ret, frame = cap.read()

    # Display the captured frame (optional)
    cv2.imshow("Captured Image", frame)
    cv2.waitKey(1)

    # Save the captured image
    image_path = os.path.join(output_folder, f"captured_image_{image_counter}.jpg")
    cv2.imwrite(image_path, frame)
    print(f"Image {image_counter} saved: {image_path}")

    # Increment the counter
    image_counter += 1

# Capture images until the user presses 'q' key
print("Press 'q' to exit and save captured images.")
while True:
    # Capture a frame
    ret, frame = cap.read()

    # Display the captured frame (optional)
    cv2.imshow("Capture Images", frame)

    # Check for user input
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('c'):
        # Capture and save an image when the 'c' key is pressed
        capture_and_save_image()

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
