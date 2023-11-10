import math


# 4*. 7.1 реалізувати через in.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x: int, y: int, radius: int) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    @staticmethod
    def _distance(x1, y1, x2, y2):
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def contains(self, point: Point):
        distance = self._distance(self.x, self.y, point.x, point.y)
        return distance <= self.radius

    def __contains__(self, point: Point):
        return self.contains(point)


c = Circle(1, 2, 10)

assert c.contains(Point(1, 3)) == True
assert c.contains(Point(100, 100)) == False
assert c.contains(Point(1, 2)) == True
assert c.contains(Point(11, 2)) == True
assert c.contains(Point(1, 12)) == True
assert c.contains(Point(1, 13)) == False
assert (Point(1, 13) in c) == False
assert (Point(11, 1) in c) == False
assert (Point(11, 2) in c) == True
assert (Point(11, 3) in c) == False
assert (Point(11, 2) in c) == True
