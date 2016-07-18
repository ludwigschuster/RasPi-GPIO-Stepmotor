from stepmotor import Stepmotor
from time import sleep

print("moving started")
motor = Stepmotor()
print("One Step")
motor.turnSteps(1)
sleep(0.5)
print("20 Steps")
motor.turnSteps(20)
sleep(0.5)
print("quarter turn")
motor.turnDegrees(90)
print("moving stopped")
motor.close()
