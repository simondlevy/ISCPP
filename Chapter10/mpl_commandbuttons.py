#!/usr/bin/env python3

"""
mpl_commandbuttons.py : Example of command buttons in Matplotlib

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

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Create an array of possible frequencies
freqs = np.arange(2, 20, 3)

# Display the first frequency
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2*np.pi*freqs[0]*t)
l, = plt.plot(t, s, lw=2)

class State:
    """ A class to track the frequency chosen by the user"""

    def __init__(self):
        self.index = 0

    def increase(self, event):
        self.update(+1)

    def decrease(self, event):
        self.update(-1)

    def update(self, direction):
        self.index += direction
        i = self.index % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()        

# Set up some buttons and associate them with State methods
state = State()
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, "Next")
bnext.on_clicked(state.increase)
bprev = Button(axprev, "Previous")
bprev.on_clicked(state.decrease)

plt.show()
