#!/usr/bin/env pybricks-micropython
import time
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import time

vmoottori = Motor(Port.B, Direction.CLOCKWISE)
omoottori = Motor(Port.C, Direction.CLOCKWISE)
#variSensori = ColorSensor(Port.D)

# Play a sound
#brick.sound.file("Taistelujaska.wav")
i = 0
while i < 50:
    vari = Color.WHITE
    if vari == Color.WHITE:
        vmoottori.run(500)
        omoottori.run(500)
    i+=10;
    brick.sound.beep()
vmoottori.stop()
omoottori.stop()

# Initialize a motor at port
#B.test_motor = Motor(Port.B)

# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
#test_motor.run_target(500, 90)

# Play another beep sound.
# This time with a higher pitch (1000 Hz) and longer duration (500 ms).
#brick.sound.beep(1000, 500)

# Low battery warning
if brick.battery.voltage() < 7000:
    brick.sound.beep()
