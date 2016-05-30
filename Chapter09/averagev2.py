#!/usr/bin/env python3

"""
average.py : Computes the average of an array
             Raises an exception on empty array

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

def averageV2(a):

    n = len(a)

    if n == 0:

        raise Exception("Array must non-empty")

    return sum(a) / n

if __name__ == "__main__":
    """
    Examples
    """
    print(averageV2(arange(10)))
    print(averageV2(array([])))
