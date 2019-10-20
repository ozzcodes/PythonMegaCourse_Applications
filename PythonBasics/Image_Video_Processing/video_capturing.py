import cv2
import time

# Capture a video form camera using opencv
# First camera, specify index if multiple camera's
my_video = cv2.VideoCapture(0)

# Allow the camera to be used for specified time
time.sleep(3)

# Allow computer to release imaging from camera
my_video.release()
