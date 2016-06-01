#!/usr/bin/env python3

"""
menudemo.py: Demonstrates a simple menu using BreezyPythonGUI

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

from breezypythongui import EasyFrame, END

class MenuDemo(EasyFrame):
    """Displays the name of the selected menu item."""
    
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "Menu Demo")
        
        # Add the menu bar for the two menus
        menuBar = self.addMenuBar(row = 0, column = 0, columnspan = 2)
        
        # Add the File menu
        fileMenu = menuBar.addMenu("File")
        
        # Add the command options for the File menu
        newMenuCommand = fileMenu.addMenuItem("New",  self.newSelected)
        openMenuCommand = fileMenu.addMenuItem("Open", self.openSelected)
        saveMenuCommand = fileMenu.addMenuItem("Save", self.saveSelected)
        
        # Add the Edit menu
        editMenu = menuBar.addMenu("Edit")
        
        # Add the command options for the Edit menu
        copyMenuCommand = editMenu.addMenuItem("Copy",  self.copySelected)
        cutMenuCommand = editMenu.addMenuItem("Cut",   self.cutSelected)
        pasteMenuCommand = editMenu.addMenuItem("Paste", self.pasteSelected)
        
        # Output field for the results
        self.output = self.addTextField("", row = 1, column = 0)

    # Event handlers for menu commands

    def newSelected(self):
        self.output.setText("New")
        
    def openSelected(self):
        self.output.setText("Open")

    def saveSelected(self):
        self.output.setText("Save")

    def copySelected(self):
        self.output.setText("Copy")

    def cutSelected(self):
        self.output.setText("Cut")

    def pasteSelected(self):
        self.output.setText("Paste")
        

# Instantiate and pop up the window."""
MenuDemo().mainloop()
