#!/usr/bin/env python3
from time import sleep
import subprocess
import os

print("Subprocess demonstration by running the gui script for 5 seconds")

path = os.getcwd()

gui_command = ["python3", path + "/gui.py"]
gui_process = subprocess.Popen(
    gui_command,
    stdin=subprocess.PIPE
)

sleep(5)

gui_process.terminate()
print("Ran gui script for 5 seconds")
