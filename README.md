# OBS wayland shortcuts workaround

Currently (august 2023) it is not possible to set shortcuts in obs when you are in Wayland session. This project may be used to workaround the problem.
This probably will be not needed after OBS implements GlobalShortcuts portal. See https://ideas.obsproject.com/posts/2066/implement-globalshortcuts-portal and https://invent.kde.org/plasma/xdg-desktop-portal-kde/-/merge_requests/80.

The idea of workaround is to use kde global shortcuts, that are running a command. This command is a script, which tells obs what to do. It works via obs-websocket plugin (usually built-in).

This repository contains the following sctipt:  
- recording-toggle.py - script that allows you to use a single shortcut to trigger start, then pause/unpause recording.

## Reqirements

Install the following packages (Arch Linux names of packages):  
- obs-studio-git (because currently the obs-studio package misses the websocket plugin, see Arch Wiki).

## Installation and configuration
Clone this repository to the folder when it is comfortable for you to keep it. For example, in `~/Development/obs-scripts`  

Go to kde System Settings, Shortcuts. Click the "Add Command" button.  
Paste (or pick) the path to the script. In my example it will be `/home/andrey/Development/obs-scripts/obs-wayland-shortcuts/recording-toggle.py`, then press "Add".  
Then press "Add custom shortcut", and press the desired shortcut. For example, I will use `Meta+X`. Then press "Apply".  

### Configure for Logitech Options
For Logitech mice, use logid configs to bind keypresses to mouse gestures. Then configure as normal, but draw a gesture when specifying shortcut.

## Usage
Open obs. Minimize it. Prepare for recording. Press the shortcut (Meta+X in my case). You see in tray that obs started recording. Press Meta+X again. You see that obs paused recording. Press shortcut again. You see that obs resumed recording. Unminimize obs window. Stop recording manually by hitting the stop recording button.

# Development
Protocol reference is here:  
https://github.com/obsproject/obs-websocket/blob/master/docs/generated/protocol.md
