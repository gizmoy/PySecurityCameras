class CheckPoint:
    def __init__(self, x, y, box):
        self.x = x
        self.y = y
        self.box = box
        self.is_observed = False

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)
