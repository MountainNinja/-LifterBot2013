from sr import *


# nearest_cube_directions returns a Directions object
# which contains information about the directions the
# robot should take to reach the nearest cube.
#
# Directions objects contain:
# - bearing  :  Bearing in degrees (clockwise, from the direction the camera is facing)
# - distance :  Direct distance in metres
# - x        :  Distance to move in the X axis (forwards, I think)
# - y        :  Distance to move in the Y axis (to the left or right, I think)


class Directions:
    bearing = 0
    distance = 0
    x = 0
    y = 0
    def __init__(self, cube_marker):
        self.distance = cube_marker.dist
        bearing = cube_marker.rot_y
        x = cube_marker.centre.world.x
        y = cube_marker.centre.world.y


def nearest_cube_directions(cube_list):
    if len(cube_list) == 0:
        return None
    nearest_cube = sorted(l, key=lambda marker:marker.dist)[0]
    return Directions(nearest_cube)
