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
    pass


cashier = Cashier("최우진", 10000)

cashier.raise_pay()
print(cashier.wage) # 10300.0

"""
상속을 하게 되면 부모 클래스에 정의한 함수와 메소드
모두를 그대로 가지고 와서 사용할 수 있다.
"""