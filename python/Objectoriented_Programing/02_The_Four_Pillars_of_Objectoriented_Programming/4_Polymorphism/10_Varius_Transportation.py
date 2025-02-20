"""
저번 과제에서는 "교통 수단"을 의미하는 Vehicle 추상 클래스를 정의했습니다. 아래 코드 기억나시죠?
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        # 추상 메소드 start: 교통 수단의 주행을 시작한다
        pass

    @property
    @abstractmethod
    def speed(self):
        # 변수 _speed(교통 수단의 속도)에 대한 추상 getter 메소드
        pass

    def stop(self):
        # 일반 메소드 stop: 교통 수단의 속도를 0으로 바꾼다
        self.speed = 0

이번 과제에서는 이 추상 클래스를 상속받는 3개의 자식 클래스를 완성할 건데요.

    - 자전거(Bicycle)
    - 일반 자동차(NormalCar)
    - 스포츠카(SportsCar)
    
지금 3가지 자식 클래스(Bicycle, NormalCar, SportsCar)가 템플릿에 있습니다. 
그리고 Vehicle 추상 클래스에 있던 추상 getter 메소드 speed는 
각 클래스마다 이미 speed getter/setter 메소드로 오버라이딩이 되어 있습니다.

이제 여러분이 각 클래스에서 아래 메소드 들을 직접 오버라이딩해야 합니다.

    - start 메소드
    - __str__ 메소드
    
각 클래스의 start 메소드는 다음 조건을 만족시켜야 합니다:

    - Bicycle 클래스의 start 메소드는 speed를 최대 속도의 1/3 값으로 설정해 줍니다.
    - NormalCar 클래스의 start 메소드는 speed를 최대 속도의 1/2 값으로 설정해 줍니다.
    - SportsCar 클래스의 start 메소드는 speed를 최대 속도값으로 설정해 줍니다.
    
아래 테스트 코드의 실행결과와 같은 결과가 나오도록 각 클래스의 이 두 가지 메소드를 오버라이딩해 보세요.
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        """추상 메소드 start: 교통 수단의 주행을 시작한다"""
        pass

    @property
    @abstractmethod
    def speed(self):
        """변수 _speed(교통 수단의 속도)에 대한 추상 getter 메소드"""
        pass

    def stop(self):
        """일반 메소드 stop: 교통 수단의 속도를 0으로 바꾼다"""
        self.speed = 0


class Bicycle(Vehicle):
    max_speed = 15 # 자전거의 최대 속도
    
    def __init__(self, speed):
        self._speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= Bicycle.max_speed else 0

    def start(self):
        self.speed = self.max_speed * (1 / 3)
        print("자전거 페달 돌리기 시작합니다.")
        
    def __str__(self):
        return f"이 자전거는 현재 {self.speed}km/h로 주행 중입니다."


class NormalCar(Vehicle):
    def __init__(self, speed, max_speed):
        self._speed = 0
        self.max_speed = max_speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0

    def start(self):
        self.speed = self.max_speed * (1 / 2)
        print("일반 자동차 시동겁니다.")
        
    def __str__(self):
        return f"이 일반 자동차는 현재 {self.speed}km/h로 주행 중입니다."


class SportsCar(Vehicle):
    def __init__(self, speed, max_speed):
        self._speed = speed
        self.max_speed = max_speed

    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self, new_value):
        self._speed = new_value if 0 <= new_value <= self.max_speed else 0

    def start(self):
        self.speed = self.max_speed
        print("스포츠카 시동겁니다.")
        
    def __str__(self):
        return f"이 스포츠카는 현재 {self.speed}km/h로 주행 중입니다."


# 자전거 인스턴스
bicycle = Bicycle(0)        
    
# 일반 자동차 인스턴스
car = NormalCar(0, 100)

# 스포츠카 인스턴스
sports_car = SportsCar(0, 200)

# 정의한 인스턴스들을 모두 주행 시작시킨다
bicycle.start()
car.start()
sports_car.start()

# 자전거의 속도를 출력한다
print(bicycle)

# 자전거만 주행을 멈춰준다
bicycle.stop()

# 결과 값을 출력한다
print(bicycle)
print(car)
print(sports_car)
