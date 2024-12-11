# Основи ООП

class Point:
    x = 0                              # оголошення класу
    y = 0                              #

    def __init__(self, x, y):
        self.x = x
        self.y = y

                                       #
                                       #
def main():                            #
    p1 = Point()                       # Створення об'єкту - оператор new не вживається
    print(p1.x, p1.y)                  #
    Point.x = 10                       # оголошення полів у класі дозволяє статичний доступ
    print(p1.x, p1.y)                  # 5 10

if __name__ == '__main__': main()
