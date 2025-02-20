+ 요즘은 가상으로 현실과 최대한 비슷한 환경에서 실험할 수 있게 해주는 시뮬레이터 프로그램이 많습니다. 
+ 이번 과제에서는 자동차를 마치 실제 도로에서 운전하는 것 같은 체험을 하게 해주는 주행 시뮬레이터를 만들어 볼게요. 
+ 본격적으로 주행 시뮬레이터를 만들기 전에 아래의 조건들을 만족하는 프로그램을 
+ 어떻게 객체 지향적으로 작성할 수 있을지 한번 고민해보세요!

### 주행 시뮬레이터는:

+ 여러 가지 교통 수단들(일반 자동차, 스포츠카, 자전거 등)을 가질 수 있습니다.
+ 갖고 있는 교통 수단들의 주행을 동시에 시작하고 정지할 수 있습니다.
+ 갖고 있는 교통 수단들의 현재 속도를 문자열 메시지로 볼 수 있습니다.
+ 주행 시뮬레이터가 완성되면 어떻게 사용할 수 있을지 미리 테스트 코드를 보여드리겠습니다.

```python
# 일반 자동차 인스턴스들
car_1 = NormalCar(0, 100)
car_2 = NormalCar(0, 120)

# 스포츠카 인스턴스들
sports_car_1 = SportsCar(0, 200)
sports_car_2 = SportsCar(0, 190)

# 자전거 인스턴스
bicycle = Bicycle(0)

# 주행 시뮬레이터 인스턴스
driving_simulator = DrivingSimulator()

# 주행 가능 인스턴스들을 주행 시뮬레이터에 추가한다
driving_simulator.add_vehicle(car_1)
driving_simulator.add_vehicle(car_2)
driving_simulator.add_vehicle(sports_car_1)
driving_simulator.add_vehicle(sports_car_2)
driving_simulator.add_vehicle(bicycle)
driving_simulator.add_vehicle(1)

# 시뮬레이터 내 모든 인스턴스들을 주행 시작시킨다
driving_simulator.start_all_vehicles()
print(driving_simulator)

# 시뮬레이터 내 모든 인스턴스들의 주행 정지시킨다
driving_simulator.stop_all_vehicles()
print(driving_simulator)

"""
1은 교통 수단이 아니기 때문에 추가할 수 없습니다
모든 교통 수단을 주행 시작시킵니다!

일반 차량 시동겁니다.
일반 차량 시동겁니다.
스포츠카 시동겁니다.
스포츠카 시동겁니다.
자전거 페달 돌리기 시작합니다.
이 일반 차량은 현재 50.0km/h로 주행 중입니다.
이 일반 차량은 현재 60.0km/h로 주행 중입니다.
이 스포츠카는 현재 200km/h로 주행 중입니다.
이 스포츠카는 현재 190km/h로 주행 중입니다.
이 자전거는 현재 5.0km/h로 주행 중입니다.

모든 교통 수단을 주행 정지시킵니다!

이 일반 차량은 현재 0km/h로 주행 중입니다.
이 일반 차량은 현재 0km/h로 주행 중입니다.
이 스포츠카는 현재 0km/h로 주행 중입니다.
이 스포츠카는 현재 0km/h로 주행 중입니다.
이 자전거는 현재 0km/h로 주행 중입니다.
"""
```