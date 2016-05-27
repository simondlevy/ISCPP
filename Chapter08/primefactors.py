#!/usr/bin/env python3

"""
primefactors.py : compute the prime factors of a number

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
from smallestfactor import smallestfactor

def primeFactors(n):

    factors = array([], int)

    remaining = n 

    while remaining > 1: # Condition for continuing

       sf = smallestfactor(remaining)

       factors = append(factors, sf) # Update accumulator

       remaining //= sf

    return factors

if __name__ == "__main__":
    """
    Example
    """
    print(primeFactors(132))
