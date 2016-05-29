#!/usr/bin/env python3

"""
squarerootv2.py : Iterative square-root function

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

def squarerootV2(x): 

    if x > 1:
        lower = 1
        upper = x
    else:
        lower = x
        upper = 1

    for k in range(20):
        middle = (lower+upper)/2. 
        if middle*middle > x:
            upper = middle
        else:
            lower = middle

    return (upper + lower)/2.


if __name__ == "__main__":
    """
    Example
    """
    print(squarerootV2(9))
    print(squarerootV2(2))

