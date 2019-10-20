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

# Create a new, resized image and save
resized_image = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
cv2.imshow('Hexacopter', resized_image)
cv2.imwrite('resource_files/Tarot680_Resized.jpg', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
