import copy
import math
from domain import check_point as CheckPoint, line as Line


class Box:
    def __init__(self, vertex, width, height):
        self.vertex = vertex
        self.width = width
        self.height = height
        self.check_points = []

    def __str__(self):
        return 'Box: {bottom left vertex: (%s), width: %f, height: %f}' % (str(self.vertex), self.width, self.height)

    def __eq__(self, other):
        return self.vertex == other.vertex and self.height == other.height and self.height == other.height

    def generate_check_points(self, distance):
        # count number of check points on both axes
        num_check_points_on_x = int(math.floor(self.width  / distance + 1e-10))
        num_check_points_on_y = int(math.floor(self.height / distance + 1e-10))
        # biases for centering check points on both axes
        x_bias = (self.width  - (num_check_points_on_x - 1) * distance) / 2
        y_bias = (self.height - (num_check_points_on_y - 1) * distance) / 2
        # generate check points
        for i in xrange(num_check_points_on_x):
            for j in xrange(num_check_points_on_y):
                x = self.vertex.x + i * distance + x_bias
                y = self.vertex.y + j * distance + y_bias
                point = CheckPoint.CheckPoint(x, y, self)
                self.check_points.append(point)

    def get_vertex(self, key):
        vertex = copy.copy(self.vertex)
        if key == 'bottom_left':
            pass
        elif key == 'bottom_right':
            vertex.x + self.width
        elif key == 'upper_left':
            vertex.y + self.height
        elif key == 'upper_right':
            vertex.x + self.width
            vertex.y + self.height
        else:
            vertex = None
        return vertex

    def get_sides(self):
        return [
            Line.Line( # left side of box
                self.get_vertex('bottom_left'),
                self.get_vertex('upper_left')
            ),
            Line.Line( # bottom side of box
                self.get_vertex('bottom_left'),
                self.get_vertex('bottom_right')
            ),
            Line.Line(  # upper side of box
                self.get_vertex('upper_left'),
                self.get_vertex('upper_right')
            ),
            Line.Line(  # right side of box
                self.get_vertex('bottom_right'),
                self.get_vertex('upper_right')
            )
        ]
