#!/usr/bin/env python3

"""
thermometerview2.py: Second view of our thermometer class

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
from thermometer import Thermometer

class ThermometerView(EasyFrame):
    """A temperature conversion program.  Uses sliding scales."""

    def __init__(self, model):
        """Sets up the view.  The model comes in as an argument."""
        EasyFrame.__init__(self, title = "Temperature Converter")
        self.model = model
        # Sliding scale for Celsius
        self.celsiusScale = self.addScale(label = "Celsius",
                                          row = 0, column = 0,
                                          from_ = -273.15, to = 100.0,
                                          resolution = 0.01,
                                          length = 250,
                                          tickinterval = 0,
                                          command = self.computeFahr)
        self.celsiusScale.set(model.getCelsius())

        # Sliding scale for Fahrenheit
        self.fahrScale = self.addScale(label = "Fahernheit",
                                       row = 1, column = 0,
                                       from_ = -459.67, to = 212.0,
                                       resolution = 0.01,
                                       length = 250,
                                       tickinterval = 0,
                                       command = self.computeCelsius)
        self.fahrScale.set(model.getFahrenheit())

    # The controller methods
    def computeFahr(self, degreesCelsius):
        """Inputs the Celsius degrees
        and outputs the Fahrenheit degrees."""
        degrees = float(degreesCelsius)
        self.model.setCelsius(degrees)
        self.fahrScale.set(self.model.getFahrenheit())

    def computeCelsius(self, degreesFahrenheit):
        """Inputs the Fahrenheit degrees
        and outputs the Celsius degrees."""
        degrees = float(degreesFahrenheit)
        self.model.setFahrenheit(degrees)
        self.celsiusScale.set(self.model.getCelsius())

# Instantiate the model, pass it to the view, and pop up the window.
if __name__ == "__main__":
    model = Thermometer()
    view = ThermometerView(model)
    view.mainloop()
