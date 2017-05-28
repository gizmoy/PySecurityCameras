import random
import numpy as np
from domain import point


class Camera:
    def __init__(self, box):
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

    def modify_position(self, sigma):
        # for convenience
        v = self.box.vertex
        b = self.box

        # generate random x until it is within box
        pos_x = np.random.normal(self.pos.x, sigma)
        while pos_x < v.x or pos_x > v.x + b.width:
            pos_x = np.random.normal(self.pos.x, sigma)

        # generate random y until it is within box
        pos_y = np.random.normal(self.pos.y, sigma)
        while pos_y < v.y or pos_y > v.y + b.height:
            pos_y = np.random.normal(self.pos.y, sigma)

        # point is within box
        self.pos = point.Point(pos_x, pos_y)

