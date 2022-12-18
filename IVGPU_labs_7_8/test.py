

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print(f"x = {self.x}, y = {self.y}")
        pass

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

# ---------------------------


def func():
    points = set()

    points.add(Point(0, 0))
    points.add(Point(43, 0))
    points.add(Point(847, 50))
    points.add(Point(0, 0))
    points.add(Point(3, -28))
    points.add(Point(847, 50))

    return frozenset(points)


#base_frozen = frozenset(base_types)
points_frozen = func()

# print(base_frozen)
print(len(points_frozen))

for point in points_frozen:
    point.print()
