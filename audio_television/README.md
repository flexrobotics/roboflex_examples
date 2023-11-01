# Audio Television

Demonstrates

    roboflex (core)
    roboflex.audio_sdl
    roboflex.imgui

The program: 

1. Creates an AudioSensor, which is a roboflex node. It will use SDL to listen to a microphone, and broadcast tensors containing the data.
2. Creates a OneDTV node, which displays the incoming audio data.


## Install

    python3 -m venv pyvenv
    source pyvenv/bin/activate
    pip install --upgrade pip
    pip install wheel # <- shouldn't need in theory, but in this case, theory and practice differ...

    # either:
    pip install roboflex
    pip install roboflex.audio_sdl
    pip install roboflex.imgui

    # or:
    pip install -r requirements.txt

## Run

    # You need to have a microphone that SDL can access.
    python audio_tv.py
