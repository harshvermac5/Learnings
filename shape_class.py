class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length**2
    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__()
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * (self.length + self.breadth)

    

shape = Shape()
# square = Square(float(input(f"Enter the Side of Square: ")))

# print(square.area())

rectangle = Rectangle(float(input(f"Enter the Length of Rectangle: ")), float(input(f"Enter the Breadth of the Rectangle: ")))

print(rectangle.area())
print(rectangle.perimeter())
