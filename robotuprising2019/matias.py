#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


Tarttuja = Motor(Port.A)

Tarttuja.run_until_stalled(200, Stop.COAST, 50)
Tarttuja.reset_angle(0)
Tarttuja.run_target(200, -90)

def robot_pick(position):
    # Close the gripper to grab the wheel stack.
    Tarttuja.run_until_stalled(200, Stop.HOLD, 50)

def robot_release(position):
    # Open the gripper to release the wheel stack.
    Tarttuja.run_target(200, -90)

LEFT = 160
MIDDLE = 100
RIGHT = 40 

while True: 
    # Move an object from the left to the middle.
    robot_pick(LEFT)
    robot_release(MIDDLE)

    # Move an object from the right to the left. 
    robot_pick(RIGHT)
    robot_release(LEFT)

    # Move an object from the middle to the right.
    robot_pick(MIDDLE)
    robot_release(RIGHT)

# Low battery warning
if brick.battery.voltage() < 7000:
    brick.sound.beep()
