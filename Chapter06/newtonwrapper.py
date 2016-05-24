#!/usr/bin/env python3

"""
newtonwrapper.py : Wrapper for Newton's cooling formula

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

def newtonWrapper(T0,  Tenv,  time):
     """
     a  wrapper  for  newtonCooling with constant k
     """
     return  newtonCooling(T0, Tenv,  0.0426,  time)
 
if __name__ == "__main__":
    """
    Example
    """
    t = linspace(0,10,100)
    T0 = 98
    print(newtonWrapper(T0, 24.5, t))
