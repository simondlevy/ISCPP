# plotsunspots.py : plot sunspot data from spreadsheet
#
# Simon D. Levy   CSCI 121  Winter 2016

# These packages will do most of our work for us
from numpy import *
from matplotlib.pyplot import *

# Load the sunspot data into a NumPy array
a = loadtxt("sunspots-no-header.csv", delimiter=",")

# The first column is the year
year = a[:,0]

# The second column in the month
month = a[:,1]

# The third column is the sunspots
spots = a[:,2]

# Compute the date
time = year + (month - .5) / 12

# Build the plot 
plot(time, spots)

# Add annotations
xlabel('Year')
ylabel('# of Sunspots')
title('Sunspot Counts')

# Show it!
show()
