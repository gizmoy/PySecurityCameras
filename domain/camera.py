import random
import numpy as np
from domain import point


class Camera:
    def __init__(self, problem, box):
        self.problem = problem
        self.box = box
        # generate random position within box
        pos_x = random.uniform(box.vertex.x, box.vertex.x + box.width)
        pos_y = random.uniform(box.vertex.y, box.vertex.y + box.height)
        self.pos = point.Point(pos_x, pos_y)

    def __str__(self):
        return 'Camera: {origin: %s}' % (str(self.pos))

    def change_box(self, box):
        self.box = box
        # generate random position within box
        pos_x = random.uniform(box.vertex.x, box.vertex.x + box.width)
        pos_y = random.uniform(box.vertex.y, box.vertex.y + box.height)
        self.pos = point.Point(pos_x, pos_y)

    def modify_position(self):
        # generate random point until it is contained by at least one box
        pos_x = np.random.normal(self.pos.x, self.problem.sigma)
        pos_y = np.random.normal(self.pos.y, self.problem.sigma)
        p = point.Point(pos_x, pos_y)
        while not p.is_in_box(self.problem):
            pos_x = np.random.normal(self.pos.x, self.problem.sigma)
            pos_y = np.random.normal(self.pos.y, self.problem.sigma)
            p = point.Point(pos_x, pos_y)
        # point is within box
        self.pos = point.Point(pos_x, pos_y)

