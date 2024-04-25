
    
# import RPi.GPIO as GPIO
# import time
# import sys
# import os

# # Set up GPIO using BCM numbering
# GPIO.setmode(GPIO.BCM)

# # Define GPIO pins for the sensor
# beam_sensor_pin = 26
# # Set up the beam sensor pin as input
# GPIO.setup(beam_sensor_pin, GPIO.IN)

# # Flag to track whether the secondary script has been executed
# script_executed = False

# # Function to be called when the sensor is triggered
# def sensor_triggered(channel):
    # global script_executed
    # if not script_executed:
        # print("Object detected!")
        # # Wait for 10 seconds
        # time.sleep(10)
        # print("Exiting program")
        # GPIO.cleanup()  # Clean up GPIO on exit

        # # Save the current directory
        # current_directory = os.getcwd()

        # # Change directory to ballmap
        # os.chdir('/home/YCCap/ballmap')

        # # Change directory back to the original directory
        # os.chdir(current_directory)

        # sys.exit()

# # Add event detection to the sensor pin
# GPIO.add_event_detect(beam_sensor_pin, GPIO.RISING, callback=sensor_triggered)

# try:
    # print("Break beam sensor initialized. Waiting for objects...")
    # while True:
        # # Keep the script running
        # time.sleep(1)
        
# except KeyboardInterrupt:
    # print("\nExiting program")
    # GPIO.cleanup()  # Clean up GPIO on exit

import RPi.GPIO as GPIO
import time
import sys
import os

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the sensor
beam_sensor_pin = 26
# Set up the beam sensor pin as input
GPIO.setup(beam_sensor_pin, GPIO.IN)


# Function to be called when the sensor is triggered
def sensor_triggered():

        print("Object detected!")
        # # Wait for 10 seconds
        # time.sleep(10)
       # print("Exiting program")
        GPIO.cleanup()  # Clean up GPIO on exit
        sys.exit()

try:
    print("Break beam sensor initialized. Waiting for objects...")
    while True:
        if GPIO.input(beam_sensor_pin) == GPIO.LOW:
            sensor_triggered()
        time.sleep(0.1)  # Poll every 0.1 second
        
except KeyboardInterrupt:
    print("\nExiting program")
    GPIO.cleanup()  # Clean up GPIO on exit
