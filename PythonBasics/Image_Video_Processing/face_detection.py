import cv2

face_cascade = cv2.CascadeClassifier('resource_files/haarcascade_frontalface_default.xml')

img = cv2.imread('resource_files/ajw_recognition.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray_Image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

