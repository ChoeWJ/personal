"""
실습 설명
이번 과제에서는 계산기 클래스를 만들어 볼게요. 이때까지 객체는 속성과 행동을 갖는 존재라고 했습니다. 
하지만 속성없이 행동만 있는 객체도 있습니다. 이 말은 변수는 없고 메소드만 있는 클래스도 만들 수 있다는 뜻입니다. 
우리가 배웠던 메소드의 종류는 아래 3가지입니다.

    1. 인스턴스 메소드
    2. 클래스 메소드
    3. 정적 메소드
    
변수가 없는 클래스에서는 무슨 메소드를 써야 할까요? 
이전에 우리는 인스턴스 변수나 클래스 변수를 쓰지 않을 거라면 정적 메소드(static method)를 사용해야 한다고 배웠죠? 
변수가 없는 클래스에서는 정적 메소드를 정의하면 됩니다.

다음 조건들을 보고 계산기 클래스인 SimpleCalculator 클래스의 정적 메소드들을 완성해 보세요.

    - 정적 메소드
        - add: 파라미터로 받은 두 숫자의 합을 리턴한다
        - subtract: 첫 번째 파라미터에서 두 번째 파라미터를 뺀 값을 리턴한다
        - multiply: 파라미터로 받은 두 숫자의 곱을 리턴한다
        - divide: 첫 번째 파라미터를 두 번째 파라미터로 나눈 값을 리턴한다
"""

# 계산기 클래스
class SimpleCalculator:
    
    @staticmethod
    def add(first_number, second_number):
        return first_number + second_number
    
    @staticmethod
    def subtract(first_number, second_number):
        return first_number - second_number
    
    @staticmethod
    def multiply(first_number, second_number):
        return first_number * second_number
    
    @staticmethod
    def divide(first_number, second_number):
        return first_number / second_number
    
    
# 계산기 인스턴스 생성
calculator = SimpleCalculator()
    
# 계산기 연산 호출
print(calculator.add(4, 5))
print(calculator.subtract(4, 5))
print(calculator.multiply(4, 5))
print(calculator.divide(4, 5))
