+ 이제 리스코프 치환 원칙에 맞게 `Cashier 클래스`를 수정해봅시다. 

+ 리스코프 치환 원칙을 지키는 것은 부모 클래스의 규칙을 지키기만 하면 되니까 그리 어렵지 않습니다.

# 직원(Employee) 클래스

```python
class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03
    
    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name
        self._wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self._wage *= self.raise_percentage

    @property
    def wage(self):
        """_wage 변수 getter 메소드"""
        return self._wage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name
```

# 계산대 직원(Cashier) 클래스

```python
class Cashier(Employee):
    """계산대 직원 클래스"""
    raise_percentage = 1.05
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def take_order(self, money_received):
        """손님이 낸 돈을 받아 주문 처리를 하고 거스름돈을 리턴한다"""
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다. 돈을 다시 계산해서 주세요!")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return Cashier.company_name + " 계산대 직원: " + self.name
```

+ 수정한 `Cashier 클래스`의 코드에는 `raise_pay` , `wage` 메소드가 없군요. 

+ 리스코프 치환 원칙을 지키려면 부모 클래스의 메소드를 그냥 물려받는 것이 가장 안전하고 빠른 해결책이겠죠? 

+ 만약 오버라이딩을 하고 싶다면 **메소드의 파라미터와 리턴값의 타입과 개수를 맞춰서 오버라이딩**하면 됩니다. 

+ `take_order 메소드`는 `Employee 클래스`에는 없고, `Cashier 클래스`에서 아예 새로 추가한 메소드이므로 자유롭게 정의해도 상관없습니다.

+ 이전 영상의 코드를 다시 실행해볼까요?

```python
# Employee 인스턴스들 생성
employee_1 = Employee("성태호", 7000)
employee_2 = Employee("강영훈", 6500)

# Cashier 인스턴스 생성
cashier = Cashier("김대위", 9000)

# 생성한 모든 직원 인스턴스들을 리스트에 추가
employee_list = []
employee_list.append(employee_1)
employee_list.append(employee_2)
employee_list.append(cashier)

# 모든 직원들의 시급 인상
for employee in employee_list:
    employee.raise_pay()

# 모든 직원들의 총 시급 구하기
total_wage = 0

for employee in employee_list:
    total_wage += employee.wage

print(total_wage)

"""
실행 결과
23355.0
"""
```