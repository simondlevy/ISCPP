#!/usr/bin/env python3

"""
convertgradev2.py : Working code for converting a number grade to a letter grade

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

def convertGradeV2( score ):
    if score >= 90: 
        return "A"
    elif score >= 80: 
        return "B"
    elif score >= 70: 
        return "C"
    elif score >= 60: 
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    """
    Examples
    """
    myscore = 89.5
    print("A score of %3.1f produces a grade of %s" % (myscore, convertGradeV2(myscore)))
    myscore = 92
    print("A score of %3.1f produces a grade of %s" % (myscore, convertGradeV2(myscore)))
