import sys
from roboflex import GraphRoot, MessagePrinter, Null
from roboflex.webcam_uvc import WebcamSensor, uvc_frame_format, get_device_list_string
from roboflex.visualization import RGBImageTV
from pan_tilt_velocity_controller import PanTiltController
from roboflex.transport.zmq import ZMQContext, ZMQPublisher, ZMQSubscriber
from roboflex.transport.mqtt import MQTTContext, MQTTPublisher
sys.path.append("./yoloface")
from facedetect import DetectorYoloFaceNode

# prints all uvc webcam devices
print(get_device_list_string())

# mqtt transport stuff - used to publish metrics
mqtt_context = MQTTContext()
metrics_pub = MQTTPublisher(mqtt_context, "localhost", 1883, "metrics")

# zmq transport stuff - used to public images to other threads
PUB_ADDRESS = "inproc://mycam"
zmq_context = ZMQContext()
pub = ZMQPublisher(zmq_context, PUB_ADDRESS, max_queued_msgs=1)
sub1 = ZMQSubscriber(zmq_context, PUB_ADDRESS, max_queued_msgs=1)
sub2 = ZMQSubscriber(zmq_context, PUB_ADDRESS, max_queued_msgs=1)

# create the graph root
gc = GraphRoot(metrics_pub)

# create the camera sensor node
# WIDTH=800
# HEIGHT=600
# FPS=20
# FORMAT=uvc_frame_format.UVC_FRAME_FORMAT_ANY
WIDTH=800
HEIGHT=600
FPS=60
FORMAT=uvc_frame_format.UVC_FRAME_FORMAT_MJPEG

webcam = WebcamSensor(
    width=WIDTH,
    height=HEIGHT,
    fps=FPS,
    device_index=1,
    format=FORMAT,
)
webcam.print_device_info()

# create the face detector node
face_detector = DetectorYoloFaceNode(HEIGHT, WIDTH)

#create the image viewer node
viewer = RGBImageTV(
    frequency_hz=24.0, 
    width=WIDTH, 
    height=HEIGHT, 
    image_key="rgb",
    mirror=True,
)

# create the dynamixel controller
pan_tilt_controller = PanTiltController(
    device_name='/dev/ttyUSB0', 
    baud_rate=2_000_000, 
    dxl_ids=[5,6],
)

# connect the graph
gc > webcam > face_detector > pub
gc > sub1 > viewer 
gc > sub2 > pan_tilt_controller > Null()

# run it all (profile it all)
gc.profile(node_to_run=viewer)
