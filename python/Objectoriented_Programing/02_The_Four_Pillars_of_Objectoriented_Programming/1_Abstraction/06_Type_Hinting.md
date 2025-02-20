+ 파이썬은 변수나 함수를 사용할 때 타입을 미리 정하지 않아도 되는 **동적 타입 언어**입니다. 

+ 코드를 쓸 때 더 간결하게 작성할 수 있지만,

+ 다른 사람이 쓴 코드를 사용할 때 어떤 타입을 써야 되는지 애매해서 혼란스러울 수 있다는 단점이 있는데요.

+ 파이썬은 이 단점을 보완하기 위해 버전 3.5부터 다양한 요소들에 타입을 표시할 수 있는 

+ ***타입 힌팅(type hinting)***이라는 기능을 추가했습니다. 

+ `BankAccount 클래스`에 적용해 보면서 어떻게 사용하는지 알아보겠습니다.

## 타입 힌팅 적용 전 코드

```python
class BankAccount:
    """은행 계좌 클래스"""
    interest = 0.02

    def __init__(self, name, balance):
        """인스턴스 변수: name(문자열), balance(실수형)"""
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount 만큼 늘린다"""
        self.balance += amount

    def withdraw(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount 만큼 줄인다"""
        if self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount

    def add_interest(self):
        """잔액 인스턴스 변수 balance를 이자율만큼 늘려준다"""
        self.balance *= 1 + BankAccount.interest
```

## 타입 힌팅 적용 후 코드

```python
class BankAccount:
    """은행 계좌 클래스"""
    interest = 0.02

    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """예치금 인스턴스 변수 balance를 파라미터 amount 만큼 늘려준다"""
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """예치금 인스턴스 변수 balance를 파라미터 amount 만큼 눌려준다"""
        if self.balance < amount:
            print("Insufficient balance!")
        else:
            self.balance -= amount

    def add_interest(self) -> None:
        """예치금 인스턴스 변수 balance를 이자율 만큼 늘려준다"""
        self.balance *= 1 + BankAccount.interest
```

+ ***타입 힌팅***을 사용하기 위해서는 `__init__()` 메소드 헤더 부분처럼 

+ `name: str balance: float` 

+ 이렇게 파라미터 이름 뒤에 콜론을 쓰고, 타입을 써주면 됩니다. 

+ `self`는 타입 힌팅을 안 했는데요. 어차피 인스턴스 자신을 나타내니까 따로 해줄 필요가 없습니다.

+ 메소드의 리턴값은 함수 정의 부분 뒤에 화살표를 쓰고 타입을 써주면 됩니다. 

+ 지금처럼 **리턴하는 것이 없을 때**는 이걸 표시하기 위해 그냥 None이라고 쓰면 되죠.

## 타입 힌팅 적용 클래스 사용

+ `BankAccount`를 사용하는 코드를 한 번 볼까요? 의도한 것과 다른 타입들을 사용해 볼게요.

```python
# 타입이 타입 힌팅으로 써준 것과는 다르게 파라미터 balance가 문자열로 넘어갔다
bank_account = BankAccount("Hong Gildong", "1000")

print(bank_account.balance) # 1000
bank_account.deposit("00") 
print(bank_account.balance) # 100000
```

+ 위 코드를 보면 `__init__()` 의 파라미터 `balance` , 

+ 그리고 `deposit()` 의 `amount` 에 타입 힌팅으로 표시한 실수형과는 다른 문자열 데이터를 넘겨줬습니다.

+ 사실 이 코드도 실행해도 아무 문제 없이 똑같이 실행되긴 하는데요. 

+ 문자열과 숫자형은 `+` 연산자가 다르게 작동하기 때문에 결과가 엉뚱하게 나옵니다.

+ 그럼 이걸 사용하는 개발자는 잘못된 타입을 쓰고 있다는 걸 어떻게 알 수 있을까요? 

+ 바로 IDE에서 보여주는 경고 메시지를 통해서입니다. 

+ 토픽 가이드처럼 코드를 IDE를 통해서 작성하고 있었다면 코드 줄이 생기고 이걸 살펴보면 

+ `"Expected type float, got str instead"`라는 경고가 나오죠.

+ 클래스를 올바르게 사용하려면 **타입 힌팅한대로 파라미터를 전달**해야 합니다.

+ 실행에 직접적인 영향을 주진 않지만 개발자들이 변수, 메소드 등을 사용할 때 의도와 다른 타입을 사용하려고 할 때 코드를 실행시키지 않아도 알아차릴 수 있게 도와줍니다. 

+ 파이썬 3.5 이전 버전에서는 작동하지 않는다는 단점이 있고 사용할 수 있어도 동적 타입 언어인 파이썬에 어울리지 않는다는 의견도 있긴 한데요. 

+ 변수나 메소드를 사용하는데 도움이 되는 기능임은 분명합니다.