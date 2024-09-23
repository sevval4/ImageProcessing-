Image Processing with OpenCV
This project demonstrates basic image processing operations using OpenCV in Python. It reads an image, manipulates the image by cropping it, displays individual color channels (Red, Green, Blue), and converts the image to grayscale.

Features
Image Loading: Reads an image from the specified path and converts it into a matrix.
Cropping: Crops a specific region of the image based on given coordinates.
Color Channels: Extracts and displays the Red, Green, and Blue channels of the cropped image separately.
Grayscale Conversion: Converts the image to grayscale and displays it.
Basic Pixel Operations: Prints pixel values from both the original and grayscale images.
Requirements
-Python 3.x
-OpenCV (cv2)
-Numpy

You can install the required packages using:
pip install opencv-python numpy

How to Use
Clone the repository and navigate to the project folder.
Place your desired image in the images folder and adjust the img_path variable in the script to the correct image path.
Run the script using:
python image_processing.py

Example Code:
The script reads an image, extracts pixel values, crops part of the image, displays color channels, and converts the image to grayscale:
img_path = "./images/image.jpg"
img = cv2.imread(img_path)  # Read the image

Output
The script displays the original image, cropped section, individual RGB channels, and grayscale version in separate windows.
It also prints the dimensions, pixel values, and grayscale pixel value of the top-left corner.
