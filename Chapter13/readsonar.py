#!/usr/bin/env python3

"""
readsonar.py : Parse ASCII data from a MaxBotix ultrasonic sensor

Copyright (C) Simon D. Levy 2016

This file is part of ISCPP.

ISCPP is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,     
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU Lesser General Public License 
along with this code.  If not, see <http:#www.gnu.org/licenses/>.
"""

from serial import Serial

port = Serial("/dev/ttyUSB0", 57600)

msg = ""

while True:

    b = port.read(1).decode("utf-8")

    if b == "R":
        if len(msg) == 5:
            print(int(msg[:4]))
        msg = ""
    else:
        msg += str(b)
