import sys
sys.path.append('/home/YCCap/ballmap/env/lib/python3.11/site-packages/cv2')
import cv2
sys.path.append('/home/YCCap/ballmap/env/lib/python3.11/site-packages/numpy')
import numpy as np
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/home/YCCap/ballmap/env/lib/python3.11/site-packages/cv2/qt/plugins/platforms'

import pexpect
import sys 


# Load the images
image_path1 = '/home/YCCap/ballmap/Background.jpg'
image_path2 = '/home/YCCap/ballmap/Imagecapture.jpg'
img1 = cv2.imread(image_path1)
img2 = cv2.imread(image_path2)

# Subtract image2 from image1
subtracted_img = cv2.subtract(img2, img1)

# Convert to grayscale
gray = cv2.cvtColor(subtracted_img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to obtain binary image
_, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area to get circular objects
circles = []
for contour in contours:
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    if perimeter == 0:
        continue  # Skip contours with zero perimeter
    circularity = (4 * np.pi * area) / (perimeter ** 2)
    if circularity > 0.5:  # Tune this threshold based on your requirements
        circles.append(contour)

# Function to sample color at a point
def sample_color(image, point):
    x, y = point
    return image[y, x]

# Define points around the perimeter of the circle
def points_around_circle(center, radius, num_points):
    points = []
    for i in range(num_points):
        angle = i * (2 * np.pi / num_points)
        x = int(center[0] + radius * np.cos(angle))
        y = int(center[1] + radius * np.sin(angle))
        points.append((x, y))
    return points

# Define colors to look for (e.g., blue)
target_colors = [(255, 0, 0)]  # BGR format

# Iterate over detected circles
for contour in circles:
    # Fit a circle to the contour
    center, radius = cv2.minEnclosingCircle(contour)
    center = tuple(map(int, center))
    radius = int(radius)
    
    # Get points around the perimeter of the circle
    circle_points = points_around_circle(center, radius, num_points=10)  # Adjust num_points as needed
    
    # Check if any of the points match the target color
    num_matching_points = sum(1 for point in circle_points if sample_color(img2, point) in target_colors)
    
    # If enough points match, consider the circle as valid
    if num_matching_points >= 2:  # Adjust threshold as needed
        cv2.circle(img2, center, radius, (0, 255, 0), 2)

# Display the result
cv2.imshow("Detected Circles", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
