import sys
sys.path.append('/home/YCCap/ballmap/env/lib/python3.11/site-packages/cv2')
import cv2
import sys
sys.path.append('/home/YCCap/ballmap/env/lib/python3.11/site-packages/numpy')
import numpy as np
#import sys
#sys.path.append('/home/YCCap/ballmap/env/lib/python3.11/site-packages/cv2/qt/plugins/platforms/libqxcb.so')
#import libqxcb.so
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/home/YCCap/ballmap/env/lib/python3.11/site-packages/cv2/qt/plugins/platforms'

#import os
#os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/usr/lib/aarch64-linux-gnu/qt5/plugins/'
image_path = '/home/YCCap/ballmap/Imagecapture.jpg'

def detect_red_ball(image_path):
    img = cv2.imread(image_path)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        rect = cv2.minAreaRect(contour)
        (x,y),(w,h), angle = rect
        box=cv2.boxPoints(rect)
        box=np.int0(box)
        cv2.circle(img, (int(x), int(y)), 5, (100,200,0),-1)
        cv2.polylines(img,[box],True, (255,0,0),2)
        cv2.putText(img, "Width {}".format(round(w,1)), (int(x),int(y-15)),cv2.FONT_HERSHEY_PLAIN,2,(100,200,0),2)
     #   cv2.putText(img, 'Red Ball', (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,0),2)
        
    cv2.imshow('Red Ball Detection',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
detect_red_ball(image_path)
