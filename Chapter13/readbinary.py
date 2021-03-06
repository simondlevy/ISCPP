#!/usr/bin/env python3

"""
readbinary.py : Read binary data over a serial port

This program was tested with a UBlox GPS unit using an FTDI adapter,
and may not work for other configurations.

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

port = Serial('/dev/ttyUSB0', 57600)

while True:

    print('%02X' % ord(port.read(1)), end=" ")
