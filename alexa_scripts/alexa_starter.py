#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 12:24:42 2018

@author: optimist2309
"""

import pyttsx3

# Creating instance for ttx speech engine
engine = pyttsx3.init()

# Setting the engine speed 
rate = engine.getProperty('rate')
engine.setProperty('rate' , 160)

# Text that need to say 
engine.say("Alexa Play Hindi Top Songs")

# Starting the engine
engine.runAndWait()