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
        self.vertices = {
            'bo_lf': Point(vertex.x, vertex.y),  # bottom left vertex
            'up_lf': Point(vertex.x, vertex.y + height),  # upper left vertex
            'bo_rt': Point(vertex.x + width, vertex.y),  # bottom right vertex
            'up_rt': Point(vertex.x + width, vertex.y + height)  # upper right vertex
        }
        self.sides = {
            'lf': Segment(self.vertices['bo_lf'], self.vertices['up_lf']),  # left side of a box
            'rt': Segment(self.vertices['bo_rt'], self.vertices['up_rt']),  # right side of a box
            'bo': Segment(self.vertices['bo_lf'], self.vertices['bo_rt']),  # bottom side of a box
            'up': Segment(self.vertices['up_lf'], self.vertices['up_rt']),  # upper side of a box
        }

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
