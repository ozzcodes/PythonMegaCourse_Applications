import cv2

# Capture a video form camera using opencv
# First camera, specify index if multiple camera's
my_video = cv2.VideoCapture(0)

# Allow computer to release imaging from camera
my_video.release()
