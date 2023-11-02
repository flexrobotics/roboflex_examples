import roboflex.audio_sdl as ras
import roboflex.imgui as rgu

ras.AudioSensor.show_devices()

sensor = ras.AudioSensor(
    capture_id = -1,
    channels = 1,
    sampling_rate = 44100,
    capture_samples = 1024,
    format = ras.BitDepth.F32,
    name = "mysensor",
    data_key = "data",
    debug = True,
)

viewer = rgu.OneDTV(
    data_key = "data",
    sample_size = 4,
    center_zero = True,
    initial_size = (800, 120),
    initial_pos = (100, -1),
    name = "myviewer",
    debug = True,
)

sensor > viewer

sensor.start()

# will block until window closed
viewer.run()

sensor.stop()
