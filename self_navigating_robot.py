#  The objective of the project is to code a two wheel self navigating robot.
#  The microswitches is used to navigate around an arena/maze.

import threading
import time
from time import sleep
import RPi.GPIO as GPIO
from gpiozero import Robot

#  change the pin number according to the connection between the sensors and the circuit board.
left_sensor = 6
right_sensor = 25

#  Whether the it is pull up or pull down depends on the connection.
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_sensor,GPIO.IN)
GPIO.setup(right_sensor,GPIO.IN)

# change the pin number according to the connection between the motors and the circuit board.
machine = Robot(right=(4,27), left =(18,24))

while True:
    if ((GPIO.input(left_sensor) == True) & (GPIO.input(right_sensor) == True)):
          print('nothing is in front')
          sleep(1)
          machine.forward()
          print('forward')
          sleep(1)
          
    elif ((GPIO.input(left_sensor) == False) & (GPIO.input(right_sensor) == True)):
          print('left switch pressed')
          sleep(1)
          machine.backward()
          print('reverse')
          sleep(1)
          machine.stop()
          print('hold')
          sleep(1)
          machine.right()
          print('right')
          sleep(1)
          machine.stop
          print('hold')
          sleep(1)
             
    elif ((GPIO.input(left_sensor) == True) & (GPIO.input(right_sensor) == False)):
          print('right switch pressed')
          sleep(1)
          machine.backward()
          print('reverse')
          sleep(1)
          machine.stop()
          print('hold')
          sleep(1)
          machine.left()
          print('left')
          sleep(1)
          machine.stop
          print('hold')
          sleep(1)
        
    elif ((GPIO.input(left_sensor) == False) & (GPIO.input(right_sensor) == False)):
          print('both switch pressed')
          sleep(1)
          machine.backward()
          print('reverse')
          sleep(1)
          machine.stop()
          print('hold')
          sleep(1)
          machine.right()
          print('right')
          sleep(1)
          machine.stop()
          print('hold')
          sleep(1)
