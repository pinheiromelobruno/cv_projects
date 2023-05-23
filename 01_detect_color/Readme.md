# Color Detection Project

## Introduction:
This Color Detection project utilizes computer vision techniques to detect and track a specific color in real-time. By implementing OpenCV and Python, the project enables the detection of a specified color in a live video stream. This project is freely inspired by [Detecting color with Python and OpenCV using HSV colorspace | Computer vision tutorial](https://www.youtube.com/watch?v=aFNDh5k3SjU).

## Project Steps:

* Importing Libraries: The necessary libraries are imported, including cv2 for computer vision tasks, os for file and directory operations, and Image from PIL for image manipulation.
* Color Definition: A specific color is defined using BGR values. For this project, the color yellow is used as an example with the BGR values [0, 255, 255].
* Video Capture Initialization: The project initializes the video capture from the camera index 0 using cv2.VideoCapture.
* Directory Retrieval: The directory path of the current script is obtained using os.path operations. This information will be used for saving the detected image.

## Main Loop:
The project enters a loop where frames are continuously read from the video capture. Within this loop, the following operations are performed:

1. Frame Reading: Each iteration reads a frame from the video capture using cap.read(). If no frame is successfully read, the loop is exited.
2. Colorspace Conversion: The frame is converted from the BGR colorspace to the HSV colorspace using cv2.cvtColor.
3. Lower and Upper Limits Calculation: The get_limits function is called to calculate the lower and upper limits for the specified color in the HSV colorspace.
4. Mask Creation: A mask is created using cv2.inRange by applying the lower and upper limits to the HSV image.
5. Mask Conversion: The mask is converted to an Image object using Image.fromarray.
6. Bounding Box Calculation: The bounding box coordinates of the mask are obtained using mask_.getbbox().
7. Object Detection: If a bounding box exists, a blue rectangle is drawn around the detected object using cv2.rectangle.
8. Image Saving: If the save_image flag is enabled, the frame with the detected object is saved as an image in the specified directory using cv2.imwrite.
9. Frame Display: The current frame, along with the rectangle (if applicable), is displayed using cv2.imshow.
10. User Interaction: The program waits for user input using cv2.waitKey. Pressing 'q' terminates the program, while pressing 's' enables saving the next detected image.

## Cleanup:
After exiting the loop, the video capture is released using cap.release(), and all OpenCV windows are closed using cv2.destroyAllWindows().

## Additional Function:

get_limits(color): This function converts the BGR color values to the HSV colorspace and calculates the lower and upper limits for the specified color range in the HSV colorspace.
