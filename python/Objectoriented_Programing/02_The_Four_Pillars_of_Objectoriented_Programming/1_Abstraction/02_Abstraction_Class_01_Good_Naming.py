# 추상화의 안 좋은 예시
class SomeClass:
    
    class_variable = 0.02
    
    def __init__(self, variable_1, variable_2):
        self.variable_1 = variable_1
        self.variable_2 = variable_2
        
    def method_1(self, some_value):
        self.variable_2 += some_value
        
    def method_2(self, some_value):
        if self.variable_2 < some_value:
            print("Insufficient balance!")
        else:
            self.variable_2 -= some_value
            
    def method_3(self):
        self.variable_2 *= 1 + SomeClass.class_variable
        
# 추상화의 좋은 예시
# 계좌 클래스 생성
class BankAccount:
    
    # 이자율은 연 2%
    interest = 0.02
    
    # 계좌 주인의 인스턴스 변수 초기화 
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
    
    # 계좌에 입금하는 함수
    def deposit(self, amount):
        # 입력된 값(amount)만큼 계좌(balance) 잔액을 추가 
        self.balance += amount
    # 계좌에서 출금하는 함수
    def withdraw(self, amount):
        # 만약 출금(amount)하려는 금액이 계좌 잔액보다 클 경우
        if self.balance < amount:
            # Insufficient balance!라는 오류 메시지를 출력
            print("Insufficient balance!")
        # 아닐시에는
        else:
            # 계좌 잔액에서 출금하려는 잔액만큼을 뺀다.
            self.balance -= amount
    
    # 이자 지급함수
    def add_interest(self):
        # 계좌의 잔액의 2%를 이자로 지급
        self.balance *= 1 + BankAccount.interest
        
        
account = BankAccount("홍길동", 1000)

account.add_interest()

print(account.balance)  # 1020.0

account.deposit(500)

print(account.balance)  # 1520.0

account.withdraw(2000)

print(account.balance)  # Insufficient balance!
                        # 1520.0

account.withdraw(1000)

print(account.balance)  # 520.0