#!/usr/bin/env python3

"""
mpl_commandbuttons.py : Example of check buttons in Matplotlib

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
from matplotlib.widgets import CheckButtons

# Set up sine signals with three different frequencies
t = np.arange(0.0, 2.0, 0.01)
s0 = np.sin(2*np.pi*t)
s1 = np.sin(4*np.pi*t)
s2 = np.sin(6*np.pi*t)


# Plot the first signal
fig, ax = plt.subplots()
l0, = ax.plot(t, s0, visible=False, lw=2)
l1, = ax.plot(t, s1, lw=2)
l2, = ax.plot(t, s2, lw=2)
plt.subplots_adjust(left=0.2)

# Set up a check box and callback for choosing frequencies

rax = plt.axes([0.05, 0.4, 0.1, 0.15])
check = CheckButtons(rax, ("2 Hz", "4 Hz", "6 Hz"),
                    (False, True, True))

def func(label):
    if label == "2 Hz": l0.set_visible(not l0.get_visible())
    elif label == "4 Hz": l1.set_visible(not l1.get_visible())
    elif label == "6 Hz": l2.set_visible(not l2.get_visible())
    plt.draw()

check.on_clicked(func)

plt.show()
