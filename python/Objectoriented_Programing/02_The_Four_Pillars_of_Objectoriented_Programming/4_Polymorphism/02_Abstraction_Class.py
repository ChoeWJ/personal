"""
코드를 실행하는데에는 문제가 없지만 또 다른 문제가 발생하게 된다
그림판 클래스에 추가할 도형 클래스를 만드는 개발자가 어떻게 draw 메소드를 구현해야할지 알아내기 힘들다
이 문제를 해결하기 위해서 모든 도형 클래스들이 꼭 만족시켜야 될 필수 내용을 정리해서
손쉽게 전달하는 방법을 사용한다

    - 그림판 클래스에서 사용되는 모든 도형 메소드는 반드시 draw 메소드를 구현해야 한다.

클래스 안에서 반복되는 내용은 이전 챕터의 상속을 사용하면 되는데
이러한 중복되는 내용을 부모 클래스로 지정해준다

상속받은 draw 메소드를 반드시 오버라이드를 해야만 하게 만든다.
이때 추상클래스를 사용하면 해결할 수 있다.

추상클래스는 여러 클래스들이 꼭 구현해야 될 내용들을 적어두고
자식클래스가 상속받아 오버라이드에 사용하는 클래스이다.
따라서 부모 클래스를 추상클래스로 만든다.

    - ABC(Abstract Base Class): 추상 클래스를 만들기 위한 기능을 제공하는 클래스
    - abstractmethod
        - 추상클래스가 되기 위한 두 번쨰 조건
        - 적어도 하나의 추상 메소드라는 것을 가져야 한다.

추상 클래스로는 인스턴스를 만들 수없다. 
만약 강제로 만들면 
    TypeError: Can't instantiate abstract class Shape without an implementation for abstract method 'draw' 
에러가 발생한다.
"""
from abc import ABC, abstractmethod

class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def draw(self):
        """도형을 콘솔에 그린다."""
        pass