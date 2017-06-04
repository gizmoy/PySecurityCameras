from point import Point


class Checkpoint(Point):
    def __init__(self, x, y, box):
        self.box = box
        self.is_observed = False
        Point.__init__(self, x, y)
