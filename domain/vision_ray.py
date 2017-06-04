from segment import Segment
from point import Point


class VisionRay(Segment):
    def __init__(self, p1, p2, camera):
        self.camera = camera
        Segment.__init__(self, p1, p2)

    def get_intersections_with(self, box):
        # intersection points
        intersection_points = []
        # for readability
        x_lo = self.x_lo  # vision ray lower x coord
        x_hi = self.x_hi  # vision ray higher x coord
        y_lo = self.y_lo  # vision ray lower y coord
        y_hi = self.y_hi  # vision ray higher y coord
        # iterate over sides and depending on its type check whether it intersects with a vision ray
        for name, side in box.get_sides().iteritems():
            s = side
            # separate into vertical and horizontal sides
            if name == 'lf' or name == 'rt':
                # check whether left or right side are between two ray's ending points
                x_side = s.x_lo if name == 'lf' else s.x_hi
                if x_lo <= x_side <= x_hi and (s.y_lo <= y_lo <= s.y_hi or s.y_lo <= y_hi <= s.y_hi):
                    # ray and side may be crossing - get intersection's coords
                    x_inter = s.p1.x
                    y_inter = self.get_y_for(x_inter)
                    # and check whether y of intersection point is between both of side's ys
                    if s.y_lo <= y_inter <= s.y_hi:
                        intersection_points.append(Point(x_inter, y_inter)) # vision ray lowest x coord
            else:
                # check whether bottom or upper side are between two segment's ending points
                y_side = side.y_lo if name == 'bt' else side.y_hi
                if y_lo <= y_side <= y_hi and (s.x_lo <= x_lo <= s.x_hi or s.x_lo <= x_hi <= s.x_hi):
                    # ray and side may be crossing - get intersection's coords
                    y_inter = s.p1.y
                    x_inter = self.get_x_for(y_inter)
                    # and check whether x of intersection point is between both of side's xs
                    if s.x_lo <= x_inter <= s.x_hi:
                        intersection_points.append(Point(x_inter, y_inter))  # ray and side are crossing
        # return all of box's intersection points
        return intersection_points
