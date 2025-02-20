"""
실습 설명
신용 카드를 나타내는 CreditCard 클래스를 만들고 싶습니다. CreditCard 클래스에는 다음과 같은 정보가 저장됩니다.

- 소유자 이름
- 비밀번호
- 카드 한도 정보


아래 조건들에 맞게 CreditCard 클래스를 완성하세요.

1. CreditCard 클래스의 비밀번호, 카드 한도 정보 인스턴스 변수 이름 앞에 밑줄 한 개를 써서 
다른 개발자들에게 해당 변수를 직접 사용하는 것을 자제하라는 표시를 남깁시다. (_password, _payment_limit)

2. @property를 이용해서 앞에 밑줄 하나를 쓴 변수들을 캡슐화하세요.

    변수 _password

        - getter 메소드: 문자열 "비밀번호는 볼 수 없습니다"를 리턴한다.

        - setter 메소드: 파라미터로 받은 값을 변수에 설정한다.

    변수 _payment_limit
    
        - getter 메소드: _payment_limit 변수를 리턴한다.

        - setter 메소드: 파라미터로 받은 값을 변수에 설정한다.
            - 단, setter 메소드에서 파라미터로 받은 값이 0과 MAX_PAYMENT_LIMIT 사이에 있는 값이 아니면 
            - "카드 한도는 0원 ~ 3천만 원 사이로 설정해 주세요!"라는 메시지를 출력한다.
"""

class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        self.name = name
        self._password = password
        self._payment_limit = payment_limit
        
    @property
    def password(self):
        return "비밀번호는 볼 수 없습니다"
    
    @password.setter
    def password(self, new_password):
        self._password = new_password
    
    @property
    def payment_limit(self):
        return self._payment_limit

    @payment_limit.setter
    def payment_limit(self, new_payment_limit):
        if not 0 < new_payment_limit < self.MAX_PAYMENT_LIMIT:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해 주세요!")
        else:
            self._payment_limit = new_payment_limit

card = CreditCard("강영훈", "123", 100000)

print(card.name)
print(card.password)
print(card.payment_limit)

card.name = "성태호"
card.password = "1234"
card.payment_limit = -10

print(card.name)
print(card.password)
print(card.payment_limit)