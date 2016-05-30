#!/usr/bin/env python3

"""
nicecos.py : Friendly cosine function supporting radians or degrees
             Raises an exception on unrecognized units

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

from math import pi, cos

def nicecos(angle, units="radians"):

    if units == "radians":
        return cos(angle)

    elif units == "degrees":
        return cos(pi / 180 * angle)

    else:
        raise Exception("Uknown units: " + units)

if __name__ == "__main__":
    """
    Examples
    """
    print(nicecos(0))
    print(nicecos(45, "degrees"))
    print(nicecos(2, "oopsie"))
