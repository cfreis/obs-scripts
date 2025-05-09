#!/bin/bash

cd "$HOME/obs-scripts" || exit 1

OBS_PLUGINS_PATH=/usr/local/lib64/obs-plugins OBS_PLUGINS_DATA_PATH=/usr/local/share/obs/obs-plugins obs
