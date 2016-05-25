#!/usr/bin/env python3

"""
max3v3.py : Deliberately broken code for returning the largest of three numbers

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

def max3V3(a,b,c):
    """
    WARNING: This code is deliberately broken!
    """
    if a > b and  a > c:
        return a
    elif b > a and  b > c:
        return b
    elif c > a and  c > b:
        return c
    else:
       print("Impossible case.")

if __name__ == "__main__":
    """
    Example
    """
    print("Attempting max3V3(3,3,1)")
    max3V3(3,3,1)
