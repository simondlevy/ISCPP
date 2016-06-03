#!/usr/bin/env python3

"""
playalias.py : Illustrate time-domain aliasing with sound

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
from pygame import mixer
from time import sleep
from puretone import puretone

def playalias(analogfreq, sampfreq):

    playfreq = 8192*2
    dur      = 1
    A        = 0.5

    if sampfreq > playfreq:
       raise Exception('sampfreq must be less than %d Hz' % playfreq)

    samptimes = linspace(0, dur, sampfreq*dur)
    finetimes = linspace(0, dur, playfreq*dur)
    samps = A*sin(2*pi*analogfreq*samptimes)
    Pt = interp(finetimes, samptimes, samps)

    raw = (Pt*128 + 128).astype('byte').tostring()

    mixer.init(frequency=playfreq, size=8, channels=1)
    snd = mixer.Sound(raw)
    snd.play()
    sleep(1)

if __name__ == "__main__":
    """
    Example
    """
    playalias(1000, 15000)

    from pygame import mixer
    from time import sleep

    raw = puretone(440)
    mixer.init(frequency=10000, size=8, channels=1)
    snd = mixer.Sound(raw)
    snd.play()
    sleep(1) # Give the mixer enough time to play the sound




