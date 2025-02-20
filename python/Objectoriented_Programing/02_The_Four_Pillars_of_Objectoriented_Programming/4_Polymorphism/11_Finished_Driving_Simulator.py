"""
실습 설명
교통 수단을 추상 클래스인 Vehicle 클래스로, 
실제 교통 수단들을 그것의 자식 클래스인 Bicycle, NormalCar, SportsCar 클래스로 모두 정의했습니다. 
이제 주행 시뮬레이터를 나타내는 클래스를 본격적으로 만들어볼까요? 주행 시뮬레이터는 다음 조건을 만족해야 합니다.

    1. 여러 가지 교통 수단들(자전거, 일반 자동차, 스포츠카 등)을 가질 수 있습니다.
    2. 갖고 있는 교통 수단들의 주행을 동시에 시작/정지시킬 수 있습니다.
    3. 갖고 있는 교통 수단들의 현재 속도를 문자열 메시지로 볼 수 있습니다.
    
주행 시뮬레이터는 템플릿에 DrivingSimulator라는 이름으로 미리 적어두었습니다. 
DrivingSimulator 클래스가 완성되었을 때 아래 코드의 실행 결과와 동일한 결과가 나와야합니다. 
DrivingSimulator 클래스의 각 메소드를 완성해 보세요.
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
        print("자전거 페달 돌리기 시작합니다.")
        self.speed = Bicycle.max_speed / 3    
        
    def __str__(self):
        return "이 자전거는 현재 {}km/h로 주행 중입니다.".format(self.speed)
        
        
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
        print("일반 자동차 시동겁니다.")
        self.speed = self.max_speed / 2    

    def __str__(self):
        return "이 일반 자동차는 현재 {}km/h로 주행 중입니다.".format(self.speed)

    
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
        print("스포츠카 시동겁니다.")
        self.speed = self.max_speed

    def __str__(self):
        return "이 스포츠카는 현재 {}km/h로 주행 중입니다.".format(self.speed)


class DrivingSimulator:
    def __init__(self):
        """교통 수단 인스턴스들을 담을 리스트를 변수로 갖는다"""
        self.vehicles = []

    def add_vehicle(self, new_vehicle):
        """교통 수단 인스턴스들만 시뮬레이터에 추가될 수 있게 한다"""
        if not isinstance(new_vehicle, Vehicle):
            print(f"{new_vehicle}은 교통 수단이 아니기 때문에 추가할 수 없습니다.")
            return
        self.vehicles.append(new_vehicle)

    def start_all_vehicles(self):
        """모든 교통 수단을 주행 시작시킨다"""
        print("모든 교통 수단을 주행 시작시킵니다!\n")
        
        for vehicle in self.vehicles:
            vehicle.start()

    def stop_all_vehicles(self):
        """모든 교통 수단을 주행 정지시킨다"""
        print("모든 교통 수단을 주행 정지시킵니다!\n")
        
        for vehicle in self.vehicles:
            vehicle.stop()

    def __str__(self):
        """갖고 있는 교통 수단들의 현재 속도를 문자열로 리턴한다"""
        res_str = ""

        for vehicle in self.vehicles:
            res_str += str(vehicle) + "\n"

        return res_str


# 자전거 인스턴스
bicycle = Bicycle(0)

# 일반 자동차 인스턴스들
car_1 = NormalCar(0, 100)
car_2 = NormalCar(0, 120)

# 스포츠카 인스턴스들
sports_car_1 = SportsCar(0, 200)
sports_car_2 = SportsCar(0, 190)


# 주행 시뮬레이터 인스턴스
driving_simulator = DrivingSimulator()

# 교통 수단 인스턴스들을 주행 시뮬레이터에 추가한다
driving_simulator.add_vehicle(bicycle)
driving_simulator.add_vehicle(car_1)
driving_simulator.add_vehicle(car_2)
driving_simulator.add_vehicle(sports_car_1)
driving_simulator.add_vehicle(sports_car_2)
driving_simulator.add_vehicle(1)

# 시뮬레이터 내 모든 인스턴스들을 주행 시작시킨다
driving_simulator.start_all_vehicles()
print(driving_simulator)

# 시뮬레이터 내 모든 인스턴스들을 주행 정지시킨다
driving_simulator.stop_all_vehicles()
print(driving_simulator)