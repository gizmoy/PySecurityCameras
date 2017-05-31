import random
import math
import numpy as np
from domain import point as Point, line as Line


class Camera:
    def __init__(self, problem, box):
        self.problem = problem
        self.box = box
        # generate random position within box
        pos_x = random.uniform(box.vertex.x, box.vertex.x + box.width)
        pos_y = random.uniform(box.vertex.y, box.vertex.y + box.height)
        self.pos = Point.Point(pos_x, pos_y)

    def __str__(self):
        return 'Camera: {origin: %s}' % (str(self.pos))

    def change_box(self, box):
        self.box = box
        # generate random position within box
        pos_x = random.uniform(box.vertex.x, box.vertex.x + box.width)
        pos_y = random.uniform(box.vertex.y, box.vertex.y + box.height)
        self.pos = Point.Point(pos_x, pos_y)

    def modify_position(self):
        # generate random point until it is contained by at least one box
        pos_x = np.random.normal(self.pos.x, self.problem.sigma)
        pos_y = np.random.normal(self.pos.y, self.problem.sigma)
        p = Point.Point(pos_x, pos_y)
        while not p.is_in_box(self.problem):
            pos_x = np.random.normal(self.pos.x, self.problem.sigma)
            pos_y = np.random.normal(self.pos.y, self.problem.sigma)
            p = Point.Point(pos_x, pos_y)
        # point is within box
        self.pos = p

    def can_reach(self, check_point):
        distance = self.get_distance_to(check_point)
        if distance <= self.problem.camera_range:
            return True
            # intersection_points = self.get_intersection_points(check_point)
        return False

    def get_distance_to(self, point):
        x_distance = self.pos.x - point.x
        y_distance = self.pos.y - point.y
        sum = x_distance**2 + y_distance**2
        return sum**.5

    def get_intersection_points(self, check_point):
        # segment between camera's origin and check point
        segment = Line.Line(self.pos, check_point)
        points = []
        for box in self.problem.boxes:
            sides = box.get_sides()
            for side in sides:
                points += side.intersection(segment)
        return points
