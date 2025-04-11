# OBS wayland shortcuts workaround

Currently in Wayland sessions, OBS Studio shortcuts can only be triggered when the window has focus. To work around this limitation, I've implemented a kludge solution while we await proper system-level fixes.

It is based on a Andrew Shark's original concept (https://gitlab.com/AndrewShark/obs-scripts), using a KDE global shortcut to execute a Python application. The program monitors keyboard input for the next keypress, forwards it as a hotkey command to OBS Studio through the obs-websocket plugin interface and quit.

This task are made from the Python script `wayland_obs_keys.py`

## Installation Guide

### OBS Studio setup
1. Launch OBS Studio;
2. Configure WebSocket Server:
    * Navigate to Tools > WebSocket Server Settings;
    * Enable WebSocket server;
    * Security (recommended):
        * Set a password and copy it for later use.
3. Click Apply to save settings;
4. Create the desired hotkeys in File > Setup > Hotkeys menu.

### Clone the repository
1. Clone this repository to your local machine;
2. Open wayland_obs_keys.py;
3. Update the WebSocket connection line:

    `cl = obs.ReqClient(host='localhost', port=4455, password='your_password', timeout=3);`
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

3. Repeat the process for additional hotkeys.


### List of Supported Keys

The following key values are accepted by the WebSocket function:

`cl.trigger_hot_key_by_key_sequence(key)`

To show the exact name of the pressed key, change the script `wayland_obs_keys.py` line from

`show_key = False  # Change to 'True' to enable key name display`


| **LETTERS** | **LETTERS** | **NUMBERS** | **F KEYS** |
| ---------- | ---------- | ---------- | ---------- |
| OBS_KEY_A | OBS_KEY_N | OBS_KEY_0 | OBS_KEY_F1 |
| OBS_KEY_B | OBS_KEY_O | OBS_KEY_1 | OBS_KEY_F2 |
| OBS_KEY_C | OBS_KEY_P | OBS_KEY_2 | OBS_KEY_F3 |
| OBS_KEY_D | OBS_KEY_Q | OBS_KEY_3 | OBS_KEY_F4 |
| OBS_KEY_E | OBS_KEY_R | OBS_KEY_4 | OBS_KEY_F5 |
| OBS_KEY_F | OBS_KEY_S | OBS_KEY_5 | OBS_KEY_F6 |
| OBS_KEY_G | OBS_KEY_T | OBS_KEY_6 | OBS_KEY_F7 |
| OBS_KEY_H | OBS_KEY_U | OBS_KEY_7 | OBS_KEY_F8 |
| OBS_KEY_I | OBS_KEY_V | OBS_KEY_8 | OBS_KEY_F9 |
| OBS_KEY_J | OBS_KEY_W | OBS_KEY_9 | OBS_KEY_F10 |
| OBS_KEY_K | OBS_KEY_X |  | OBS_KEY_F11 |
| OBS_KEY_L | OBS_KEY_Y |  | OBS_KEY_F12 |
| OBS_KEY_M | OBS_KEY_Z |  |  |

Other keys can be used as long as they can be typed with a single stroke. Combinations of two keys (e.g., `<Ctrl>+<C>`) will not be detected.

| **OTHERS** | **OTHERS** | **OTHERS** | **OTHERS** |
| ---------- | ---------- | ---------- | ---------- |
| OBS_KEY_LEFT | OBS_KEY_NUM0 | OBS_KEY_HOME | OBS_KEY_ASTERISK |
| OBS_KEY_UP | OBS_KEY_NUM1 | OBS_KEY_END | OBS_KEY_PLUS |
| OBS_KEY_RIGHT | OBS_KEY_NUM2 | OBS_KEY_NUMEQUAL | OBS_KEY_COMMA |
| OBS_KEY_DOWN | OBS_KEY_NUM3 | OBS_KEY_NUMASTERISK | OBS_KEY_MINUS |
| OBS_KEY_PAGEUP | OBS_KEY_NUM4 | OBS_KEY_NUMPLUS | OBS_KEY_PERIOD |
| OBS_KEY_PAGEDOWN | OBS_KEY_NUM5 | OBS_KEY_NUMCOMMA | OBS_KEY_SLASH |
| OBS_KEY_SHIFT | OBS_KEY_NUM6 | OBS_KEY_NUMMINUS | OBS_KEY_INSERT |
| OBS_KEY_CONTROL | OBS_KEY_NUM7 | OBS_KEY_NUMPERIOD | OBS_KEY_DELETE |
| OBS_KEY_META | OBS_KEY_NUM8 | OBS_KEY_NUMSLASH | OBS_KEY_PAUSE |
| OBS_KEY_ALT | OBS_KEY_NUM9 | OBS_KEY_CLEAR | OBS_KEY_PRINT |
| OBS_KEY_ALTGR | OBS_KEY_SPACE | OBS_KEY_PERCENT | OBS_KEY_SYSREQ |
| OBS_KEY_CAPSLOCK | OBS_KEY_ENTER | OBS_KEY_APOSTROPHE | OBS_KEY_EXCLAM |
| OBS_KEY_NUMLOCK | OBS_KEY_ESCAPE | OBS_KEY_SCROLLLOCK | OBS_KEY_DOLLAR |
| OBS_KEY_TAB | OBS_KEY_BACKSPACE | OBS_KEY_AT |  |

See the full key list [here][1].

[1]: https://github.com/obsproject/obs-studio/blob/master/libobs/obs-hotkeys.h
