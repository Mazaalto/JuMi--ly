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
    if vari == 6:
        Vmoottori.run(50)
        Omoottori.run(-120)
        time.sleep(2.5)
        laskuri += 1
    else:
        Vmoottori.run(-150)
        Omoottori.run(-70)
        time.sleep(0.1)
    if laskuri >= 2:
        Vmoottori.run(100)
        Omoottori.run(100)
        time.sleep(2)
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
