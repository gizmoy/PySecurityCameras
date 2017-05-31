from domain import point as Point


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
        self.x_lo = self.p1.x if self.p1.x < self.p2.x else self.p2.x
        self.x_hi = self.p1.x if self.p1.x > self.p2.x else self.p2.x
        self.y_lo = self.p1.y if self.p1.y < self.p2.y else self.p2.y
        self.y_hi = self.p1.y if self.p1.y > self.p2.y else self.p2.y

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_intersections_with(self, box):
        # intersection points
        intersection_points = []
        # for readability
        x_lo = self.x_lo
        x_hi = self.x_hi
        y_lo = self.y_lo
        y_hi = self.y_hi
        # iterate over sides and depending on its type check whether it intersects with a segment
        for name, side in box.get_sides().iteritems():
            p1 = side.p1
            p2 = side.p2
            # separate into vertical and horizontal sides
            if name == 'left' or name == 'right':
                # check whether left or right side are between two segment's ending points
                x_side = p1.x if name == 'left' else p2.x
                if x_lo <= x_side <= x_hi:
                    # segment and side are crossing - get intersection's coords
                    x_inter = p1.x
                    y_inter = self.get_y_for(x_inter)
                    # and check whether y of intersection point is between both of side's ys
                    if p1.y <= y_inter <= p2.y:
                        intersection_points.append(Point.Point(x_inter, y_inter))
            else:
                # check whether bottom or upper side are between two segment's ending points
                y_side = p1.y if name == 'bottom' else p2.y
                if y_lo <= y_side <= y_hi:
                    # segment and side are crossing - get intersection's coords
                    y_inter = p1.y
                    x_inter = self.get_y_for(y_inter)
                    # and check whether x of intersection point is between both of side's xs
                    if p1.x <= x_inter <= p2.x:
                        intersection_points.append(Point.Point(x_inter, y_inter))
        # return all of box's intersection points
        return intersection_points

    def get_x_for(self, y):
        return (y - self.b) / self.a

    def get_y_for(self, x):
        return self.a * x + self.b