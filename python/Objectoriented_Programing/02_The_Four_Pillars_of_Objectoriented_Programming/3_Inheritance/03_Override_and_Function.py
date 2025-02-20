"""
부모 클래스에서 물려받은 내용을
자식 클래스가 바꾸는 것을 오버라이딩(Overriding) 이라고 한다.
오버라이딩에서는 기존의 내용을 바꿔서 정의해주면 된다.
"""

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
    
    # 스페셜 메소드 오버라이드
    def __init__(self, name, wage, number_sold):
        """
        super 함수로 부모 클래스의 메소드를 활용할 때는 argument로 self를 넘겨줄 필요가 없다
        """
        super().__init__(name, wage)
        self.number_sold = number_sold
    """
    def __init__(self, name, wage, number_sold):
        Employee.__init__(self, name, wage)
        '''
        부모 클래스에서 넘겨받은 인스턴스들을
        위와 같이 사용이 가능하다
        이렇게 사용하면 위의 줄이 실행될때 Employee 클래스의 init 메소드의 내용
        즉, self.name과 self.wage를 초기화하는 변수가 실행되므로
        새 인스턴스 변수가 모두 잘 설정된다
        '''
        self.number_sold = number_sold
    """
    """
    def __init__(self, name, wage, number_sold):
        self.name = name
        self.wage = wage
        self.number_sold = number_sold
    """
    
    def take_order(self,money_received):
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
        
cashier = Cashier("최우진", 10000, 4)
cashier.raise_pay()

print(cashier.wage) # 10300.0

print(cashier.take_order(7000)) # 3000
print(cashier.take_order(3000)) # 돈이 충분하지 않습니다
                                # 3000

print(cashier.burger_price) # 4000

print(cashier.number_sold)  # 5
print(cashier)  # 코드잇 버거 계산대 직원: 최우진


