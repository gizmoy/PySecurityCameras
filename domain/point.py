class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_in_box(self, problem):
        for box in problem.boxes:
            v = box.vertex
            if (v.x <= self.x <= v.x + box.width and
                v.y <= self.y <= v.y + box.height):
                return True
        return False
