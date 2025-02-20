+ 파이썬에서는 하나의 자식 클래스가 여러 부모 클래스를 상속받는 것도 가능합니다. 
+ 이것을 다중 상속이라고 하는데요. `Cashier` 과 `DeliveryMan` 클래스 다중 상속받는 예시를 통해서 어떻게 작동하는지 알아봅시다.

---
+ 상속받을 때 클래스 이름 뒤에 괄호를 쓰고, 그 사이에 부모 클래스 이름을 썼잖아요? 
+ 여기 한 개가 아닌 상속받고 싶은 모든 클래스의 이름을 써주면 됩니다. 아래처럼요.

```python
# 다중 상속을 받는 계산대-배달원 클래스 
class CashierDeliveryMan(DeliveryMan, Cashier):     
	
	def __init__(self, name, wage, on_standby, number_sold=0):        
		Employee.__init__(self, name, wage)        
		self.on_standby = on_standby         
		self.number_sold = number_sold
```


+ 일단은 두 클래스의 인스턴스 변수를 모두 초기화해야 되기 때문에 `__init__()` 메소드만 오버라이드할게요.

```python
cashier_delivery_man = CashierDeliveryMan("강영훈", 7000, True, 10)  

cashier_delivery_man.take_order(3000)  # 돈이 충분하지 않습니다. 돈을 다시 계산해서 주세요!

cashier_delivery_man.deliver_to("코드잇 건물 101호")  # 코드잇 건물 101호로 배달 나갑니다! 
cashier_delivery_man.deliver_to("코드잇 건물 101호")  # 이미 배달하러 나갔습니다! 
cashier_delivery_man.back()  

print(cashier_delivery_man)  # 코드잇 버거 배달원 직원: 강영훈

```

+ CashierDeliveryMan 인스턴스가 `Cashier` 와 `DeliveryMan`의 기능들을 다 잘 수행합니다.

# 다중 상속 문제

+ 그런데 짚고 넘어가야 할 부분이 있습니다. 
+ 바로 마지막 줄, CashierDeliveryMan 인스턴스를 출력하는 이 **print(cashier_and_delivery_man)** 부분입니다.
+ 이 부분의 실행 결과는 **코드잇 버거 배달원: 강영훈**인데요.
+ CashierDeliveryMan에는 일단 `__str__()` 메소드가 없습니다. 
+ 하지만 부모 클래스인 `Cashier` 와 `DeliveryMan`에는 모두 `__str__()` 메소드가 있죠

+ 실행결과를 보면 DeliveryMan 클래스의 `__str__()` 메소드가 실행된 걸 알 수 있습니다.
+ DeliveryMan`과 `Cashier 에 모두 `__str__()` 메소드가 있는데 왜 전자에 있는 게 실행될 걸까요?

+ 저번에 배운 `mro()` 메소드를 사용하면 알 수 있습니다.

```python
print(CashierDeliveryMan.mro())
```

```python
[<class '__main__.CashierDeliveryMan'>, <class '__main__.DeliveryMan'>, <class '__main__.Cashier'>, <class '__main__.Employee'>, <type 'object'>]
```

+ DeliveryMan 클래스가 Cashier 클래스보다 MRO에서의 우선순위가 높기 때문에 여기 정의된 `__str__()` 메소드가 실행된 겁니다.
+ 이렇게 `mro()` 메소드를 호출하면 어느 클래스의 메소드가 호출될지 확실히 알 수 있습니다. 
+ 하지만 `mro()`는 클래스 간의 상속받는 순서에 따라 변합니다. 
+ 지금 같은 경우는 DeliveryMan 클래스를 먼저 상속받았기 때문에 `mro()`에서 순서가 Cashier 보다 앞입니다. 
+ 순서를 바꾸고 다시 `mro()` 메소드를 호출하면

```python
class CashierDeliveryMan(Cashier, DeliveryMan):
```

```python
<class '__main__.CashierDeliveryMan'>, <class '__main__.Cashier'>, <class '__main__.DeliveryMan'>, <class '__main__.Employee'>, <type 'object'>]
```

+ 이번엔 Cashier 클래스가 DeliveryMan 클래스보다 먼저 나옵니다. 
+ 이렇게 되면 인스턴스를 출력하면 Cashier 클래스의 `__str__()` 메소드가 호출되죠.

+ `super()` 함수도 이 `mro()` 순서에서 바로 뒤에 있는 클래스를 리턴하는데요. 
+ 어떤 클래스의 메소드가 호출되는지 뿐만 아니라 `super()` 함수를 사용했을 때 어떤 클래스가 리턴되는지까지 신경 써야 되죠.

+ **이 문제를 해결하는 방법이 하나 있기는 합니다.**
+ 자식 클래스에서 겹치는 메소드를 오버라이딩하는 겁니다. 
+ 그럼 부모 클래스들을 생각할 필요도 없이 
+ 무조건 더 우선순위에 있는 자식 클래스의 메소드가 실행될 테니까요.

+ 파이썬에서 다중 상속을 한다면 부모 클래스들이 같은 메소드 이름을 갖지 않도록 하거나, 
+ 같은 메소드 이름이 있다면 자식 클래스에서 아예 오버라이딩해 두는 게 좋습니다. 
+ 그래야 어느 부모 클래스의 메소드를 호출하는 건지, 혼동이 생기는 문제를 막을 수 있습니다.