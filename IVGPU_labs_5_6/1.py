class Point():
    __x: int
    __y: int
    name: str

    def __init__(self, name, x, y):
        self.name = name
        self.__x = x
        self.__y = y
        pass

    def __str__(self):
        return f"{self.name}({self.__x}, {self.__y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.__x == other.__x and self.__y == other.__y)
        else:
            raise BaseException("Объекты нельзя сравнивать")

    def __hash__(self):
        return hash(self.name)

    def __add__(self, other):
        if isinstance(other, Point):
            return Segment(self, other)

        elif isinstance(other, Segment):
            return BrokenLine([self, other.start_point, other.end_point])

        elif isinstance(other, BrokenLine):
            other.points.append(self)

        else:
            raise BaseException("Объекты нельзя складывать")

    def set_coordinate(self, x, y):
        self.__x = x
        self.__y = y
        pass

    def get_coordinate(self):
        return self.__x, self.__y

# -----------------------------------------------------------------------------


class Segment():
    start_point: Point
    end_point: Point
    start_x: int
    start_y: int
    end_x: int
    end_y: int

    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point
        self.start_x, self.start_y = self.start_point.get_coordinate()
        self.end_x, self.end_y = self.end_point.get_coordinate()
        pass

    def get_len(self):
        return ((self.start_x - self.end_x)**2 + (self.start_y - self.end_y)**2)**0.5

    def __str__(self):
        return f"{self.start_point.name}{self.end_point.name}({self.start_x}, {self.start_y}; {self.end_x}, {self.end_y})"

    def __add__(self, other):
        if isinstance(other, Segment):
            if (self.start_point == other.start_point) or (self.end_point == other.start_point):
                return BrokenLine([self.start_point, self.end_point, other.end_point])

            elif (self.start_point == other.end_point) or (self.end_point == other.end_point):
                return BrokenLine([self.start_point, self.end_point, other.start_point])

        elif isinstance(other, BrokenLine):
            other.points.append(self.start_point)
            other.points.append(self.end_point)

        elif isinstance(other, Point):
            return BrokenLine([self.start_point, self.end_point, other])

        else:
            raise BaseException("Объекты нельзя складывать")

# -----------------------------------------------------------------------------


class BrokenLine():
    points: list

    def __init__(self, points):
        if type(points) == list and len(points) >= 3:
            i = 0
            while i < len(points) - 1:
                if points[i] == points[i + 1]:
                    points.pop(i + 1)
                i += 1
            self.points = points
        pass

    def __str__(self):
        names = ""
        for point in self.points:
            names = names + point.name + ", "
        return names[:-2]

    def get_len(self):
        line_length = 0
        for i in range(len(self.points) - 1):
            line_length += (Segment(self.points[i],
                            self.points[i + 1])).get_len()
        return line_length

    def __add__(self, other):
        if isinstance(other, Point):
            if (other not in self.points):
                self.points.append(other)

        elif isinstance(other, Segment):
            if other.start_point in self.points or other.end_point in self.points:
                self.points.append(other.start_point)
                self.points.append(other.end_point)

        elif isinstance(other, BrokenLine):
            self.points.append(other)

        else:
            raise BaseException("Объекты нельзя складывать")


# -----------------------------------------------------------------------------
if __name__ == "__main__":

    broken_line = BrokenLine([
        Point("A", 0, 0),
        Point("B", 1, 1),
        Point("B", 1, 1),
        Point("C", 2, 2)
    ])

    print(broken_line.__str__())

    for element in broken_line.points:
        print(element.__str__())

    print(broken_line.get_len())

    # --------------------------

    # segment = Segment(Point("A", 0, 0), Point("B", 4, 3))
    # segment2 = Segment(Point("A", 0, 0), Point("C", -1, 18))
    # segment3 = Segment(Point("D", 18, 3), Point("C", -1, 18))

    # # print(str(segment))
    # # print(str(segment2))

    # broken_line = segment + segment2
    # segment3.__add__(broken_line)

    # # for element in broken_line.points:
    # #     print(str(element))

    # for element in (segment + Point("J", -8, -8)).points:
    #     print(str(element))

    # --------------------------

    # point = Point("point", 18, 7)

    # x, y = point.get_coordinate()
    # point.set_coordinate(0, 0)

    # print(point.get_coordinate())
    # print(x, y)

    # --------------------------

    # point = Point("point", 18, 7)
    # segment = Segment(Point("point2", -6, 0), Point("point3", 60, 91))

    # broken_line = point.__add__(segment)

    # for element in broken_line.points:
    #     print(element.__str__())

    # point4 = Point("point4", 0, 0)
    # point4.__add__(broken_line)

    # print(broken_line.points[3].__str__())

    # --------------------------

    # point = Point("point", 2, 7)
    # point2 = Point("point2", 2, -7)

    # print(point.__str__())
    # print(point2.__str__())
    # print(point == point2)

    # points_set = {
    #     Point("point", 2, 7),
    #     Point("point2", 8, -51),
    #     Point("point3", 39, 10),
    #     Point("point4", -1, 19),
    #     Point("point5", 0, 38)
    # }

    # for element in points_set:
    #     print(element.__str__())

    # --------------------------

    # point1 = Point("point2", 19, -3)
    # point2 = Point("point2", 4, -3)
    # point3 = Point("point3", 29, 1)
    # point4 = Point("point4", 0, -12)

    # points_list = [point1, point2, point3, point4]

    # broken_line = BrokenLine(points_list)
    # broken_line.points[2].print()
