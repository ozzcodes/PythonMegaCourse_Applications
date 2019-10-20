import cv2

img = cv2.imread('resource_files/tarot680.jpg', 0)

# Print the type of image
print(type(img))
# Type is <class 'numpy.ndarray'> Printing image shows numpy array of pixels
print(img)
print(img.shape)
print(img.ndim)

cv2.imshow('Hexacopter', img)
cv2.waitKey(5000)  # pass time to wait before image window closes or 0 to close upon a key pressed
cv2.destroyAllWindows()
