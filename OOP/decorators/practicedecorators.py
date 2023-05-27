import math

class Generic:
    def __init__(self):
        self.area = 0

    @staticmethod
    def sum_areas(*args):
        total_sum = 0
        for elem in args:
            total_sum += elem.area
        return total_sum
    
    @classmethod
    def create_object(cls, value):
        return cls(value)


class Square(Generic):
    def __init__(self, size):
        super().__init__()
        self.width = size
        self.height = size
    
    def calculate_area(self):
        self.area = self.height * self.width
        return self.area
    
    def __repr__(self):
        return f'Square of width {self.width} and height {self.height}'


class Circle(Generic):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def calculate_area(self):
        self.area = (self.radius ** 2) * math.pi
        return self.area

    def __repr__(self):
        return f'Circle of radius {self.radius}'
    

my_square = Square.create_object(4)
print(my_square)
print(my_square.calculate_area())

my_circle = Circle.create_object(2)
print(my_circle)
print(my_circle.calculate_area())

total_area = Generic.sum_areas(my_square, my_circle)
print(total_area)