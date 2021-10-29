# Circle Localization
Accurately locate a given target on the field.

## Responsibilities
* Use inputted images to detect circles
* Create contours on those circles
* Calculate distance from robot camera to the circle (ball)
* Collaborating with other CV subteams (hardware?)
* Locate the target (if time permits)

## Class Structure
One class for each different target and a class to find the distance. (More to be added for future targets)
1. BallDetector (used to detect the ball)
2. DistanceDetector (used to calculate the distance)

## API
`calculate_distance()`

Calculates the distance between the camera and the generated image. Returns a tuple of (distance_x, distance_y).

`get_generator()`

Returns the contained generator from input

`run_detection()`

Implements Helper methods to help detect the target object

### Possible improvements from last year:
- [ ] Decrease the use of hard coded values
- [ ] Better edge detection for circles
- [ ] Improve accuracy of distance calculated
- [ ] Train and deploy better ML models, gain better input data to work with
- [ ] Use in person roboshack to test the code better.
- [ ] Play around and see if we can apply it to other objects on the field.
- [ ] If time permits, try detecting the targets


