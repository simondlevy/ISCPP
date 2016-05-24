#!/usr/bin/env python3

"""
newtoncooling.py : Newton's formula for a cooling cup of coffee.

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

def newtonCooling(T0,  Tenv,  k,  time):
    """
    newtonCooling(T0,  Tenv,  k,  time)
    Temperature  of  a  cooling  object  at  any  given  time
    T0   --  object's  temperature  at  time  0
    Tenv --  environment's  temperature
    k    --  time  constant  of  exponential  cooling
    time --  the  time    
    """
    return Tenv  +  (T0  -  Tenv) * exp(-k*time)

if __name__ == "__main__":
    """
    Example
    """
    t = linspace(0,10,100)
    T0 = 98
    print(newtonCooling(T0, 24.5, 0.0426, t))
