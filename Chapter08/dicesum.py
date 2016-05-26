#!/usr/bin/env python3

"""
dicesum.py : report probability of a given dice roll

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

def dicesum(score):

    count = 0

    for die1 in range(1,7):
        for die2 in range(1,7):
            if score == die1 + die2:
                count += 1

    return count / 36.


if __name__ == "__main__":
    """
    Example
    """
    print('Probability of rolling a seven = %f' % dicesum(7))
