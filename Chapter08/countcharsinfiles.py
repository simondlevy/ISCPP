#!/usr/bin/env python3

"""
countcharsinfiles.py : occurrences of characters in a set of files

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
from countchars import countchars

def countCharsInFiles(filenames):
    """
    countcharsInFiles(filenames): sum up counts of
    alphabetic characters in files.  Ignores upper/lower-case
    distinction.
    Example: 
    countCharsInFiles(["mobydick.txt", "hamlet.txt", "sula.txt"])
    """
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    counts = zeros(len(letters)) 

    for filename in filenames:

        f = open(filename)

        s = f.read()
        
        counts += countchars(s.lower(), letters)
                
        f.close()
        
    return counts, letters

if __name__ == "__main__":
    """
    Example
    """
    counts, letters = countCharsInFiles(["countchars.py", "countcharsinfiles.py"])
    print(counts)
    print(letters)
