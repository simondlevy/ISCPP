#!/usr/bin/env python3

"""
puretone.py : Return a playable pure sine-wave tone at a specified frequency

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

def puretone(f, A=1.0, dur=1.0, fs=10000):
    t = linspace(0, dur, dur*fs)
    Pt = A * sin(2*pi*f*t)
    raw = (Pt*128 + 128).astype("byte").tostring()
    return raw

if __name__ == "__main__":
    """
    Example with audio
    """

    from pygame import mixer
    from time import sleep

    raw = puretone(440)
    mixer.init(frequency=10000, size=8, channels=1)
    snd = mixer.Sound(raw)
    snd.play()
    sleep(1) # Give the mixer enough time to play the sound


