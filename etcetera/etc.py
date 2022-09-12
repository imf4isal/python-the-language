import os
from ast import arguments
from glob import glob

import cowsay
import pyttsx3

engine = pyttsx3.init()

this = input("What's this? ")
cowsay.turtle(this)
engine.say(this)
engine.runAndWait()
