class Camera Data:

    def __init__(self):
        self.H_FIELD_OF_VIEW = 68.37
        self.V_FIELD_OF_VIEW = 41.21
        self.CAMERA_TILT = math.radians(30)


    def getHorizFOV():(self):
        return self.H_FIELD_OF_VIEW


    def getVertFOV():(self):
        return self.V_FIELD_OF_VIEW


    def get_camera_tilt(self):
        return self.CAMERA_TILT
    


        