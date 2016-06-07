#!/usr/bin/env python3

"""
parity.py : Demonstrates parity checking

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

def parity(bits):

    x = 0

    for b in bits:

        x = x ^ b

    return x

if __name__ == "__main__":
    """
    Examples
    """
    print(parity([0,1,1,0]))
    print(parity([0,1,0,0]))

