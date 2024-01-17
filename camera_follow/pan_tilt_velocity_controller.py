import roboflex.dynamixel as rxd

class PanTiltController(rxd.DynamixelGroupControllerNode):

    def __init__(self, device_name, baud_rate, dxl_ids, pantilt_speed=50.0):
        super().__init__(
            rxd.DynamixelGroupController.VelocityController(
                device_name=device_name,
                baud_rate=baud_rate,
                dxl_ids=dxl_ids,
            ),
            "pantiltcontroller")
        self.pantilt_speed = pantilt_speed

    def readwrite_loop_function(self, state, last_msg):
        if last_msg:
            x = last_msg["x"]
            y = last_msg["y"]
        else:
            x = y = 0.5

        if x == -1 and y == -1:
            x = y = 0.5

        dx = x - 0.5
        dy = y - 0.5
        speedx = abs(dx) * self.pantilt_speed
        speedy = abs(dy) * self.pantilt_speed
        dir_x = -1 if dx > 0 else 1
        dir_y = 1 if dy > 0 else -1
        vel_x = int(dir_x * speedx)
        vel_y = int(dir_y * speedy)

        return {
            5: {rxd.DXLControlTable.GoalVelocity: vel_x},
            6: {rxd.DXLControlTable.GoalVelocity: vel_y},
        }



# keep around for a bit... I re-architected to the above, didn't like this approach...
# class PanTiltController(rxd.DynamixelRemoteController):

#     def __init__(self, pantilt_speed = 50.0):
#         super().__init__("pantiltcontroller")
#         self.pantilt_speed = pantilt_speed
#         self.target_x = None
#         self.target_y = None
#         self.lock = threading.Lock()
#         self.t0 = 0

#     def receive(self, m):
#         keys = m.keys()
#         if "x" in keys and "y" in keys:
#             with self.lock:
#                 self.target_x = m["x"]
#                 self.target_y = m["y"]
#         else:
#             super().receive(m)

#     def readwrite_loop_function(self, state):
#         if self.t0 == 0:
#             self.t0 = time.time()

#         with self.lock:
#             x = self.target_x
#             y = self.target_y
            
#         if x is None or y is None or ((time.time() - self.t0) < 3.0):
#             x = y = 0.5
            
#         dx = x - 0.5
#         dy = y - 0.5
#         speedx = abs(dx) * self.pantilt_speed
#         speedy = abs(dy) * self.pantilt_speed
#         dir_x = -1 if dx > 0 else 1
#         dir_y = 1 if dy > 0 else -1
#         vel_x = int(dir_x * speedx)
#         vel_y = int(dir_y * speedy)
#         return {
#             5: {rxd.DXLControlTable.GoalVelocity: vel_x},
#             6: {rxd.DXLControlTable.GoalVelocity: vel_y},
#         }


# def get_pan_tilt_pair():
#     pan_tilt_controller = PanTiltController()

#     dynamixel_node = rxd.DynamixelGroupNode(
#         controller = rxd.DynamixelGroupController.VelocityController(
#             device_name='/dev/ttyUSB0',
#             baud_rate=3_000_000,
#             dxl_ids=[5,6],
#         ),
#     )

#     dynamixel_node > pan_tilt_controller
#     pan_tilt_controller > dynamixel_node

#     return dynamixel_node, pan_tilt_controller


