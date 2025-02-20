"""
개발자들에게 추상 클래스를 사용하라고 알려주는 방법 3가지가 있다
추상 클래스 사용에 대한 강제성을 늘려가는 순서로 나아간다.

    1. Docstring 사용
        - 가장 쉽고 강제성이 약함
        - 그림판의 모든 도형들은 add 메소드를 통해서 추가를 하는데
        - add의 파라미터 shape은 추상 클래스 Shape의 인스턴스여야한다고 작성해 놓는다.
        - 그러면 개발자들이 확인하고 알아서 사용하게 만든다.
    
    2. TypeHinting 기능 사용
        - shape: Shape
    
    3. isinstance 함수 사용
        - 가장 강제성이 강함

"""
import importlib.util

# 모듈 경로 지정
module_name = "00_Collection_of_Shapes"
file_path = "./Python\\Objectoriented_programming\\02_The_Four_Pillars_of_Objectoriented_Programming\\4_Polymorphism\\00_Collection_of_Shapes.py"

# 모듈 로드
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

Rectangle = module.Rectangle
Circle = module.Circle
EquilateralTriangle = module.EquilateralTriangle
Shape = module.Shape

class Paint:
    """그림판 클래스"""
    def __init__(self):
        self.shapes = []
        
    def add(self, shape: Shape):
        """
        파라미터 shape 도형을 추가한다
        
        파라미터 shape은 반드시 추상 클래스 Shape의 인스턴스여야 한다.
        """
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("추상 클래스 Shape의 인스턴스가 아닌 도형은 추가할 수 없습니다.")
    
    def draw(self, index):
        """파라미터 index에 해당하는 도형을 그린다"""
        if 0 <= index and index < len(self.shapes):
            self.shapes[index].draw()
        else:
            print("인덱스를 확인해 주세요")
            
    def draw_all(self):
        """모든 도형을 그린다"""
        if not self.shapes:
            print("그림판에 도형이 없습니다")
        
        for shape in self.shapes:
            shape.draw()
        
    def __str__(self):
        """그림판 안 도형들에 대한 정보를 리턴한다"""
        result = "\n그림판에 있는 도형들:\n"
        for i in range(len(self.shapes)):
            result += f"    {i}. {self.shapes[i]}\n"
        return result



rectangle = Rectangle(7, 8)
circle = Circle(9)
triangle = EquilateralTriangle(7)

paint = Paint()

paint.add(rectangle)
paint.add(circle)
paint.add(triangle)

paint.draw(0)
paint.draw(2)
paint.draw(3)

paint.draw_all()



