#!/usr/bin/env python3

"""
rectangleclass.py : A simple Python class for modeling rectangles

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

class Rectangle:

    def __init__(self, ulx, uly, w, h):
        self.ulx = ulx
        self.uly = uly
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def resize(self, dw, dh):
        self.w += dw
        self.h += dh

    def move(self, dx, dy):
        self.ulx += dx
        self.uly += dy

if __name__ == "__main__":
    """
    Example
    """
    r = Rectangle(10, 10, 50, 30)
    print(r.area())
    r.resize(10, 10)
    print(r.area())
