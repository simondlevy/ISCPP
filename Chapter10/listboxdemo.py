#!/usr/bin/env python3

"""
listboxdemo.py: Demonstrates list boxes in BreezyPythonGUI

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
from tkinter import END, NORMAL

class ListBoxDemo(EasyFrame):

    def __init__(self):

        """Sets up the window and widgets."""
        EasyFrame.__init__(self, "List Box Demo")
        
        # Set up the list box
        # Note the event-handling parameter for selecting a list item
        self.listBox = self.addListbox(row = 0, column = 0, rowspan = 4,
                                  listItemSelected = self.listItemSelected)
        # Add some items to the list box and select the first one
        self.listBox.insert(END, "Apple")
        self.listBox.insert(END, "Banana")
        self.listBox.insert(END, "Cherry")
        self.listBox.insert(END, "Orange")
        self.listBox.setSelectedIndex(0)

        # Set up the labels, fields, and buttons
        self.addLabel(text = "Input", row = 0, column = 1)
        self.addLabel(text = "Index", row = 1, column = 1)
        self.addLabel(text = "Current item", row = 2, column = 1)
        self.inputField = self.addTextField(text = "", row = 0,
                                            column = 2, width = 10)
        self.indexField = self.addIntegerField(value = "", row = 1,
                                               column = 2, width = 10)
        self.itemField = self.addTextField(text = "", row = 2,
                                           column = 2, width = 10)
        self.addButton(text = "Add", row = 3,
                       column = 1, command = self.add)
        self.removeButton = self.addButton(text = "Remove", row = 3,
                                           column = 2, command = self.remove)

        # Display current index and currently selected item
        self.listItemSelected(0)

    def listItemSelected(self, index):
        """Responds to the selection of an item in the list box.
        Updates the fields with the current item and its index."""
        self.indexField.setNumber(index)
        self.itemField.setText(self.listBox.getSelectedItem())

    def add(self):
        """If an input is present, insert it before the selected
        item in the list box.  The selected item remains current.
        If the first item is added, select it and enable the
        remove button."""
        item = self.inputField.getText()
        if item != "":
            index = self.listBox.getSelectedIndex()
            if index == -1:
                self.listBox.insert(0, item)
                self.listBox.setSelectedIndex(0)
                self.listItemSelected(0)
                self.removeButton["state"] = NORMAL
            else:
                self.listBox.insert(index, item)
                self.listItemSelected(index + 1)
            self.inputField.setText("")

    def remove(self):
        """If there are items in the list, remove
        the selected item, select previous one,
        and update the fields.  If there was no previous
        item, select the next one.  If the last item is
        removed, disable the remove button."""
        index = self.listBox.getSelectedIndex()
        self.listBox.delete(index)
        if self.listBox.size() > 0:
            if index > 0:
                index -= 1
            self.listBox.setSelectedIndex(index)
            self.listItemSelected(index)
        else:
            self.listItemSelected(-1)
            self.removeButton["state"] = DISABLED

ListBoxDemo().mainloop()
