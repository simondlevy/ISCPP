#!/usr/bin/env python3

"""
taxcalc.py : Tax calculator using terminal I/O

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

print("Tax Calculator\n")
income = float(input("Please enter your income: $"))
numDependents = float(input("Please enter the number of dependents: "))
exemptionAmount = float(input("Please enter the exemption amount: $"))
tax = (income - numDependents * exemptionAmount) * .15
print("Your total tax is $%0.2f" % tax)
