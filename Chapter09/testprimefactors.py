#!/usr/bin/env python3

"""
testprimefactors.py : Use excpetion-handling to test a prime-factors generator

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

def smallestfactor(n):

    res = n
    
    for k in range(2, int(sqrt(n)) + 1):

        if mod(n,k) == 0:
            res = k 
            break   

    return res

def primeFactors(n):

    factors = array([], int)

    remaining = n 

    while remaining > 1: # Condition for continuing

       sf = smallestfactor(remaining)

       factors = append(factors, sf) # Update accumulator

       remaining //= sf

    return factors

def testPrimeFactors(n):
    '''
    test primefactors on n random inputs
    return inputs for which the answer was wrong
    or an error was generated
    '''
    res = array([])
    edgecases = array([-1, 0, 1, 2, -10, 4.1])
    randomcases = floor(1000000000000*random.rand(n)) # Round to integers

    for k in append(edgecases, randomcases):
        
       try:
          factors = primeFactors(k)
          if prod(factors) != k: # Test for wrong answer
             res = append(res, k)
       except:
          res = append(res,k)    # An error was generated

    return res


if __name__ == "__main__":
    """
    Example
    """
    print(testPrimeFactors(10))
