import cv2
from VideoFileGenerator import VideoFileGenerator as VFG
from CameraData import CameraData
import ImageGenerator as IG

CD = CameraData()

# run test code for VideoFileGenerator
test_video = VFG("/Users/arjunsudheer/Desktop/video_test_FRC.mp4")
next_video_frame, is_valid_frame = test_video.get_next_frame()
print(IG.get_image_rgb(next_video_frame))
i = 0
while is_valid_frame:
    cv2.imwrite("saved_image_" + str(i) + ".jpg", next_video_frame)
    cv2.imwrite("original_saved_image_" + str(i) + ".jpg", CD.convert_bgr_to_rgb(next_video_frame))
    print(CD.convert_bgr_to_rgb(next_video_frame))
    print(IG.get_pixel_rgb(next_video_frame, 500 + i, 500 + i))
    next_video_frame, is_valid_frame = test_video.get_next_frame()
    i += 1
