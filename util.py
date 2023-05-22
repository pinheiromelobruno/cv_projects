import numpy as np  # Importing the NumPy library for numerical operations
import cv2  # Importing the OpenCV library for computer vision tasks


def get_limits(color):
    # Convert the BGR color values to HSV color space
    c = np.uint8([[color]])  # Here insert the BGR values which you want to convert to HSV
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    # Define the lower and upper limits in the HSV color space
    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    # Convert the limits to the appropriate data type
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit