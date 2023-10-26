# Realsense Television

Demonstrates

    roboflex (core)
    roboflex.realsense
    roboflex.visualization

The program: 

1. Creates a RealsenseSensor, which is a roboflex node.
2. ... which signals to an RGBImageTV, another node,
3. ... and to a DepthTV, another node


## Install

    python3 -m venv pyvenv
    source pyvenv/bin/activate
    pip install --upgrade pip
    pip install wheel # <- shouldn't need in theory, but in this case, theory and practice differ...

    # either:
    pip install roboflex
    pip install roboflex.realsense
    pip install roboflex.visualization

    # or:
    pip install -r requirements.txt

## Run

    # first, plug in a realsense camera, then:
    
    python realsense_tv.py
