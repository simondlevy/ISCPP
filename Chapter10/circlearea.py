#!/usr/bin/env python3

"""
circlearea.py: Prompts the user for the radius of a circle and computes and prints the circle's area.

Copyright (C) Kenneth A. Lambert 2016

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

from breezypythongui import EasyFrame
import math

class CircleArea(EasyFrame):
    """Computes and displays the area of a circle."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Circle Area")

        # Label and field for the radius
        self.addLabel(text = "Radius",
                      row = 0, column = 0)
        self.radiusField = self.addFloatField(value = 0.0,
                                               row = 0,
                                               column = 1)

        # Label and field for the area
        self.addLabel(text = "Area",
                      row = 1, column = 0)
        self.areaField = self.addFloatField(value = 0.0,
                                              row = 1,
                                              column = 1)
        self.areaField["state"] = "readonly"

        # The command button
        self.addButton(text = "Compute", row = 2, column = 0,
                       columnspan = 2, command = self.computeArea)

    # The event handling method for the button
    def computeArea(self):
        """Inputs the radius, computes the area,
        and outputs the result."""
        radius = self.radiusField.getNumber()
        area = math.pi * radius ** 2
        self.areaField.setNumber(area)

#Instantiate and pop up the window."""
if __name__ == "__main__":
    CircleArea().mainloop()
