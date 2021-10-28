# Detection
Accurately detect any required target on the field

## Input
* RGB values of the image

## Responsibilities 
* Identify pixels that correspond to target
* Construct contours around targets
* Color calibration to correct for lighting changes

## Output
* Contours around objects of a certain color (cv2.findContours)

## Class structure 
* PowerPortDetector: returns the location of the power port
* PowerCellDetector: returns a tuple with a list of balls (each with [x, y, radius]) and the generator's depth frame

## API
* get_generator(): Returns the contained Generator
* run_detection(): Calls Generator.generate()

Returns tuple with:
* List of contours, one per target sorted by enclosed area
* Mask showing detected target




