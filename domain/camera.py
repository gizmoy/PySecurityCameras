import random
import math
import operator
import numpy as np
from point import Point
from vision_ray import VisionRay


class Camera:
    def __init__(self, problem, box):
        self.problem = problem
        self.box = box
        # generate random position within a box
        x = np.random.normal(box.vertex.x + box.width  / 2.0, problem.sigma)
        y = np.random.normal(box.vertex.y + box.height / 2.0, problem.sigma)
        p = Point(x, y)
        while not p.is_in_box(box):
            x = np.random.normal(box.vertex.x + box.width  / 2.0, problem.sigma)
            y = np.random.normal(box.vertex.y + box.height / 2.0, problem.sigma)
            p = Point(x, y)
        # point is within a box
        self.pos = p

    def modify_position(self):
        # generate random point until it is contained by at least one box
        x = np.random.normal(self.pos.x, self.problem.sigma)
        y = np.random.normal(self.pos.y, self.problem.sigma)
        p = Point(x, y)
        while not p.is_in_boxes(self.problem.boxes):
            x = np.random.normal(self.pos.x, self.problem.sigma)
            y = np.random.normal(self.pos.y, self.problem.sigma)
            p = Point(x, y)
        # point is within a box
        self.pos = p

    def can_reach(self, checkpoint):
        # check whether checkpoint is in range of a camera and then try to pair intersection points
        distance = self.get_distance_to(checkpoint)
        if distance <= self.problem.camera_range:
            intersection_points = self.get_intersection_points(checkpoint)
            return self.can_pair_points(intersection_points)
        return False

    def get_distance_to(self, point):
        # get euclidean distance
        x_distance = self.pos.x - point.x
        y_distance = self.pos.y - point.y
        sum = x_distance**2 + y_distance**2
        return sum**.5

    def get_intersection_points(self, checkpoint):
        # vision ray between camera's position point and checkpoint
        ray = VisionRay(self.pos, checkpoint, self)
        points = []
        for box in self.problem.boxes:
            points += ray.get_intersections_with(box)
        return points

    def can_pair_points(self, points):
        # check whether number of points is an even number
        if len(points) % 2 == 1:
            return False
        # sort points by x, y and try to pair
        points.sort(key=lambda p: (p.x, p.y))
        for i in range(0, len(points), 2):
            if points[i] != points[i+1]:
                return False
        # all points are paired
        return True
