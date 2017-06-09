class Segment:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # compute line equation's params
        epsilon = 1e-8
        if p1.x == p2.x:
            self.a = (p1.y - p2.y) / epsilon
            self.b = (p1.x * p2.y - p2.x * p1.y) / epsilon
        else:
            self.a = (p1.y - p2.y) / (p1.x - p2.x)
            self.b = (p1.x * p2.y - p2.x * p1.y) / (p1.x - p2.x)
        # compare coords of two segment's ending points
        self.x_lo = self.p1.x if self.p1.x <= self.p2.x else self.p2.x
        self.x_hi = self.p1.x if self.p1.x >= self.p2.x else self.p2.x
        self.y_lo = self.p1.y if self.p1.y <= self.p2.y else self.p2.y
        self.y_hi = self.p1.y if self.p1.y >= self.p2.y else self.p2.y

    def get_x_for(self, y):
        return (y - self.b) / self.a

    def get_y_for(self, x):
        return self.a * x + self.b