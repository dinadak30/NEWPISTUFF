#!/usr/bin/python

import subprocess
import time

if __name__ == "__main__":
    try:
		# Run takepic.py script
        subprocess.run(["python", "takepic.py"]) 
       

        # Run Circle_detect.py script
        subprocess.run(["python", "Circle_detect.py"])

        
        
    except Exception as e:
        print(f"Error occurred: {e}")

