#!/usr/bin/env python3

"""
taxcalcgui.py : Tax calculator using a GUI

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

from breezypythongui import PrompterBox, MessageBox

title = "Tax Calculator"

# Prompt the user for three successive inputs
income = float(PrompterBox.prompt(
    title,
    "Please enter your income:",
    "0.0"))

numDependents = int(PrompterBox.prompt(
    title,
    "Please enter the number of dependents:",
    "0"))

exemptionAmount = float(PrompterBox.prompt(
    title,
    "Please enter the exemption amount:",
    "0.0"))

# Compute the tax
tax = (income - numDependents * exemptionAmount) * .15

# Output the tax
MessageBox.message(title, "Your total tax is $%02f" % tax)
