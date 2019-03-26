import RPi.GPIO as GPIO 
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(4,GPIO.IN)

while True:
	GPIO.input(4)
	
	if i == 0:
		print('Motion Detected')
