from picamera import PiCamera
from gpiozero import MotionSensor
#import RPi.GPIO as GPIO
#import time

pir = MotionSensor(4)
camera = PiCamera()
#GPIO.setup(4,GPIO.IN)


while True:

	#state = GPIO.input(4)
	
	#print(state)

	
	filename = "intruder.h264" 
	pir.wait_for_motion()
	print('You Moved!')
	camera.start_recording(filename)
	pir.wait_for_no_motion()
	camera.stop_recording()
	

