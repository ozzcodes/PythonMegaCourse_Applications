import cv2
import time

# Capture a video form camera using opencv
# First camera, specify index if multiple camera's
my_video = cv2.VideoCapture(0)

a = 0

while True:
    a += 1
    # Print a frame, after checking it's active
    check, frame = my_video.read()
    print(check)
    print(frame)

    # Allow the camera to be used for specified time
    # Also create a gray image just for testing
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(3)

    # Show the image on a frame
    cv2.imshow('Video Capture', gray_scale)
    # Allow computer to release imaging from camera
    key = cv2.waitKey(1)

    # If you press 'q' key then the video will stop
    if key == ord('q'):
        break

print(a)
my_video.release()
cv2.destroyAllWindows()
