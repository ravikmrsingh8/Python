import math


class Line(object):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def slope(self):
        del_y = self.point2[1]-self.point1[1]
        del_x = self.point2[0]-self.point1[0]
        return del_y/del_x

    def distance(self):
        del_y = self.point2[1] - self.point1[1]
        del_x = self.point2[0] - self.point1[0]
        return math.sqrt(del_y**2 + del_x**2)


# using tuple unpacking
class Line2(object):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def slope(self):
        x2, y2 = self.point2
        x1, y1 = self.point1
        return (y2-y1)/(x2-x1)

    def distance(self):
        x2, y2 = self.point2
        x1, y1 = self.point1
        return math.sqrt((y2-y1)**2 + (x2-x1)**2)


l = Line((3, 2), (8, 10))
print("Slope {}".format(l.slope()))
print("Distance {:0.3f}".format(l.distance()))


l2 = Line2((3, 2), (8, 10))
print("Slope {}".format(l2.slope()))
print("Distance {:0.3f}".format(l2.distance()))

