import sys
sys.path.append('/home/YCCap/ballmap/env/lib/python3.11/site-packages/cv2')
import cv2
sys.path.append('/home/YCCap/ballmap/env/lib/python3.11/site-packages/numpy')
import numpy as np
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/home/YCCap/ballmap/env/lib/python3.11/site-packages/cv2/qt/plugins/platforms'

import pexpect
import sys 

def execute_commands_interactively(commands):
    try:
        # Spawn a shell
        child = pexpect.spawn('/bin/bash')
        child.logfile = sys.stdout.buffer
        
        # Loop through commands
        for command in commands:
            child.sendline(command)
            child.expect(pexpect.EOF)
    except Exception as e:
        print(f"Error executing commands interactively: {e}")
    finally:
        child.close()

if __name__ == "__main__":
    # Define the commands to execute interactively
    commands_to_execute = [
        "libcamera-jpeg -o Background.jpg"
    ]

    execute_commands_interactively(commands_to_execute)


import pexpect
import sys 

def execute_commands_interactively(commands):
    try:
        # Spawn a shell
        child = pexpect.spawn('/bin/bash')
        child.logfile = sys.stdout.buffer
        
        # Loop through commands
        for command in commands:
            child.sendline(command)
            child.expect(pexpect.EOF)
    except Exception as e:
        print(f"Error executing commands interactively: {e}")
    finally:
        child.close()

if __name__ == "__main__":
    # Define the commands to execute interactively
    commands_to_execute = [
        "libcamera-jpeg -o Imagecapture.jpg"
    ]

    execute_commands_interactively(commands_to_execute)


image_path1 = '/home/YCCap/ballmap/Background.jpg'
image_path2 = '/home/YCCap/ballmap/Imagecapture.jpg'
img1 = cv2.imread(image_path1)
img2 = cv2.imread(image_path2)

img = cv2.subtract(img2, img1)

#cv2.imshow('image', subtracted)


cv2.waitKey(0)
cv2.destroyAllWindows()

# Known diameter of the ball in centimeters
known_diameter_cm = 8.6

#image_path = '/home/YCCap/ballmap/Imagecapture.jpg'
#img = cv2.imread(image_path)

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

lower1 = np.array([90,50,50]) #([0,10,30])
upper1 = np.array ([120,255,255])#([10,255,255])

lower2 = np.array([120,50,50]) #([0,10,30])
upper2 = np.array([150,255,255])#([10,255,255])

mask1 = cv2.inRange(hsv, lower1, upper1)
mask2 = cv2.inRange(hsv, lower2, upper2)
mask = mask1 + mask2;

# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(mask, 
			cv2.HOUGH_GRADIENT, 1, 20, param1 = 300, 
			param2 = .8, minRadius = 15, maxRadius = 75)
#img=mask
# Draw circles that are detected.
if detected_circles is None:
    print ('None')
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
		
		# Break out of the loop after processing the first detected circle
		break

# Display the final image with the detected circle and midline
cv2.imshow("Detected Circle", img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
