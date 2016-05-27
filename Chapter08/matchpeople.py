#!/usr/bin/env python

"""
matchpeople.py : Match people to tasks for optimal quality

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

def matchpeople(q): 

    bestassignment = [] # no assignment to start  
    bestqualitysofar = 0 

    jobsfora = set(range(4)) 
    for a  in jobsfora: 
        jobsforb = jobsfora - set([a]) 
        for b in jobsforb: 
            jobsforc = jobsforb - set([b]) 
            for c in jobsforc: 
                jobsford = jobsforc - set([c]) 
                for d in jobsford: 
                    totalquality = q[0][a] + q[1][b] + q[2][c] + q[3][d] 
                    if totalquality > bestqualitysofar: 
                        bestqualitysofar = totalquality 
                        bestassignment = [a, b, c, d] 

    return bestassignment


if __name__ == "__main__":
    """
    Example
    """
    q = array([ [7, 4, 2, 4], [6, 8, 5, 2], [4, 7, 1, 3], [6, 5, 2, 1] ])
    print(matchpeople(q))


