#!/usr/bin/env python3

"""
strtomorse.py : Text string to Morse code conversion

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

from numpy import *

def charToMorse(c):
    """
    Complete this function for Exercise 7.12
    """

    return []

def strToMorse(s):

    bcspace = 4             # code for space between characters

    res = array([])         # Initialize the accumulator

    for c in s:             # Loop over characters in the string

       m = charToMorse(c)   # Convert to Morse

       res = append(res, m) # Append to the accumulator

    return res


if __name__ == "__main__":
    """
    Example
    """
    print(strToMorse("SOS"))


