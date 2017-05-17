import random
from domain import point


class Camera:
    def __init__(self, box):
        self.box = box
        # generate random position within box
        pos_x = random.uniform(box.vertex.x, box.vertex.x + box.width)
        pos_y = random.uniform(box.vertex.y, box.vertex.y + box.height)
        self.pos = point.Point(pos_x, pos_y)
