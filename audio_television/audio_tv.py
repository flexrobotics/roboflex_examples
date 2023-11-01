import time
import roboflex as rcc
import roboflex.audio_sdl as ras
import roboflex.imgui as rgu

sensor = ras.AudioSensor(
    capture_id = -1,
    channels = 1,
    sampling_rate = 44100,
    capture_samples = 512,
    format = ras.BitDepth.F32,
    name = "mysensor",
    data_key = "data",
    debug = False,
)

viewer = rgu.OneDTV(
    data_key = "data",
    sample_size = 4,
    center_zero = True,
    initial_size = (800, 120),
    initial_pos = (100, -1),
    name = "myviewer",
    debug = False,
)

sensor > viewer

sensor.start()
viewer.start()

time.sleep(10000)

sensor.stop()
viewer.stop()