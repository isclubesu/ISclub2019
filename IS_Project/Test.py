import gpiozero 
import RPi.GPIO as GPIO
import time
import picamera
from io import BytesIO
from PIL import Image

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

pause_time=time.time()

test = 0
while test==0:
	
	start_time = time.time()
	test = GPIO.input(4)
	while test:
		print("---%s seconds ---" %(time.time()-start_time))
		print (test)
		test = GPIO.input(4)
	test = 0
		
#def capture_img():

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(11,GPIO.IN)




#pause_time=time.time()

#test = 0
#while test==0:
#	
#	start_time = time.time()
#	test = GPIO.input(4)
#	while test:
#		print("---%s seconds ---" %(time.time()-start_time))
#		print (test)
#		test = GPIO.input(4)
#	test = 0
		
#def capture_img():
