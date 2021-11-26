import cv2
import math
import random


class CameraData:
    def __init__(self):
        self.H_FIELD_OF_VIEW = 68.37
        self.V_FIELD_OF_VIEW = 41.21
        self.CAMERA_TILT = math.radians(30)

    def get_horiz_FOV(self):
        return self.H_FIELD_OF_VIEW

    def get_vert_FOV(self):
        return self.V_FIELD_OF_VIEW

    def get_camera_tilt(self):
        return self.CAMERA_TILT

    def convert_bgr_to_rgb(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    def convert_bgr_to_yuv(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
