import cv2
from VideoFileGenerator import VideoFileGenerator as VFG
import ImageGenerator as IG

# run test code for VideoFileGenerator
test_video = VFG("/Users/arjunsudheer/Desktop/video_test_FRC.mp4")
next_video_frame, is_valid_frame = test_video.get_next_frame()
print(IG.get_image_channel(next_video_frame))
i = 0
while is_valid_frame:
    cv2.imwrite("original_saved_image_" + str(i) + ".jpg", next_video_frame)
    next_video_frame = cv2.cvtColor(next_video_frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite("saved_image_" + str(i) + ".jpg", next_video_frame)
    print(IG.get_pixel_channel(next_video_frame, 500 + i, 500 + i))
    next_video_frame, is_valid_frame = test_video.get_next_frame()
    i += 1
