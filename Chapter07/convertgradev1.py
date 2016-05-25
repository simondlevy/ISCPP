#!/usr/bin/env python3

"""
convertgradev1.py : Deliberately broken code for converting a number
                    grade to a letter grade

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

def convertGradeV1( score ):
    """
    WARNING: This code is deliberately broken!
    """
    if score >= 90: 
        return "A"
    elif score >= 80 and  score <= 89: 
        return "B"
    elif score >= 70 and  score <= 79:
        return "C"
    elif score >= 60 and  score <= 69:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    """
    Example
    """
    myscore = 89.5
    print("A score of %3.1f produces a grade of %s!" % (myscore, convertGradeV1(myscore)))
