from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()
camera.rotation = 180

while True:
	pir.wait_for_motion()
	print('You Moved!')
	camera.start_preview()
	sleep(5)
	camera.stop_preview()
	pir.wait_for_no_motion()





