#!/usr/bin/env python3

"""
equalize.py : Simulated color restoration through histogram equalization

Copyright (C) Simon D. Levy 2016

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

from numpy import *

def equalize(im, mixture=1):
    '''
    histogram equalization of an image plane
    im -- the image: a single plane
    mixture -- optional, mix the equalized and 
    original with this proportion of the original
    '''

    imflat = im.flatten()

    index = argsort(imflat)

    n = len(imflat)
    
    imflat[index] = arange(n)/n
    imflat = mixture*imflat + (1-mixture)*im.flatten()

    return reshape(imflat, im.shape)
    
from matplotlib.pyplot import *
from matplotlib import cm
mona = imread('monaLisaLouvre.png')
subplot(1,2,1)
imshow(mona)
gca().axes.get_xaxis().set_visible(False)
gca().axes.get_yaxis().set_visible(False)
subplot(1,2,2)
red = mona[:,:,0]
green = mona[:,:,1]
blue = mona[:,:,2]
gca().axes.get_xaxis().set_visible(False)
gca().axes.get_yaxis().set_visible(False)
fig=imshow(dstack((equalize(red,.25), equalize(green,.25), equalize(blue,.5))))
axis('off')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
show()
