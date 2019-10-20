import cv2

face_cascade = cv2.CascadeClassifier('resource_files/haarcascade_frontalface_default.xml')

img = cv2.imread('resource_files/Kelly_Austin_Fullbody.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect the face of image using pixel dimensions
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.075,
                                      minNeighbors=5)

# create a rectangle around image to detect in pixels
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

# Prints type of faces object
print(type(faces))  # Numpy Array
print(faces)

cv2.imwrite('resource_files/face_detect_kelly_austin.jpg', img)

cv2.imshow('Gray_Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
