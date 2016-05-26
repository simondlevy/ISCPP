#!/usr/bin/env python3

"""
squarerootv1.py : Primitive version of square-root function with two iterations

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

def squarerootV1(x):

    if x > 1:
        lower = 1
        upper = x
    else:
        lower = x
        upper = 1

    middle = (lower+upper)/2. 

    if middle*middle > x:
        upper = middle
    else:
        lower = middle

    middle = (lower+upper)/2.

    if middle*middle > x:
        upper = middle
    else:
        lower = middle

    middle = (lower+upper)/2.

    if middle*middle > x:
        upper = middle
    else:
        lower = middle

    return (lower+upper)/2.


if __name__ == "__main__":
    """
    Example
    """
    print(squarerootV1(9))
    print(squarerootV1(0.16))

