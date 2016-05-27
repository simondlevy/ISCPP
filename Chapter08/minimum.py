#!/usr/bin/env python3

"""
minimum.py : Compute the minimum element in a sequence using a loop

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

def minimum(L):
    S = L[0] 
    for item in L:
        if item < S: 
            S = item 
    return S


if __name__ == "__main__":
    """
    Example
    """
    print(minimum([5,1,4,2,3,7,6,8,9,0]))
