#!/usr/bin/env python3

"""
risk.py : compute the probability of a defender winning at the game Risk

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

def risk():

    wincount = 0

    for a1 in range(1,7):
        for a2 in range(1,7):
            for d in range(1,7):
                if d >= max(a1,a2):
                    wincount += 1

    return wincount/216.


if __name__ == "__main__":
    """
    Example
    """
    print(risk())
