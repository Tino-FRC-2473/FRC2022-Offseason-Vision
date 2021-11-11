# Vision Input
Uses cv2 API

# Responsibilities:
* open/close the camera
* Return the camera video feed as images represented by ndarrays using the rgb channels
* Field of View
* Handle multiple cameras (threads)

## ImageGenerator
* Returns the image as an ndarray (with the rgb values)

## Video File Generator
* Returns the image that the camera sees (as a 2D or 3D arr)
* Captures video from a video file

## DepthDataGenerator
* Returns the depth array using the camera port directly

## Video Live Generator
* Returns current image frame 
* Captures video from the camera itself

## DepthLiveGenerator
Returns the depth array using an image file 

## CameraData
* Stores all the camera parameters (takes in a camera in constructor)
* Horizontal and Vertical FOV
* Camera tilt angle
* Screen Size 

### Methods
* getImageArr(): Returns rgb/yuv image ndarray
* getHorizFOV(): getVertFOV():Returns horizontal and vertical field of view
* getImage(): Returns the raw image from the camera feed

# Jetson

Involves a collection of shell scripts to run on the Jetson. run2022vision.sh is in the FRC2020-Vision repository and other setup/preparation scripts are in Jetson-Setup.

# Driver/testing file
* Runs the main program
* Tests if the camera methods work
