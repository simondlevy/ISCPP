#!/usr/bin/env python3

"""
taxcodegui.py : Tax calculator using a dialog box

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

class TaxCodeDemo(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Tax Calculator")

        # Label and field for the income
        self.addLabel(text = "Income",
                      row = 0, column = 0)
        self.incomeField = self.addFloatField(value = 0.0,
                                              row = 0,
                                              column = 1)

        # Label and field for the number of dependents
        self.addLabel(text = "Dependents",
                      row = 1, column = 0)
        self.depField = self.addIntegerField(value = 0,
                                             row = 1,
                                             column = 1)

        # Label and field for the exemption amount
        self.addLabel(text = "Exemption amount",
                      row = 2, column = 0)
        self.exeField = self.addFloatField(value = 0.0,
                                           row = 2,
                                           column = 1)
        # The command button
        self.button = self.addButton(text = "Compute",
                                     row = 3, column = 0,
                                     columnspan = 2,
                                     command = self.computeTax)

        # Label and field for the tax
        self.addLabel(text = "Total tax",
                      row = 4, column = 0)
        self.taxField = self.addFloatField(value = 0.0,
                                           row = 4,
                                           column = 1,
                                           precision = 2)

    # The event handling method for the button
    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field."""
        income = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()
        exemptionAmount = self.exeField.getNumber()
        tax = (income - numDependents * exemptionAmount) * .15
        self.taxField.setNumber(tax)
        
       
#Instantiate and pop up the window.
TaxCodeDemo().mainloop()
