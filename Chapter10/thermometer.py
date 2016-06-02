#!/usr/bin/env python3

"""
thermometer.py: Thermometer model class

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

class Thermometer(object):
    """Models temperature conversion between degrees Fahrenheit
    and degrees Celsius."""

    def __init__(self):
        """Sets up the model."""
        # Celsius is the standard
        self._degreesCelsius = 0.0

    def getCelsius(self):
        """Returns the Celsius temperature."""
        return self._degreesCelsius

    def setCelsius(self, degrees):
        """Sets the thermometer to degrees in Celsius."""
        self._degreesCelsius = degrees

    def getFahrenheit(self):
        """Returns the Fahrenheit temperature."""
        return self._degreesCelsius * 9 / 5 + 32

    def setFahrenheit(self, degrees):
        """Sets the thermometer to degrees in Fahrenheit."""
        self._degreesCelsius = (degrees - 32) * 5 / 9
