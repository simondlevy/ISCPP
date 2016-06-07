#!/usr/bin/env python3

"""
readposllh.py : Read binary POSLLH messages from a UBlox GPS unit

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
from struct import unpack

def decode(payload, pos, divisor):
    
    return unpack("i", payload[pos:pos+4])[0] / divisor

port = Serial("/dev/ttyUSB0", 57600)

state = 0
message = b""

while True:

    c = port.read(1)
    x = ord(c)

    if state == 0:
        if x == 0xB5:
            state = 1
            
    elif state == 1:
        if x == 0x62:
            state = 2
        else:
            state = 0
            
    else:
        if x == 0xB5:
            if message[0] == 0x01 and message[1] == 0x02:
                payload = message[4:32]
                lon = decode(payload, 4, 1e7)
                lat = decode(payload, 8, 1e7)
                alt = decode(payload, 12, 1e3)
                print(lat, lon, alt)
            message = b""
            state = 1
        else:
            message += c
