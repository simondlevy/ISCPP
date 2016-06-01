#!/usr/bin/env python3

"""
radiobuttondemo2.py: Demonstrates radio buttons in BreezyPythonGUI

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
from tkinter import HORIZONTAL

class RadioButtonDemo(EasyFrame):
    """When the Display button is pressed, shows the label of
    the selected radio button.  The button group has a
    horizontal alignment."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "Radio Button Demo")

        # Add the button group
        self.group = self.addRadiobuttonGroup(row = 1, column = 0,
                                              columnspan = 4,
                                              orient = HORIZONTAL)

        # Add the radio buttons to the group
        self.group.addRadiobutton("Freshman")
        self.group.addRadiobutton("Sophomore")
        self.group.addRadiobutton("Junior")
        defaultRB = self.group.addRadiobutton("Senior")

        # Select one of the buttons in the group
        self.group.setSelectedButton(defaultRB)
        
        # Output field and command button for the results
        self.output = self.addTextField("", row = 0, column = 1)
        self.addButton("Display", row = 0, column = 0,
                       command = self.display)

    # Event handling method
    def display(self):
        self.output.setText(self.group.getSelectedButton()["value"])

RadioButtonDemo().mainloop()
