from stepmotor import Stepmotor
from time import sleep

print("moving started")
motor = Stepmotor()
print("One Step")
motor.turnOneStep()
sleep(0.5)
print("20 Steps")
motor.turnNSteps(20)
sleep(0.5)
print("quarter turn")
motor.turn90()
print("moving stopped")
motor.close()
