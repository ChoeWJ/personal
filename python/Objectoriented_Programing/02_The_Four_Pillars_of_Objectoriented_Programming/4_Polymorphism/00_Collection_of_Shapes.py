from abc import ABC, abstractmethod

class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def draw(self):
        """도형을 콘솔에 그린다."""
        pass


class Rectangle(Shape):
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def draw(self):
        """직사각형을 콘솔에 그린다"""
        result = "\n"
        for i in range(self.height):
            result += "* " * self.width + "\n"
        print(result)
        
    def __str__(self):
        return f"밑변 {self.width}, 높이 {self.height}인 직사각형"
    
class Circle(Shape):
    """원 클래스"""
    def __init__(self, diameter):
        self.diameter = diameter
        
    def draw(self):
        """원을 콘솔에 그린다"""
        radius = self.diameter / 2 - .5
        r = (radius + .25)**2 + 1
        result = "\n"
        for i in range(self.diameter):
            y = (i - radius)**2
            for j in range(self.diameter):
                x = (j - radius)**2
                if x + y <= r:
                    result += "* "
                else:
                    result += "  "
            result += "\n"
        print(result)
    
    def __str__(self):
        """원 정보를 문자열로 출력한다"""
        return f"지름 {self.diameter}인 원"
    
class EquilateralTriangle(Shape):
    """정삼각형 클래스"""
    def __init__(self, side):
        self.side = side
    
    def draw(self):
        """도형을 콘솔에 그린다"""
        result = "\n"
        for i in range(1, self.side+1):
            result += " " * (self.side - i) + "* " * i + "\n"
        print(result)
    
    def __str__(self):
        return f"변의 길이가 {self.side}인 정삼각형"
