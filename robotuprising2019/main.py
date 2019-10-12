#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import time


Vmoottori = Motor(Port.B, Direction.CLOCKWISE)
Omoottori = Motor(Port.C, Direction.CLOCKWISE)

variSensori = ColorSensor(Port.S2)

# Play a sound
#brick.sound.file("Taistelujaska.wav")
i = 0
j = 0
k = 0
l = false
while i < 50:
    vari = variSensori.color()
    l = false
    j = 0

    if vari == 6:
        Vmoottori.run(-300)
        Omoottori.run(-300)
    else:
        while !l:
            while j < 5:
                Vmoottori.run(300)
                Omoottori.run(-300)
                vari = variSensori.color()
                if vari == 6:
                    l = true
                    break
                j++;
            while k < 400:
                Vmoottori.run(-300)
                Omoottori.run(300)
                vari = variSensori.color()
                if vari == 6:
                    l = true break
                    break
    print(vari)
#B.test_motor = Motor(Port.B)

# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
#test_motor.run_target(500, 90)

# Play another beep sound.
# This time with a higher pitch (1000 Hz) and longer duration (500 ms).
#brick.sound.beep(1000, 500)

# Low battery warning

# This demo shows how to remote control an Explor3r robot
#
# Red buttons control left motor, blue buttons control right motor.
# Leds are used to indicate movement direction.

from time import sleep
from ev3dev.ev3 import *

# Connect two large motors on output ports B and C
lmotor = LargeMotor('outB')
rmotor = LargeMotor('outC')

# Connect remote control
rc = RemoteControl()

# Initialize button handler
# button = Button()   # not working so disabled

# Turn leds off
Leds.all_off()

def roll(motor, led_group, direction):
    """
    Generate remote control event handler. It rolls given motor into given
    direction (1 for forward, -1 for backward). When motor rolls forward, the
    given led group flashes green, when backward -- red. When motor stops, the
    leds are turned off.

    The on_press function has signature required by RemoteControl class.
    It takes boolean state parameter; True when button is pressed, False
    otherwise.
    """
    def on_press(state):
        if state:
            # Roll when button is pressed
            motor.run_forever(speed_sp=90*direction)
            Leds.set_color(led_group, direction > 0 and Leds.GREEN or Leds.RED)
        else:
            # Stop otherwise
            motor.stop(stop_action='brake')
            Leds.set(led_group, brightness_pct=0)

    return on_press

# Assign event handler to each of the remote buttons
rc.on_red_up    = roll(lmotor, Leds.LEFT,   1)
rc.on_red_down  = roll(lmotor, Leds.LEFT,  -1)
rc.on_blue_up   = roll(rmotor, Leds.RIGHT,  1)
rc.on_blue_down = roll(rmotor, Leds.RIGHT, -1)

# Enter event processing loop
#while not button.any():   #not working so commented out
while True:   #replaces previous line so use Ctrl-C to exit
    rc.process()
    sleep(0.01)
    
# Press Ctrl-C to exit

if brick.battery.voltage() < 7000:
    brick.sound.beep()
