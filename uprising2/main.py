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
va = True
reitilla = False
i=0
laskuri = 0
while i < 50000:
    vari = variSensori.color()
    Vmoottori.run(-300)
    Omoottori.run(-300)
    time.sleep(0.05)
    if vari == 6:
        Vmoottori.run(200)
        Omoottori.run(-200)
        time.sleep(0.2)
        Vmoottori.run(-200)
        Omoottori.run(-200)
        time.sleep(1)
        Vmoottori.run(-200)
        Omoottori.run(200)
        time.sleep(0.5)
    i +=1
    laskuri += 1
    if laskuri > 30:
        Vmoottori.run(-200)
        Omoottori.run(200)
        time.sleep(1)
        laskuri = 0
    #print(vari)


#B.test_motor = Motor(Port.B)

# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
#test_motor.run_target(500, 90)

# Play another beep sound.
# This time with a higher pitch (1000 Hz) and longer duration (500 ms).
#brick.sound.beep(1000, 500)

# Low battery warning
if brick.battery.voltage() < 7000:
    brick.sound.beep()
