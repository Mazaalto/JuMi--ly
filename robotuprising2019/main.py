#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

irSensor = UltrasonicSensor(Port.S1)
print(irSensor.distance())

Vmoottori = Motor(Port.B, Direction.CLOCKWISE)
Omoottori = Motor(Port.C, Direction.COUNTERCLOCKWISE)

# Play a sound
brick.sound.file("Taistelujaska.wav)
time.sleep(2)

Vmoottori.run(100)
Omoottori.run(100)
time.sleep(4)

Vmoottori.stop()
Omoottori.stop()

Vmoottori.run(-100)
Omoottori.run(100)
time.sleep(1)

Vmoottori.stop()
Omoottori.stop()
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
