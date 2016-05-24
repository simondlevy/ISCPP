#!/usr/bin/env python3

"""
newtonwrapper2.py : Version 2 of wrapper for Newton's cooling formula

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

from newtoncooling import *

def newtonWrapper2(T0, time):
     """
     a  wrapper  for  newtonCooling with constant Tenv and k
     """
     return  newtonCooling(T0, 24.5,  0.0426,  time)
 
if __name__ == "__main__":
    """
    Example
    """
    t = linspace(0,10,100)
    T0 = 98
    print(newtonWrapper2(T0, t))
