#!/usr/bin/env python3

"""
mpl_cursors.py : Example of cursors in Matplotlib

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

from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, axisbg="#FFFFCC")

t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*2*t)
plt.plot(t, s, lw=2)

# set useblit = True for enhanced performance
cursor = Cursor(ax, useblit=True, color='red', linewidth=2 )

plt.show()
