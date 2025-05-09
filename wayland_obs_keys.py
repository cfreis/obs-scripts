#!/usr/bin/env python3

# Author: Clovis Reis
# Initial Homepage: https://github.com/cfreis/obs-scripts
# Homepage: https://github.com/uggla/obs-scripts
# License: GPLv3

# Changes Author: Uggla

"""
This script is designed as a workaround to control OBS Studio running in a
Wayland session.
It enables you to use a single shortcut to launch a simple Tkinter window
that captures the next pressed key.
The captured key is then sent to OBS via a WebSocket connection.
This solution is based on the script originally created by Andrew Shark
(https://gitlab.com/AndrewShark/obs-scripts)

Changes:
This script now loads secrets from a .env file.
"""

import obsws_python as obs
import os
import tkinter as tk

from tkinter import messagebox
from dotenv import load_dotenv

show_key = False
OBS_PASSWORD_VAR_NAME = "OBS_WEBSOCKET_PASSWORD"

load_dotenv()
OBS_PASSWORD = os.getenv(OBS_PASSWORD_VAR_NAME)

if not OBS_PASSWORD:
    print(f"Environment variable {OBS_PASSWORD_VAR_NAME} is not set.")
    exit(1)


def on_key_press(event):
    key = event.keysym
    if show_key:
        messagebox.showinfo("Key pressed", f"{key}")
    key = "OBS_KEY_" + key.upper()
    try:
        cl = obs.ReqClient(
            host="localhost", port=4455, password=OBS_PASSWORD, timeout=3
        )
        cl.trigger_hot_key_by_key_sequence(key)
    finally:
        root.quit()


root = tk.Tk()
root.title("")
root.geometry("0x0")
root.attributes("-alpha", 0.0)  # 100% transparent


root.bind("<Key>", on_key_press)
root.mainloop()
