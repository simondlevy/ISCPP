#!/usr/bin/env python3

"""
arrange2.py : Accept two numbers and return them as smaller, bigger

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

def arrange2(a,b):
    """
    which of a and b is smaller and which is bigger
    """
    if a < b:
        smaller = a
        bigger = b
    else:
        smaller = b
        bigger = a
    return smaller,bigger

if __name__ == "__main__":
    """
    Examples
    """
    print(arrange2(4,1))
    print(arrange2(3,7))
    print(arrange2(5,5))

