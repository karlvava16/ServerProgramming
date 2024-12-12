# Основи ООП

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
        else:
            raise TypeError("Can only add points to Point")


                                       #
                                       #
def main():                            #
    p1 = Point(1, 2)                       # Створення об'єкту - оператор new не вживається
    print(p1.x, p1.y)                  #
    Point.x = 10                       # оголошення полів у класі дозволяє статичний доступ
    print(p1.x, p1.y)                  # 5 10
    p2 = Point(10, 20)
    print(p2)
    print(repr(p2))


if __name__ == '__main__': main()
