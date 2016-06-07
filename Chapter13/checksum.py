#!/usr/bin/env python3

"""
checksum.py : Demonstrates checksums

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

def checksum(msg):
    
    x = 0

    for c in msg:
       
        x = x ^ ord(c)

    return x

if __name__ == "__main__":
    """
    NMEA example
    """
    msg = "$GPGLL,3747.33617,N,07926.54875,W,200846.10,A,D*71"
    print(checksum(msg[1:-3]))

