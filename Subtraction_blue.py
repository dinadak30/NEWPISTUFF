
import sys
sys.path.append('/home/YCCap/ballmap/env/lib/python3.11/site-packages/cv2')
import cv2
sys.path.append('/home/YCCap/ballmap/env/lib/python3.11/site-packages/numpy')
import numpy as np
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/home/YCCap/ballmap/env/lib/python3.11/site-packages/cv2/qt/plugins/platforms'

import pexpect
import sys 
import tkinter as tk

image_path1 = '/home/YCCap/ballmap/Background.jpg'
image_path2 = '/home/YCCap/ballmap/Imagecapture.jpg'
img1 = cv2.imread(image_path1)
img2 = cv2.imread(image_path2)

img = cv2.subtract(img2, img1)

# Known diameter of the ball in centimeters
known_diameter_cm = 8.6

# Add a midline down the center of the image
cv2.line(img, (img.shape[1] // 2, 0), (img.shape[1] // 2, img.shape[0]), (255, 0, 0), 2)

blur = cv2.blur(img, (1,1))
hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    
#blue masking

lower_blue = np.array([80,70,10])
upper_blue = np.array([140,255,255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(mask, 
cv2.HOUGH_GRADIENT, 1, 20, param1=300, 
param2=0.8, minRadius=15, maxRadius=100)

# Draw circles that are detected.
if detected_circles is not None: 
    # Convert the circle parameters a, b, and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 

    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 

        # Draw the circumference of the circle. 
        cv2.circle(img, (a, b), r, (0, 255, 0), 1)
        
        # Calculate the diameter in pixels
        diameter_pixels = 2 * r
        
        # Calculate the ratio of cm to pixels 
        cm_per_pixel = known_diameter_cm / diameter_pixels
        
        # Calculate the frame half width
        frame_half_width = cm_per_pixel * 2304
        
        # Calculate distance from camera
        distance_to_ball_cm = frame_half_width / np.tan(0.576)

        # Calculate the distance from the midline to the center point of the ball in the X direction
        distance_to_midline = abs(a - img.shape[1] // 2)
        midline_dist_cm = distance_to_midline * cm_per_pixel
        rounded_middist_cm = round(midline_dist_cm, 2)

        # Calculate the position for the text labels
        text_offset_x = int(a - (5 / 4 * r)) + int((2 * r - len(f'D: {distance_to_ball_cm:.2f} cm') * 10) / 2)
        text_offset_y = int(b - (r / 4))  # Adjust this value to move the text label higher or lower
        text_offset_x2 = int(a - (5 / 4 * r)) + int((2 * r - len(f'D: {distance_to_ball_cm:.2f} cm') * 10) / 2)
        text_offset_y2 = int(b + (r / 4))  # Adjust this value to move the text label higher or lower

        # Display the estimated distance to the ball on the image
        cv2.putText(img, f'Cam Dist: {distance_to_ball_cm:.2f} cm', (text_offset_x, text_offset_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(img, f'Mid Dev: {rounded_middist_cm: .2f} cm', (text_offset_x2, text_offset_y2),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Draw a small circle (of radius 1) to show the center. 
        cv2.circle(img, (a, b), 1, (0, 0, 255), 1) 

        # Center coordinates of the circle
        center_x = a
        center_y = b

        # Radius of the circle
        radius = r
        diameter = 2 * radius

        # Calculate the top-left corner coordinates of the cropping rectangle
        x = int(center_x - radius)
        y = int(center_y - radius)

        # Calculate the width and height of the cropping rectangle
        width = int(diameter)
        height = int(diameter)

        # Crop the image using the calculated coordinates and dimensions
        final_image = img[y:y + height, x:x + width]

        # Break out of the loop after processing the first detected circle
        break

# Create a window with fullscreen flag
cv2.namedWindow("Detected Circle", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Detected Circle", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Mouse event callback function
def mouse_callback(event, x, y, flags, param):
    global double_click
    if event == cv2.EVENT_LBUTTONDBLCLK:
        double_click = True

# Set mouse callback function
cv2.setMouseCallback("Detected Circle", mouse_callback)

# Display the final image with the detected circle and midline
cv2.imshow("Detected Circle", final_image)
cv2.imwrite('final_image.jpg', final_image)

# Wait for double-click to close the window
double_click = False
while not double_click:
    cv2.waitKey(50)  # Poll for events every 50 milliseconds

# Close the OpenCV window
cv2.destroyAllWindows()
