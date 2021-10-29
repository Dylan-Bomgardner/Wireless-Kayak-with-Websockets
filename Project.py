#!/usr/bin/python3
import time
import sys
from gpiozero import Motor

motor1 = Motor (4,14)
motor2 = Motor (17,27)


motor1.foward()
motor2.backward()

while True: 
    time.sleep(5)
    motor1.reverse()
    motor2.reverse()

motor1.stop()
motor2.stop()


