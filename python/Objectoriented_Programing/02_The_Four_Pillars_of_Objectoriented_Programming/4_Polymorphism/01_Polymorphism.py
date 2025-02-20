import importlib.util
"""
Python의 importlib.util 모듈을 가져온다
이 모듈은 동적으로 로드하거나 파일 경로에서 모듈을 가져오는 고급 기능을 제공한다.
일반적인 import 문으로 처리할 수 없는 상황
예를 들면 모듈 이름이 동적이거나
경로가 고정되지 않은 경우에 사용된다.
"""

# 모듈 경로 지정
module_name = "00_Collection_of_Shapes"
"""
가져올 모듈의 이름을 지정한다
만약 import mymodule 이 있을때 mymodule과 같은 역할을 한다.
"""
file_path = "./Python\\Objectoriented_programming\\02_The_Four_Pillars_of_Objectoriented_Programming\\4_Polymorphism\\00_Collection_of_Shapes.py"
"""
로드할 Python 파일의 절대 또는 상대 경로를 문자열로 지정한다.
여기서는 Python 코드가 포함된 .py 파일로 연결되어야만 한다.
이 파일이 나중에 모듈로 로드가 된다.
"""

# 모듈 로드
spec = importlib.util.spec_from_file_location(module_name, file_path)
"""
모듈의 spec을 생성한다
spec은 모듈의 메타데이터
예를 들면 이름이나 경로등을 포함하며
나중에 모듈을 메모리에 로드할 때 사용한다
파라미터로는
    - module_name: 가져올 모듈의 이름
    - file_path: 모듈의 소스 파일 경로
를 받고

반환값: 로드할 모듈의 spec 객체(ModuleSpec)
"""
module = importlib.util.module_from_spec(spec)
"""
spec 객체(ModuleSpec)를 기반으로 비어있는 모듈 객체를 생성한다
이 단계에서는 모듈의 내용이 메모리에 로드되지 않았으며, 단지 메타데이터와 빈 구조만 생성된 상태이다

반환값: 메모리에 생성된 모듈 객체
"""
spec.loader.exec_module(module)
"""
파일에 정의된 Python 코드를 실제로 실행하여 모듈 객체를 메모리에 로드한다
module 객체가 완전한 상태로 초기화되며, 파일에 정의된 클래스, 함수, 변수 등을 사용할 수 있게 해준다.

결과: module 객체를 통해 파일의 내용을 사용할 수 있다. 
"""

class Paint:
    """그림판 클래스"""
    def __init__(self):
        self.shapes = []
    
    def add(self, shape):
        """파라미터 shape 도형을 추가한다"""
        self.shapes.append(shape)
    
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
"""
shapes 인덱스 혹은 이걸 저장한 변수 shape이
여러 클래스의 인스턴스가 될 수 있는 성질을
객체 지향 프로그램에서는 다형성이라고 부른다.
python에서 서로 다른 클래스들의 같은 이름의 메소드를 정의함으로써
다형성을 적용한다.
따라서 앞으로 어떠한 도형클래스를 정의하더라도
draw 메소드를 이용한다면 그림판에 새로운 도형, 새로운 기능을 추가할 수 있다.
"""

Rectangle = module.Rectangle
Circle = module.Circle
EquilateralTriangle = module.EquilateralTriangle

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

