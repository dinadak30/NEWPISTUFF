import sys
sys.path.append('/home/YCCap/ballmap/env/lib/python3.11/site-packages/cv2')
import cv2
sys.path.append('/home/YCCap/ballmap/env/lib/python3.11/site-packages/numpy')
import numpy as np
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/home/YCCap/ballmap/env/lib/python3.11/site-packages/cv2/qt/plugins/platforms'

# # Load the image
# image = cv2.imread('/home/YCCap/ballmap/Imagecapture.jpg')

# # Check if the image is loaded successfully
# if image is None:
    # print("Error: Unable to load image.")
# else:
    # # Get image height
    # height, width, _ = image.shape

    # # Calculate the halfway point
    # halfway_point = height // 2

    # # Crop the image from halfway to bottom
    # cropped_image = image[halfway_point:, :]

    # # Display the cropped image
    # cv2.imshow('Cropped Image', cropped_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # # Save the cropped image to a file
    # cv2.imwrite('cropped_image.jpg', cropped_image)
    # print("Cropped image saved successfully.")


# Load the image
image = cv2.imread('/home/YCCap/ballmap/Imagecapture.jpg')

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load image.")
else:
    # Get image height and width
    height, width, _ = image.shape
    print("Image height:", height)
    print('Image width:', width)
    
new_height = height // 2
print('New Height:', new_height)

new_width = width // 4
print('New Width:',new_width)


cropped_image = image[new_height:, new_width:(width - new_width)]

#Display Cropped Image
cv2.imwrite('cropped_image.jpg',cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

