import cv2
import os
from PIL import Image

from util import get_limits

yellow = [0, 255, 255]  # Define the yellow color in BGR colorspace
cap = cv2.VideoCapture(0)  # Open video capture from camera index 2
save_image = False  # Flag to indicate whether to save the image

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

while True:
    ret, frame = cap.read()  # Read a frame from the video capture

    if not ret:
        break  # Break the loop if no frame was read successfully

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the frame from BGR to HSV colorspace

    lowerLimit, upperLimit = get_limits(color=yellow)  # Call the get_limits function to get the lower and upper limits for yellow color

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)  # Create a mask using the lower and upper limits

    mask_ = Image.fromarray(mask)  # Convert the mask to an Image object

    bbox = mask_.getbbox()  # Get the bounding box coordinates of the mask

    if bbox is not None:  # If a bounding box exists
        x1, y1, x2, y2 = bbox  # Unpack the bounding box coordinates

        # Change the color of the rectangle to blue (BGR: 255, 0, 0)
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 5)  # Draw a blue rectangle around the detected object

        # Save the image when the color is detected
        if save_image:
            image_path = os.path.join(script_dir, 'detected_image.jpg')
            cv2.imwrite(image_path, frame)
            print(f"Image saved at: {image_path}")

    cv2.imshow('frame', frame)  # Display the frame with the rectangle

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # If 'q' key is pressed, break the loop
        break
    elif key == ord('s'):  # If 's' key is pressed, set the flag to save the next detected image
        save_image = True
    else:
        save_image = False  # Reset the flag if no image is detected

cap.release()  # Release the video capture
cv2.destroyAllWindows()  # Close all OpenCV windows