import time
import roboflex as rfc
import roboflex.realsense as rfr
import roboflex.visualization as rcv

config = rfr.Config(
    camera_type = rfr.camera_type_or([rfr.CameraType.RGB, rfr.CameraType.DEPTH, rfr.CameraType.IR1, rfr.CameraType.IR2]),
    align_to = rfr.CameraAlignment.RGB,
    rgb_settings = {"fps": 30, "width": 640, "height": 480},
    depth_settings = {"fps": 30, "width": 640, "height": 480},
)
sensor = rfr.RealsenseSensor("827112072758", config)

rgb_viewer = rcv.RGBImageTV(
    frequency_hz=24.0, 
    width=640, 
    height=480, 
    image_key="rgb",
    debug=False,
    mirror=True,
)
depth_viewer = rcv.DepthTV(
    frequency_hz=24.0, 
    width=640, 
    height=480, 
    image_key="depth",
    initial_pos=(650, 0),
    debug=False,
    mirror=True,
)
ir1_viewer = rcv.BlackAndWhiteTV(
    frequency_hz=24.0, 
    width=640, 
    height=480, 
    image_key="ir1",
    initial_pos=(0, 530),
    debug=False,
    mirror=True,
    name="IR1",
)
ir2_viewer = rcv.BlackAndWhiteTV(
    frequency_hz=24.0, 
    width=640, 
    height=480, 
    image_key="ir2",
    initial_pos=(650, 530),
    debug=False,
    mirror=True,
    name="IR2",
)

sensor > rgb_viewer
sensor > depth_viewer
sensor > ir1_viewer
sensor > ir2_viewer

sensor.start()
rgb_viewer.start()
depth_viewer.start()
ir1_viewer.start()
ir2_viewer.start()

time.sleep(10)
sensor.set_laser_on_off(False)
time.sleep(10)
sensor.set_laser_on_off(True)
time.sleep(10)

sensor.stop()
rgb_viewer.stop()
depth_viewer.stop()
ir1_viewer.stop()
ir2_viewer.stop()
