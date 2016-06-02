#!/usr/bin/env python3

"""
thermometerview1.py: First view of our thermometer class

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

from thermometer import Thermometer
from breezypythongui import EasyFrame

class ThermometerView(EasyFrame):
    """A termperature conversion program."""

    def __init__(self, model):
        """Sets up the view.  The model comes in as an argument."""
        EasyFrame.__init__(self, title = "Temperature Converter")
        self.model = model

        # Label and field for Celsius
        self.addLabel(text = "Celsius", row = 0, column = 0)
        self.celsiusField = self.addFloatField(value = 
                                               model.getCelsius(),
                                               row = 1,
                                               column = 0,
                                               precision = 2)

        # Label and field for Fahrenheit
        self.addLabel(text = "Fahrenheit", row = 0, column = 1)
        self.fahrField = self.addFloatField(value =
                                            model.getFahrenheit(),
                                            row = 1,
                                            column = 1,
                                            precision = 2)

        # Celsius to Fahrenheit button
        self.addButton(text = ">>>>",
                       row = 2, column = 0,
                       command = self.computeFahr)
        # Fahrenheit to Celsius button
        self.addButton(text = "<<<<",
                       row = 2, column = 1,
                       command = self.computeCelsius)

    # The controller methods
    def computeFahr(self):
        """Inputs the Celsius degrees
        and outputs the Fahrenheit degrees."""
        degrees = self.celsiusField.getNumber()
        self.model.setCelsius(degrees)
        self.fahrField.setNumber(self.model.getFahrenheit())

    def computeCelsius(self):
        """Inputs the Fahrenheit degrees
        and outputs the Celsius degrees."""
        degrees = self.fahrField.getNumber()
        self.model.setFahrenheit(degrees)
        self.celsiusField.setNumber(self.model.getCelsius())

# Instantiate the model, pass it to the view, and pop up the window.
if __name__ == "__main__":
    model = Thermometer()
    view = ThermometerView(model)
    view.mainloop()       
