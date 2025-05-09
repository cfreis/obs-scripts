#!/usr/bin/env python3

# Author: Clovis Reis
# Homepage: https://github.com/cfreis/obs-scripts
# License: GPLv3

''' 
This script is designed as a workaround to control OBS Studio running in a Wayland session.
It enables you to use a single shortcut to launch a simple Tkinter window that captures the next pressed key.
The captured key is then sent to OBS via a WebSocket connection.
This solution is based on the script originally created by Andrew Shark (https://gitlab.com/AndrewShark/obs-scripts)
'''

import obsws_python as obs
import tkinter as tk
from tkinter import messagebox

show_key = False #change for True to explore the key detected

def on_key_press(event):
    key = event.keysym
    if show_key:
        messagebox.showinfo("Key pressed", f"{key}")
    key = 'OBS_KEY_' + key.upper()
    try:
        cl = obs.ReqClient(host='localhost', port=4455, password='your_password', timeout=3)
        cl.trigger_hot_key_by_key_sequence(key)
    finally:
        root.quit()

root = tk.Tk()
root.title("")
root.geometry("0x0")
root.attributes('-alpha', 0.0)  # 100% transparent



root.bind('<Key>', on_key_press)
root.mainloop()

