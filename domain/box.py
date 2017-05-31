import copy
import math
from domain import point as Point, check_point as CheckPoint, segment as Segment


class Box:
    def __init__(self, vertex, width, height):
        self.vertex = vertex
        self.width = width
        self.height = height
        self.checkpoints = []

    def generate_checkpoints(self, distance):
        # count number of checkpoints on both axes
        num_check_points_on_x = int(math.floor(self.width  / distance + 1e-10))
        num_check_points_on_y = int(math.floor(self.height / distance + 1e-10))
        # biases for centering checkpoints on both axes
        x_bias = (self.width  - (num_check_points_on_x - 1) * distance) / 2
        y_bias = (self.height - (num_check_points_on_y - 1) * distance) / 2
        # generate checkpoints
        for i in xrange(num_check_points_on_x):
            for j in xrange(num_check_points_on_y):
                x = self.vertex.x + i * distance + x_bias
                y = self.vertex.y + j * distance + y_bias
                point = CheckPoint.CheckPoint(x, y, self)
                self.checkpoints.append(point)

    def get_vertex(self, key):
        # for readability
        v = self.vertex
        w = self.width
        h = self.height
        # create a particular vertex
        if key == 'bottom_left':
            vertex = Point.Point(v.x, v.y)
        elif key == 'upper_left':
            vertex = Point.Point(v.x, v.y + h)
        elif key == 'bottom_right':
            vertex = Point.Point(v.x + w, v.y)
        elif key == 'upper_right':
            vertex = Point.Point(v.x + w, v.y + h)
        else:
            vertex = None
        # return a particular vertex
        return vertex

    def get_sides(self):
        return {
            'left': Segment.Segment( # left side of box
                self.get_vertex('bottom_left'),
                self.get_vertex('upper_left')
            ),
            'right': Segment.Segment( # right side of box
                self.get_vertex('bottom_right'),
                self.get_vertex('upper_right')
            ),
            'bottom': Segment.Segment( # bottom side of box
                self.get_vertex('bottom_left'),
                self.get_vertex('bottom_right')
            ),
            'upper': Segment.Segment( # upper side of box
                self.get_vertex('upper_left'),
                self.get_vertex('upper_right')
            ),
        }
