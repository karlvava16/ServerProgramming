# Основи ООП
import math
import json


class Point:
    x = 0                              # оголошення класу
    y = 0                              #
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%f, %f)" % (self.x, self.y)

    def __repr__(self):
        return "<%s> (%f, %f)" % (__class__.__name__, self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        if isinstance(other, int) or isinstance(other, float):
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError("Can only add points to Point")

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x * other.x, self.y * other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Point(self.x * other, self.y * other)
        else:
            raise TypeError("Can only multiply points to Point")

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @staticmethod
    def stat():
        return "Stat method"

    @staticmethod
    def from_json(j):
        if isinstance(j, str):
            d = json.loads(j)
            return Point(d["x"], d["y"])
        elif isinstance(j, dict):
            return Point(j["x"], j["y"])
        else:
            raise TypeError("Point can only be JSON string")


def main():                            #
    p1 = Point(1, 2)             # Створення об'єкту - оператор new не вживається
    print(p1.x, p1.y)                  #
    Point.x = 10                       # оголошення полів у класі дозволяє статичний доступ
    print(p1.x, p1.y)                  # 5 10
    p2 = Point(10, 20)
    print(p2)
    print(repr(p2))
    print(p1 + p2)
    print(p1 + 5)
    print(p1 * p2)
    print(p1 * 3)
    print(p1.magnitude())
    print(Point.stat())
    print(Point.from_json("{\"x\": 4, \"y\": 5}"))
    print(Point.from_json({"x": 1, "y": 2}))


if __name__ == '__main__': main()
