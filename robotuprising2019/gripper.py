#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase


Tarttuja = Motor(Port.A)

Vmoottori = Motor(Port.B, Direction.CLOCKWISE)
Omoottori = Motor(Port.C, Direction.COUNTERCLOCKWISE)

# Play a sound
brick.sound.file("Taigit@github.com:Mazaalto/JuMi--ly.gitgit@github.com:Mazaalto/JuMi--ly.gitstelujaska.wav)
time.sleep(1)

Vmoottori.run_time(300, 2000)
Omoottori.run_time(300, 2000)
# Initialize a motor at port
#B.test_motor = Motor(Port.B)
time.sleep(1)
# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
#test_motor.run_target(500, 90)
Vmoottori.run_time(-300, 1000)
Omoottori.run_time(300, 1000)
# Play another beep sound.
# This time with a higher pitch (1000 Hz) and longer duration (500 ms).
#brick.sound.beep(1000, 500)

# Initialize the gripper. First rotate the motor until it stalls. 
# Stalling means that it cannot move any furhter. This position
# corresponds to the closed position. Then rotate the motor
# by 90 degrees such that the gripp is open.

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
