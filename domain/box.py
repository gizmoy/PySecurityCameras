import copy
import math
from point import Point
from check_point import Checkpoint
from segment import Segment


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
                point = Checkpoint(x, y, self)
                self.checkpoints.append(point)

    def get_vertex(self, key):
        # for readability
        v = self.vertex
        w = self.width
        h = self.height
        # create a particular vertex
        if key == 'bo_lf':
            vertex = Point(v.x, v.y)
        elif key == 'up_lf':
            vertex = Point(v.x, v.y + h)
        elif key == 'bo_rt':
            vertex = Point(v.x + w, v.y)
        elif key == 'up_rt':
            vertex = Point(v.x + w, v.y + h)
        else:
            vertex = None
        # return a particular vertex
        return vertex

    def get_sides(self):
        return {
            'lf': Segment(  # left side of box
                self.get_vertex('bo_lf'),
                self.get_vertex('up_lf')
            ),
            'rt': Segment(  # right side of box
                self.get_vertex('bo_rt'),
                self.get_vertex('up_rt')
            ),
            'bo': Segment(  # bottom side of box
                self.get_vertex('bo_lf'),
                self.get_vertex('bo_rt')
            ),
            'up': Segment(  # upper side of box
                self.get_vertex('up_lf'),
                self.get_vertex('up_rt')
            ),
        }
