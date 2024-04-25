import RPi.GPIO as GPIO
import time

#Set GPIO mode
GPIO.setmode(GPIO.BCM)

#Set pin 16 as an output pin
power_pin = 16
GPIO.setup(power_pin,GPIO.OUT)


try:
	#Supply power(sret pin to high) 
	GPIO.output(power_pin, GPIO.HIGH)
	print("Power supplied to pin 16")
	
	#To stop applying power set pin to LOW
	
	
except KeyboardInterrupt:

	GPIO.cleanup()
