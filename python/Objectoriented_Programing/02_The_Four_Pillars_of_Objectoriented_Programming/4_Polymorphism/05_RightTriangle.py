"""
과제 설명
원, 직사격형, 정삼각형에 이어서 직각이등변삼각형도 그림판에서 사용하고 싶습니다. 
다음 조건을 만족하는 RightTriangle 클래스를 만들어봅시다.

추상 클래스 Shape 클래스를 상속받는다.
인스턴스 변수로는 변 하나(side)를 받는다.
출력하면 변이 {변의 길이}인 직각이등변삼각형 메시지가 나온다.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class RightTriangle(Shape):
    
    def __init__(self, side):
        self.side = side
    
    def draw(self):
        result = ""
        for i in range(1, self.side + 1):
            result += "* " * i + "\n"
        print(result)
    
    def __str__(self):
        return f"변이 {self.side}인 직각이등변삼각형"

# 실행 코드
right_triangle = RightTriangle(7)

right_triangle.draw()
print(right_triangle)
