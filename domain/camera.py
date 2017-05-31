import random
import math
import operator
import numpy as np
from domain import point as Point, segment as Segment


class Camera:
    def __init__(self, problem, box):
        self.problem = problem
        self.box = box
        # generate random position within a box
        x = random.uniform(box.vertex.x, box.vertex.x + box.width)
        y = random.uniform(box.vertex.y, box.vertex.y + box.height)
        self.pos = Point.Point(x, y)

    def change_box(self, box):
        self.box = box
        # generate random position within a box
        x = random.uniform(box.vertex.x, box.vertex.x + box.width)
        y = random.uniform(box.vertex.y, box.vertex.y + box.height)
        self.pos = Point.Point(x, y)

    def modify_position(self):
        # generate random point until it is contained by at least one box
        x = np.random.normal(self.pos.x, self.problem.sigma)
        y = np.random.normal(self.pos.y, self.problem.sigma)
        p = Point.Point(x, y)
        while not p.is_in_box(self.problem):
            x = np.random.normal(self.pos.x, self.problem.sigma)
            y = np.random.normal(self.pos.y, self.problem.sigma)
            p = Point.Point(x, y)
        # point is within a box
        self.pos = p

    def can_reach(self, checkpoint):
        # check if checkpoint is in range of a camera and then try to pair intersection points
        distance = self.get_distance_to(checkpoint)
        if distance <= self.problem.camera_range:
            intersection_points = self.get_intersection_points(checkpoint)
            return self.can_pair_points(intersection_points)
        return False

    def get_distance_to(self, point):
        x_distance = self.pos.x - point.x
        y_distance = self.pos.y - point.y
        sum = x_distance**2 + y_distance**2
        return sum**.5

    def get_intersection_points(self, checkpoint):
        # segment between camera's position and checkpoint
        segment = Segment.Segment(self.pos, checkpoint)
        points = []
        for box in self.problem.boxes:
            points += segment.get_intersections_with(box)
        return points

    def can_pair_points(self, points):
        # check whether number of points is an even number
        if len(points) % 2 == 1:
            return False
        # sort points by x and y + try to pair
        points.sort(key=lambda p: (p.x, p.y))
        for i in range(0, len(points), 2):
            if points[i] != points[i+1]:
                return False
        # return True if all points are paired
        return True
