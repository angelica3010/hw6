#HW #6: Create a class called shapes. The properties should be sides. It should have the methods: perimeter, area

#Create 4 different instances of the class. Print out each attribute of the instance and use each method in the class.

'''class Shapes:
    pass

square = Shapes()
square.perimeter = 4
square.area = 16
print(f"permiter {square.perimeter}, {square.area}")

print(square.perimeter, square.area)

rectangle = Shapes()
rectangle.perimeter = 8
rectangle.area = 64
print(rectangle.perimeter, rectangle.area)


triangle = Shapes()
triangle.perimeter = 6
triangle.area = 36
print(triangle.perimeter, triangle.area)

circle = Shapes()
circle.perimeter = 6.28
circle.area = 3.14
print(circle.perimeter, circle.area)'''

#make a class
class Shapes(object):
#make the property aka attribute sides:
    sides = None


#make the method perimeter
    def perimeter(self):
        pass
#make the method area
    def area(self):
        pass

#instance of class Shapes


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length * self.width

class Square(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*self.length + 2* self.width

class Triangle(Shapes):
    def __init__(self, base, height, side1, side2):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def perimeter(self):
        return self.base + self.side1 +self.side2

    def area(self):
        return self.base * self.height *.5

circ = Circle(4)
print(f"Circle's area is {circ.area()} and the perimeter is {circ.perimeter()}.")

rect = Rectangle(4,6)
print(f"Rectangle's area is {rect.area()} and the perimeter is {rect.perimeter()}.")

sqr = Square(8,8)
print(f"Square's area is {sqr.area()} and the perimeter is {sqr.perimeter()}.")

tria = Triangle( 3, 3, 3, 3)
rect = Rectangle(4,6)
print(f"Triangle's area is {tria.area()} and the perimeter is {tria.perimeter()}.")


#prints out the 15 most frequent from text.txt


import re
from collections import Counter
words = re.findall(r'\w+', open('text.txt').read().lower())
hello = Counter(words).most_common(15)

print(hello)
