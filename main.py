import cv2
import numpy as np

img_path = "./images/image.jpg"

# Read the image and convert it into a matrix
img = cv2.imread(img_path)

# Print the dimensions and number of channels of the image
print(img.shape)

# Print the minimum and maximum pixel values in the image
print("Minimum:", np.min(img))
print("Maximum:", np.max(img))

# Print the RGB values of the top-left pixel
print("Image R channel:", img[0, 0, 2])  # Red channel
print("Image G channel:", img[0, 0, 1])  # Green channel
print("Image B channel:", img[0, 0, 0])  # Blue channel

# Define the coordinates for cropping the image
row_start = 210
col_start = 210
row_end = 300
col_end = 350

# Crop the image
img_cropped = img[row_start:row_end, col_start:col_end]

# Display the cropped image
cv2.imshow("Cropped Image", img_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Separate the cropped image into R, G, B channels
img_cropped_R = img_cropped[:, :, 2]
img_cropped_G = img_cropped[:, :, 1]
img_cropped_B = img_cropped[:, :, 0]

# Display the red channel (white areas represent high red intensity)
cv2.imshow("Red Channel", img_cropped_R)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Display the green channel (white areas represent high green intensity)
cv2.imshow("Green Channel", img_cropped_G)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Display the blue channel (white areas represent high blue intensity)
cv2.imshow("Blue Channel", img_cropped_B)
cv2.waitKey(0)
cv2.destroyAllWindows()

# CONVERT THE IMAGE TO GRAYSCALE

img_grayscale = cv2.imread(img_path, 0)  # Read image in grayscale mode
print(img_grayscale.shape)  # Print the dimensions of the grayscale image

# Display the grayscale image
cv2.imshow("Grayscale Image", img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the pixel value of the top-left pixel in the grayscale image
print("First pixel value:", img_grayscale[0, 0])
