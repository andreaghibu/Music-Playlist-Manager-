import math

class Shape:
    def area(self):
        pass

    def __str__(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius} has area {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle with width {self.width} and height {self.height} has area {self.area()}"

def main():
    print("Introducerea formei geometrice:")

    radius = float(input("Introduceti raza cercului: "))
    circle = Circle(radius)
    print(circle)

    width = float(input("Introduceti lățimea dreptunghiului: "))
    height = float(input("Introduceti înălțimea dreptunghiului: "))
    rectangle = Rectangle(width, height)
    print(rectangle)

if __name__ == "__main__":
    main()
