"""
실습 설명
아래 코드에는 자유 입출금 계좌(CheckingAccount)와 
저축 계좌(SavingsAccount) 클래스가 정의되어 있습니다. 
자유 입출금 계좌와 저축 계좌는 서로 비슷한 점이 많아서 두 클래스에는 중복되는 코드가 많습니다. 
이번 챕터에서 배운 상속을 이용해서 중복되는 코드를 줄여 봅시다.

중복되는 코드를 바탕으로 두 클래스의 부모 클래스가 될 은행 계좌(BankAccount) 클래스를 정의하세요.
자유 입출금 계좌(CheckingAccount) 클래스와 저축 계좌(SavingsAccount) 클래스가 
은행 계좌(BankAccount) 클래스를 상속하도록 하세요.
"""

class BankAccount:
    def __init__(self, name, balance):
        """모든 인스턴스 변수의 초기값을 설정한다"""
        self.name = name
        self.balance = balance
        
    def withdraw(self, amount):
        """돈을 출금한다"""
        self.balance -= amount

    def deposit(self, amount):
        """돈을 입금한다"""
        self.balance += amount
        
    def __str__(self):
        """계좌의 정보를 문자열로 리턴한다."""
        return "{}님의 계좌 예치금은 {}원입니다".format(self.name, self.balance)

class CheckingAccount(BankAccount):
    """자유 입출금 계좌 클래스"""
    
    def __init__(self, name, balance, max_spending):
        """모든 인스턴스 변수의 초기값을 설정한다"""
        super().__init__(name, balance)
        self.max_spending = max_spending

    def use_check_card(self, amount):
        """한 회 사용 한도 초과 이하인 금액을 체크 카드 결제 시 예치금을 줄인다"""
        if amount <= self.max_spending:
            self.balance -= amount
        else:
            print("{}님의 체크 카드는 한 회 {} 초과 사용 불가능합니다".format(self.name, self.max_spending))


class SavingsAccount(BankAccount):
    """저축 계좌 클래스"""
    
    def __init__(self, name, balance, interest_rate):
        """모든 인스턴스 변수의 초기값을 설정한다"""
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        """이자를 더한다"""
        self.balance *= (1+self.interest_rate)


bank_account_1 = CheckingAccount("성태호", 100000, 10000)
bank_account_2 = SavingsAccount("강영훈", 20000, 0.05)

bank_account_1.withdraw(1000)
bank_account_1.deposit(1000)
bank_account_1.use_check_card(2000)

bank_account_2.withdraw(1000)
bank_account_2.deposit(1000)
bank_account_2.add_interest()

print(bank_account_1)   # 성태호님의 계좌 예치금은 98000원입니다
print(bank_account_2)   # 강영훈님의 계좌 예치금은 21000.0원입니다

print(CheckingAccount.mro())    # [<class '__main__.CheckingAccount'>, <class '__main__.BankAccount'>, <class 'object'>]
print(SavingsAccount.mro())     # [<class '__main__.SavingsAccount'>, <class '__main__.BankAccount'>, <class 'object'>]