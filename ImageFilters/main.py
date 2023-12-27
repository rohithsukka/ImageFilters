import cv2
import numpy as np

# Read the Image
img = cv2.imread('Resources/car.jpeg')

# Applying  Different filters

# 1. Blur image using Gaussian kernel (Function)
blurImage = cv2.GaussianBlur(img, (7, 7), 0)

# 2.Apply sharpening filter
sharpeningKernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])  # Sharpening kernel
sharpenedImage = cv2.filter2D(img, -1, sharpeningKernel)

# 3.Apply edge detection filters
threshold1 = 100
threshold2 = 200
# Canny edge detection
edgesImage = cv2.Canny(img, threshold1, threshold2)


# Combine filters for creative effects
blended = cv2.addWeighted(blurImage, 0.5, sharpenedImage, 0.5, 0)
unclear = cv2.stylization(img, sigma_s=60, sigma_r=0.07)

# Display the original and filtered images
cv2.imshow('Original Image', img)
cv2.imshow('Blurred (Gaussian)', blurImage)
cv2.imshow('Sharpened', sharpenedImage)
cv2.imshow('Edges (Canny)', edgesImage)
cv2.imshow('Blended', blended)
cv2.imshow('Unclear', unclear)

# use waitKey as 0 for showing the image for infinite seconds and 1 for one millisecond
cv2.waitKey(0)
# To close stop the execution of program
cv2.destroyAllWindows()
