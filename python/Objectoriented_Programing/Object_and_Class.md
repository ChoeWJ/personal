# 객체와 클래스

---


###  종류

| 항목 | 설명 |
|----------|----------|
| **클래스(Class)**   | 제품의 설계도   |
| **객체(Object)**   | 설계도로 만든 작품   |
| **인스턴스(Instance)**   | 메모리에 살아있는 객체   |
| **속성(Attribute)**   | 클래스 내의 변수   |
| **메서드(Method)**   | 클래스 내의 함수   |
| **생성자(Constructor)**   | 객체를 만들 때 실행되는 함수   |


# 클래스(Class)

---

+ **정의**
    + 객체를 만들어 내기 위한 툴 즉, 객체의 설계도(buleprint)나 템플릿의 역할을 한다.
    + 객체가 가질 속성(attribute)과 메서드(method)의 집합
+ **특징** 
    + 개념적으로 하나의 형식이나 툴로, 구체적인 데이터나 상태를 가지고 있지는 않는다.
+ **예시**
    ```python
    class Car:
    """Car 클래스 생성"""
    def __init__(self, color, brand):
        """Car 클래스의 색상과 제조업체 변수 초기화"""
        self.color = color
        self.brand = brand
    
    def drive(self):
        """drive 메서드 생성"""
        print(f"{self.brand} car is driving")

## `__init__` ?
### Python의 클래스(class)에서 객체가 처음 생성될 때 값들을 자동으로 호출되는 **초기화 메서드**

### `__init__` 메서드의 역할
+ 객체의 속성 설정 
    + `__init__` 메서드에서 **self** 키워드를 사용하여 객체의 속성(변수)을 정의하고 초기 값을 설정
+ 객체마다 고유한 속성 값 부여
    + 각 객체가 독립적인 상태(속성 값)을 가질  수 있게 한다
+ 생성자 역할
    + 클래스가 호출될 때 객체를 생성하고 기본 상태를 설정하는 생성자 역할을 수행
+ 예시

    ```python
    class Person:
    """Person 클래스 생성"""
    def __init__(self, name, age):
        """
        __init__ 메서드 생성을 통한 객체의 속성 정의
            두 개의 매개변수 name과 age를 받는다
            이 매개변수를 통해 각 객체의 name과 age 속성을 설정
        """
        self.name = name   # 객체의 name 속성 초기화
        self.age = age     # 객체의 age 속성 초기화

    # Person 객체 생성
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)

1. 객체의 초기화
    + Person("Alice", 25)를 호출하면 `__init__`메서드가 실행
2. 속성 할당
    + self.name = name은 객체의 name 속성에 "Alice" 라는 값을 할당
    + self.age = age는 객체의 age 속성에 25라는 값을 할당

+ person1 객체는 name 속성이 "Alice", age 속성이 25로 초기회된 상태로 생성된다.
+ 위와 같은 방식으로 person2 객체 또한 name이 "Bob", age 가 30으로 초기화 된다.

### `__init__` 메서드의 초기화 기능의 장점
+ 각 객체가 **고유한 초기값**을 가질 수 있게 된다. 이 초기값들은 객체가 생성될 때 필요한 정보(이름, 나이)등을 담고 있어, 객체가 생성된 후에 바로 사용할 수 있다. 
+ 각 객체는 `__init__`에서 설정된 속성 값을 통해 서로 독립적인 상태를 유지하므로, **객체마다 다른 데이터를 저장하고 다룰 수 있게** 한다.

# 객체(Object)

___

+ 정의
    + 클래스에 의해 생성된 구체적인 데이터를 가진 존재
    + 프로그램에서 실제로 사용되는 데이터를 포함한 실체로, 클래스를 바탕으로 만들어진 실질적인  요소
+ 특징
    + 클래스의 인스턴스(instance), 
    + 클래스에 정의된 속성과 메서드를 실제로 사용할 수 있는 상태로 가지고 있다.
+ 예시

    ```python
    # Person 객체 생성
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)

# 인스턴스(Instance)

---

+ 정의
    + **특정 클래스**의 객체
    + 즉, 객체가 특정한 클래스의 예시라는 점을 **강조**할 때 인스턴스라고 부른다.
+ 특징
    + 클래스와 객체의 관계를 나타낼 때 사용된다.
+ 예시
    ```python
    class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def drive(self):
        print(f"{self.brand} c is driving!")

    # Car 클래스에서 객체 생성
    my_car = Car("Red", "Toyota")

+ my_car는 Car 클래스에서 만들어진 구체적인 데이터 이므로 **Car 클래스(class)의 인스턴스(instance)**
+ 동시에 my_car는 Python에서 데이터와 메서드를 가진 실체화된 **객체(Object)**

# 객체와 인스턴스의 구체적인 차이점

---

### 객체(Object)
+ 인스턴스보다 더 넓은 개념
+ 프로그래밍에서 상태와 행동을 포함한 모든 데이터 구조를 말한다
+ 숫자, 문자열, 리스트, 사용자 정의 클래스 등
+ 실체화된 데이터

### 인스턴스(Instance)
+ **특정** 클래스를 기반으로 생성된 객체
+ 객체의 하위 개념
+ 어떤 클래스에서 만들어졌느냐를 기준으로 정의된 객체를 의미

### 예시를 통한 구분
+ 
    ```python
    class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def drive(self):
        print(f"{self.brand} car is driving!")

    # Car 클래스에서 객체 생성
    my_car = Car("Red", "Toyota")

+ my_car는 Car 클래스에서 만들어진 구체적인 데이터이므로 **Car 클래스의 인스턴스**
+ 동시에 Python에서 데이터와 메서드를 가진 실체화된 **객체**

# **인스턴스**가 아닌 경우

---

## 1. 기본 데이터 타입의 리터럴 값
+ Python에서는 모든 것이 객체로 다뤄지기 때문에 5, "Hello"와 같은 리터럴 값도 객체이다
+ 하지만 이것은 특정 클래스에 속한 **인스턴스** 라기 보다는 Python 내에서 기본적으로 존재하는 **기본 객체** 이다

+ 예시
    ```python
    num = 5
    text = "Hello"

    print(isinstance(num, int))  # True, num은 int 클래스의 인스턴스
    print(isinstance(text, str)) # True, text는 str 클래스의 인스턴스

## 2. 내장 함수 객체
+ Python의 내장 함수도 객체로 취급된다.
+ 하지만 이것 역시 특정 클래스의 인스턴스가 아니며 단순히 **함수 객체** 이다.

+ 예시
    ```python
    def custom_function():
        pass

    print(isinstance(custom_function, object))  # True, custom_function은 객체입니다
    print(isinstance(custom_function, int))     # False, 이는 int 클래스의 인스턴스가 아닙니다

## 3. 모듈 객체
+ 모듈 역시 Python에서 객체로 취급되지만, 특정 클래스의 인스턴스는 아니다
+ 아래의 math는 Python 내에서 정의된 모듈 객체로, 특정 클래스의 인스턴스가 아닌 독립적인 객체이다
+ 예시

    ```python
    import math

    print(isinstance(math, object))  # True, math는 객체입니다
    print(isinstance(math, int))     # False, 이는 int 클래스의 인스턴스가 아닙니다



