#!/usr/bin/env python3

"""
squareclass.py : A simple example of inheritance in Python

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

from rectangleclass import Rectangle

class Square(Rectangle):

    def __init__(self, ulx, uly, s):
        Rectangle.__init__(self, ulx, uly, s, s)

    def resize(self, ds):
        Rectangle.resize(self, ds, ds)


if __name__ == "__main__":
    """
    Example
    """
    s = Square(10, 10, 50)
    print(s.area())
    s.resize(10)
    print(s.area())
