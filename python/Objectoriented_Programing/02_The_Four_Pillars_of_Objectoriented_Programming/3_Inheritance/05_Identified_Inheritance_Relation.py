class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03
    
    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name
        self.wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self.wage *= self.raise_percentage


class Cashier(Employee):
    
    burger_price = 4000
    
    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage)
        self.number_sold = number_sold
    
    def take_order(self, money_received):
        """주문과 돈을 받고 거스름돈을 리턴한다"""
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change
    
    def __str__(self):
        return Cashier.company_name + " 계산대 직원: " + self.name

class DeliveryMan(Employee):
    """배달원 클래스"""

    def __init__(self, name, wage, on_standby):
        super().__init__(name, wage)
        self.on_standby = on_standby

    def deliver(self, address):
        """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 메시지를 출력한다"""
        if self.on_standby:
            print(address + "로 배달 나갑니다!")
            self.on_standby = False
        else:
            print("이미 배달하러 나갔습니다!")

    def back(self):
        """배달원 복귀를 처리한다"""
        self.on_standby = True

    def __str__(self):
        return DeliveryMan.company_name + " 배달원: " + self.name
        
        
        
cashier = Cashier("최우진", 10000, 4)
cashier.raise_pay()
"""
위와 같이 raise_pay 메소드를 호출하면 python은
    1. Cashier 클래스로 가서 raise_pay 메소드를 찾는다
    2. 만약 없는 것을 확인했다면, 
    3. Cashier의 부모 클래스인 Employee 클래스로 거슬러 올라가서 확인한다.
    4. 정의가 되어 있다면 그것을 확인해본다.
    5. 만약 가장 상위 클래스에도 없다면 정의되지 않았다는 오류를 발생시킨다.

Cashier의 init 메소드처럼 부모와 자식 클래스에 모두 같은 메소드가 정의되어 있으면
다시말해서 상속받은 메소드를 오버라이딩 했다면
python은 항상 자식클래스에 있는 것을 먼저 사용하기 때문에 자식 클래스에서 우선적으로 사용된다.
"""

print(isinstance(cashier, Cashier)) # True
print(isinstance(cashier, DeliveryMan)) # False
print(isinstance(cashier, Employee)) # True
"""
isinstance 함수는 첫 번째 argument가 
두 번째 argument의 인스턴스인지를 boolean으로 리턴한다.
"""

print(Cashier.mro())    # [<class '__main__.Cashier'>, <class '__main__.Employee'>, <class 'object'>]
"""
mro는 Method Resolution Order의 약자로 
인스턴스의 메소드가 호출될 때 파이썬이 탐색하는 클래스의 순서 
즉, 클래스의 상속 순서를 의미한다.
"""