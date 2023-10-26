# Webcam Television

Demonstrates

    roboflex (core)
    roboflex.webcam_uvc
    roboflex.visualization
    roboflex.transport.zmq
    roboflex.util.jpeg
    roboflex.profiler

The program: 

1. Creates a WebcamSensor, which is a roboflex node.
2. ... which signals to a JPEGCompressor, another node,
3. ... which signals to a ZMQPublisher, another node, which ultimately writes to a tcp socket...
4. Creates a ZMQSubscriber which to the publisher socket and reads jpeg-compressed camera frames.
5. ... which signals to a JPEGDecompressor
6. ... which signals to an RGBImageTV
7. Runs the entire graph through the 'profiler'.


## Install

    python3 -m venv pyvenv
    source pyvenv/bin/activate
    pip install --upgrade pip
    pip install wheel # <- shouldn't need in theory, but in this case, theory and practice differ...

    # either:
    pip install roboflex
    pip install roboflex.webcam_uvc
    pip install roboflex.visualization
    pip install roboflex.transport.zmq
    pip install roboflex.profiler
    pip install roboflex.util.jpeg

    # or:
    pip install -r requirements.txt

## Run

    # first, plug in a uvc-compatible (usb-connected, most likely) webcam, then:
    python webcam_tv.py
