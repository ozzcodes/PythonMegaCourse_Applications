import cv2
import imutils
from datetime import datetime
from cv2 import GaussianBlur
import pandas as pd

# print the opencv version
# noinspection PyUnresolvedReferences
print("OpenCV Version: {}".format(cv2.__version__))
# Assign variable name to initial frame
init_frame = None

# Create a status list
status_list = [None, None]
times = []
df = pd.DataFrame(columns=["Start", "End"])

# Capture an image with opencv
my_video = cv2.VideoCapture(0)

while True:
    check, frame = my_video.read()
    # Note no motion in current frame
    status = 0
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Make the gray image blurry
    gray_scale = GaussianBlur(gray_scale, (21, 21), 0)

    if init_frame is None:
        init_frame = gray_scale
        continue

    # Use the blur frame
    delta_frame = cv2.absdiff(init_frame, gray_scale)
    # Use a new frame named threshold
    threshold_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # Change threshold frame to be delayed, iterate twice
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)

    # check to see if we are using OpenCV 2.X or OpenCV 4
    if imutils.is_cv2() or imutils.is_cv4():
        (cnts, _) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL,
                                     cv2.CHAIN_APPROX_SIMPLE)
    # check to see if we are using OpenCV 3
    else:
        (_, cnts, _) = cv2.findContours(threshold_frame.copy(), cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        rect = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Append a new Status List
    status_list.append(status)

    # Only obtain the last two status list values
    status_list = status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow('Capturing images', gray_scale)
    cv2.imshow('Capturing Gray Frame Blur', delta_frame)
    cv2.imshow('Capturing Threshold Image', threshold_frame)
    cv2.imshow('Color Frame', frame)

    # Time delay in video capture
    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True)

df.to_csv("resource_files/Times.csv")

my_video.release()
cv2.destroyAllWindows()
