import math
import os

import arcade

import decay

decay.all()


with open('decay.py', 'r') as file:
    code = file.read()
    exec(code)


import subprocess

subprocess.call(['python', 'decay.py'])
