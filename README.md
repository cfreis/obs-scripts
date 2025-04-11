# OBS wayland shortcuts workaround

Currently in Wayland sessions, OBS Studio shortcuts can only be triggered when the window has focus. To work around this limitation, I've implemented an kludge solution while we await proper system-level fixes.

It is based on a Andrew Shark's original concept (https://gitlab.com/AndrewShark/obs-scripts), using a KDE global shortcut to execute a Python application. The program monitors keyboard input for the next keypress, forwards it as a hotkey command to OBS Studio through the obs-websocket plugin interface and quit.

This task are made from the Python script wayland_obs_keys.py

## Installation Guide

### OBS Studio setup
1. Launch OBS Studio;
2. Configure WebSocket Server:
* Navigate to Tools > WebSocket Server Settings;
* Enable WebSocket server;
* Security (recommended):
    * Set a password and copy it for later use.
3. Click Apply to save settings.

### Clone the repository
1. Clone this repository to your local machine;
2. Open wayland_obs_keys.py;
3. Update the WebSocket connection line:
* cl = obs.ReqClient(host='localhost', port=4455, password='***your_password***', timeout=3);
* Replace ***your_password*** with your actual OBS WebSocket password (keep the quotes).

### Configure a KDE Shortcut
1. Open KDE System Settings > Shortcuts
2. Click the "Add Command" button
3. Enter the full path to the script (e.g., /path/to/wayland_obs_keys.py)
4. Click "Add" to confirm
5. Set Your Shortcut:
* Click "Add Custom Shortcut"
* Press your desired key combination (e.g., Meta+Z)
* Click "Apply" to save

### Usage
1. Launch OBS Studio
   Ensure OBS is running with the WebSocket server enabled.

2. Trigger a Command 
   - Press your configured KDE shortcut (e.g. `Meta+Z`) 
   - Immediately press the OBS hotkey you want to execute 
   - The associated OBS action will trigger if configured correctly

3. Next Command 
   Repeat the process for additional hotkeys.
