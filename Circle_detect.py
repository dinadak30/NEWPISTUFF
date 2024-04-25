import sys
sys.path.append('/home/YCCap/ballmap/env/lib/python3.11/site-packages/cv2')
import cv2
sys.path.append('/home/YCCap/ballmap/env/lib/python3.11/site-packages/numpy')
import numpy as np
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/home/YCCap/ballmap/env/lib/python3.11/site-packages/cv2/qt/plugins'

# Known diameter of the ball in centimeters
known_diameter_cm = 8.6


# Load the image
img = cv2.imread('/home/YCCap/ballmap/Imagecapture.jpg')

# # Check if the image is loaded successfully
# if image is None:
    # print("Error: Unable to load image.")
# else:
    # # Get image height and width
    # height, width, _ = image.shape
    # print("Image height:", height)
    # print('Image width:', width)
    
# new_height = height // 2
# print('New Height:', new_height)

# new_width = width // 4
# print('New Width:',new_width)
 

# cropped_image = image[new_height:, new_width:(width - new_width)]

# #Display Cropped Image
# cv2.imshow('Cropped Image',cropped_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

    # # Save the cropped image to a file
# cv2.imwrite('cropped_image.jpg', cropped_image)


# Add a midline down the center of the image
cv2.line(img, (img.shape[1] // 2, 0), (img.shape[1] // 2, img.shape[0]), (255, 0, 0), 2)

blur = cv2.blur(img, (1,1))
hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

#red masking
    
# lower1 = np.array([0,100,20]) #([0,10,30])
# upper1 = np.array ([10,255,255])#([10,255,255])

# lower2 = np.array([160,100,20]) #([0,10,30])
# upper2 = np.array([179,255,255])#([10,255,255])

# mask1 = cv2.inRange(hsv, lower1, upper1)
# mask2 = cv2.inRange(hsv, lower2, upper2)
# mask = mask1 + mask2;

#blue masking

lower_blue = np.array([110,130,0])
upper_blue = np.array([130,255,190])
mask = cv2.inRange(hsv, lower_blue, upper_blue)


# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(mask, 
			cv2.HOUGH_GRADIENT, 1, 20, param1 = 300, 
			param2 = .8, minRadius = 15, maxRadius = 200)
#img=mask
# Draw circles that are detected.
if detected_circles is None:
    print ('None')
    final_image = None
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
		cm_per_pixel = known_diameter_cm/diameter_pixels
		
		# Calculate the frame half width
		frame_half_width = cm_per_pixel * 2304
		
		#Calculate distance from camera
		distance_to_ball_cm = frame_half_width / np.tan(0.576)

		# Calculate the distance from the midline to the center point of the ball in the X direction
		distance_to_midline = abs(a - img.shape[1] // 2)
		midline_dist_cm = (distance_to_midline * cm_per_pixel)
		rounded_middist_cm = round(midline_dist_cm,2)

		# Calculate the position for the text labels
		text_offset_x = a - r + int((2 * r - len(f'D: {distance_to_ball_cm:.2f} cm') * 10) / 2)
		text_offset_y = b - 20  # Adjust this value to move the text label higher or lower

		# Display the estimated distance to the ball on the image
		cv2.putText(img, f'Cam Dist: {distance_to_ball_cm:.2f} cm', (text_offset_x, text_offset_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
		cv2.putText(img, f'Mid Dev: {rounded_middist_cm} cm', (a - r, b + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
		# Draw a small circle (of radius 1) to show the center. 
		cv2.circle(img, (a, b), 1, (0, 0, 255), 1) 


		# Center coordinates of the circle
		center_x = a
		center_y = b

		# Radius of the circle
		radius = r
		diameter = 2*radius
		# Calculate the top-left corner coordinates of the cropping rectangle
		x = int(center_x - diameter)
		y = int(center_y - diameter)

		# Calculate the width and height of the cropping rectangle
		width = int(4 * radius)
		height = int(4 * radius)

		# Crop the image using the calculated coordinates and dimensions
		final_image = img[y:y+height, x:x+width]


		# Break out of the loop after processing the first detected circle
		break
		

# Display the final image with the detected circle and midline
cv2.imshow("Detected Circle", final_image) 
cv2.waitKey(0)
cv2.destroyAllWindows()

# if final_image is not None:
    # cv2.imshow("Detected Circle", final_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
# else:
    # print("No circles detected.")
