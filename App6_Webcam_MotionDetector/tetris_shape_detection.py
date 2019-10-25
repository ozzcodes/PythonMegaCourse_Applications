# import the necessary packages
import imutils
import cv2

# load the Tetris block image, convert it to grayscale, and threshold
# the image
# noinspection PyUnresolvedReferences
print("OpenCV Version: {}".format(cv2.__version__))
image = cv2.imread("resource_files/tetris_blocks.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

# check to see if we are using OpenCV 2.X or OpenCV 4
if imutils.is_cv2() or imutils.is_cv4():
    (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                 cv2.CHAIN_APPROX_SIMPLE)

# check to see if we are using OpenCV 3
elif imutils.is_cv3():
    (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)

# draw the contours on the image
# noinspection PyUnboundLocalVariable
cv2.drawContours(image, cnts, -1, (240, 0, 159), 3)
cv2.imshow("Image", image)
print(image)
cv2.waitKey(0)
cv2.destroyAllWindows()
