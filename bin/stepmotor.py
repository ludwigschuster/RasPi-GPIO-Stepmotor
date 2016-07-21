import time as timer
import RPi.GPIO as GPIO
import math

#class Stepmotor:
GPIO.setmode(GPIO.BCM)

# This are the Pins which will be used on the raspberry Pi
A=18
B=23
C=24
D=25
time = 0.010

# Declare pins as output
GPIO.setup(A,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.setup(C,GPIO.OUT)
GPIO.setup(D,GPIO.OUT)
GPIO.output(A, False)
GPIO.output(B, False)
GPIO.output(C, False)
GPIO.output(D, False)

class Stepmotor:
	# 8 steps are possible - here those 8 steps are defined
	def Step1(self):
    		GPIO.output(D, True)
    		timer.sleep (time)
    		GPIO.output(D, False)

	def Step2(self):
    		GPIO.output(D, True)
    		GPIO.output(C, True)
    		timer.sleep (time)
    		GPIO.output(D, False)
    		GPIO.output(C, False)

	def Step3(self):
    		GPIO.output(C, True)
    		timer.sleep (time)
    		GPIO.output(C, False)

	def Step4(self):
    		GPIO.output(B, True)
    		GPIO.output(C, True)
    		timer.sleep (time)
    		GPIO.output(B, False)
    		GPIO.output(C, False)

	def Step5(self):
    		GPIO.output(B, True)
    		timer.sleep (time)
    		GPIO.output(B, False)

	def Step6(self):
   		GPIO.output(A, True)
    		GPIO.output(B, True)
    		timer.sleep (time)
    		GPIO.output(A, False)
    		GPIO.output(B, False)

	def Step7(self):
    		GPIO.output(A, True)
    		timer.sleep (time)
    		GPIO.output(A, False)

	def Step8(self):
    		GPIO.output(D, True)
    		GPIO.output(A, True)
    		timer.sleep (time)
    		GPIO.output(D, False)
    		GPIO.output(A, False)

	def turn(self,count):
		for i in range (count):
			self.Step1()
			self.Step2()
			self.Step3()
			self.Step4()
			self.Step5()
			self.Step6()
			self.Step7()
			self.Step8()
			
	def close(self):
		GPIO.cleanup()
	
	# turn n steps
	#          (support with number of steps to turn)
	def turnSteps(self, count):
		for i in range (count):
			self.turn(1)
			
	# turn n degrees (small values can lead to inaccuracy)
	#          (support with degrees to turn)
	def turnDegrees(self, count):
		self.turn(round(count*512/360,0))
		
	# turn for translation of wheels or windlass (inaccuracies involved e.g. due to thickness of rope)
	#          (support with distance and radius in same metric)
	def turnDistance(self, dist, rad)
		self.turn(round(512*dist/(2*math.pi*rad),0))
