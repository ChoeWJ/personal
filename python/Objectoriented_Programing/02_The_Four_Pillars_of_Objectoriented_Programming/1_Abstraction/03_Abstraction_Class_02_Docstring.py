"""
직관적인 이름들을 사용한다고 해도 
클래스와 인스턴스의 사용법을 전달하기 힘든 경우가 있다.

클래스의 여러 요소들에 대한 간단명료한 설명을
파이썬에서는 help라는 함수가 있다.
"""

# help(list)
"""
class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:
 |
 |  __add__(self, value, /)
 |      Return self+value.
 |
 |  __contains__(self, key, /)
 |      Return bool(key in self).
 |
-- More  --
"""
# Docstring
class BankAccount:
    """은행 게좌 클래스"""
    interest = 0.02
        
    def __init__(self, owner_name, balance):
        """인스턴스 변수: name(문자열), balance(실수형)"""
        self.owner_name = owner_name
        self.balance = balance
        
    def deposit(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드"""
        self.balance += amount
    
    def withdraw(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 줄여주는 메소드"""
        if self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount
    
    def add_interest(self):
        """잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드"""
        self.balance *= 1 + BankAccount.interest
        
help(BankAccount)

"""
Help on class BankAccount in module __main__:

class BankAccount(builtins.object)
 |  BankAccount(owner_name, balance)
 |
 |  은행 게좌 클래스
 |
 |  Methods defined here:
 |
 |  __init__(self, owner_name, balance)
 |      인스턴스 변수: name(문자열), balance(실수형)
 |
 |  add_interest(self)
 |      잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드
 |
 |  deposit(self, amount)
 |      잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드
 |
 |  withdraw(self, amount)
 |      잔액 인스턴스 변수 balance를 파라미터 amount만큼 줄여주는 메소드
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  interest = 0.02
"""