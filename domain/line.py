class Line:
    def __init__(self, p1, p2):
        if p1.x == p2.x:
            self.a = (p1.y - p2.y) / 1e-7
            self.b = (p1.x * p2.y - p2.x * p1.y) / 1e-7
        else:
            self.a = (p1.y - p2.y) / (p1.x - p2.x)
            self.b = (p1.x * p2.y - p2.x * p1.y) / (p1.x - p2.x)

    def intersection(self, line):
        return [];