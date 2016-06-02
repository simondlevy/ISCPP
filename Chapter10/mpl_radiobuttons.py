#!/usr/bin/env python3

"""
mpl_radiobuttons.py : Example of radio buttons in Matplotlib

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
from matplotlib.widgets import RadioButtons

# Set up sine signals with three different frequencies
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(8*np.pi*t)

# Plot the first signal
fig, ax = plt.subplots()
l, = ax.plot(t, s0, lw=2, color="red")
plt.subplots_adjust(left=0.3)

# Set up a radio box and callback for choosing frequencies

axcolor = "lightgoldenrodyellow"
rax = plt.axes([0.05, 0.7, 0.15, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ("2 Hz", "4 Hz", "8 Hz"))

def hzfunc(label):
    hzdict = {"2 Hz":s0, "4 Hz":s1, "8 Hz":s2}
    ydata = hzdict[label]
    l.set_ydata(ydata)
    plt.draw()
radio.on_clicked(hzfunc)

# Set up a radio box and callback for choosing plot colors

rax = plt.axes([0.05, 0.4, 0.15, 0.15], axisbg=axcolor)
radio2 = RadioButtons(rax, ("red", "blue", "green"))

def colorfunc(label):
    l.set_color(label)
    plt.draw()
radio2.on_clicked(colorfunc)

# Set up a radio box and callback for choosing plot styles

rax = plt.axes([0.05, 0.1, 0.15, 0.15], axisbg=axcolor)
radio3 = RadioButtons(rax, ("-", "--", "-.", "steps", ":"))

def stylefunc(label):
    l.set_linestyle(label)
    plt.draw()
radio3.on_clicked(stylefunc)

plt.show()
