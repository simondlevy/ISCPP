#!/usr/bin/env python3

"""
counterclass.py : A simple Python class with a single instance variable

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

class Counter:

    def __init__(self):
        self.count = 0

    def keepcount(self):
        self.count += 1
        return self.count

if __name__ == "__main__":
    """
    Example
    """
    c = Counter()
    print(c.keepcount())
    print(c.keepcount())
    print(c.keepcount())
