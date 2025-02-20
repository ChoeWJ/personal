![Liskov_Substitution_Principle_001](../../../images/SOLID/03_Liskov_Substitution_Principle/001.jpg)
![Liskov_Substitution_Principle_002](../../../images/SOLID/03_Liskov_Substitution_Principle/002.jpg)
![Liskov_Substitution_Principle_003](../../../images/SOLID/03_Liskov_Substitution_Principle/003.jpg)
![Liskov_Substitution_Principle_004](../../../images/SOLID/03_Liskov_Substitution_Principle/004.jpg)
![Liskov_Substitution_Principle_005](../../../images/SOLID/03_Liskov_Substitution_Principle/005.jpg)
![Liskov_Substitution_Principle_006](../../../images/SOLID/03_Liskov_Substitution_Principle/006.jpg)
![Liskov_Substitution_Principle_007](../../../images/SOLID/03_Liskov_Substitution_Principle/007.jpg)
![Liskov_Substitution_Principle_008](../../../images/SOLID/03_Liskov_Substitution_Principle/008.jpg)
![Liskov_Substitution_Principle_009](../../../images/SOLID/03_Liskov_Substitution_Principle/009.jpg)

```python
class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self._wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self._wage *= self.raise_percentage

    @property
    def wage(self):
        return self._wage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    """리스코프 치환 원칙을 지키지 않는 계산대 직원 클래스"""
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def raise_pay(self, raise_amount):
        """직원 시급을 인상하는 메소드"""
        self.wage += self.raise_amount

    @property
    def wage(self):
        return "시급 정보를 알려줄 수 없습니다"
    
employee1 = Employee("성태호", 7000)
employee2 = Employee("강영훈", 6500)

cashier = Cashier("김대위", 9000)

employee_list = []
employee_list.append(employee1)
employee_list.append(employee2)
employee_list.append(cashier)
```
```python
for employee in employee_list:
    employee.raise_pay()        
```
+ 문제가 발생한다.

    + Employee 쪽은 문제가 없으나 

    + cashier 쪽의 raise_pay()의 파라미터가 빠져서 에러가 발생한다.

    + TypeError: Cashier.raise_pay() missing 1 required positional argument: 'raise_amount'

    + 이것이 리스코프의 치환원칙 위반이다.

```python
total_wage = 0
for employee in employee_list:
    total_wage += employee.wage
    
print(total_wage)
```
+ 역시 문제가 발생한다.

    + cashier 쪽의 __str__쪽에서 문자열로 리턴하고 있어서 에러가 발생한다.
    + TypeError: unsupported operand type(s) for +=: 'int' and 'str'
    + 역시 리스코프의 치환원칙 위반이다.

![Liskov_Substitution_Principle_010](../../../images/SOLID/03_Liskov_Substitution_Principle/010.jpg)
![Liskov_Substitution_Principle_011](../../../images/SOLID/03_Liskov_Substitution_Principle/011.jpg)
![Liskov_Substitution_Principle_012](../../../images/SOLID/03_Liskov_Substitution_Principle/012.jpg)