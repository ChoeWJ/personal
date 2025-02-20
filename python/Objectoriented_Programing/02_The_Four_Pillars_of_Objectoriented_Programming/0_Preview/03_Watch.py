"""
실습 설명
"0 또는 시작값"에서부터 특정 "최댓값"까지 숫자를 증가시키는 Counter 클래스를 정의했습니다. 그렇다면 Counter 클래스로 어떻게 시계의 시, 분, 초를 나타낼 수 있을까요? 그 전에 일단 '시계'라는 객체도 클래스로 정의해야겠죠? 이전의 레슨에서 보았듯이, 만들려는 시계 프로그램은 다음 조건들을 만족해야 합니다.

현재 시간을 설정할 수 있다.
현재 시간을 변경할 수 있다.
현재 시간에 1초씩 더할 수 있다.
Counter 클래스를 조합하면 시계의 기능을 완성할 수 있는데요. 시계를 나타내는 클래스의 이름은 Clock으로 하겠습니다. Clock 클래스가 가질 속성과 행동을 먼저 봅시다.

속성
시계는 현재 시간을 속성으로 가집니다. Counter 클래스를 사용해서 시, 분, 초를 나타낼 수 있습니다.

초: 1부터 59까지 셀 줄 아는 Counter 클래스의 인스턴스
분: 1부터 59까지 셀 줄 아는 Counter 클래스의 인스턴스
시: 1부터 23까지 셀 줄 아는 Counter 클래스의 인스턴스
행동
1초 증가시키기
시간을 1초씩 증가시킵니다.
이때 주의할 점은 시간을 증가시킬 때 59초가 60초가 되면 초를 다시 00초로 바꾼 후에 분을 1분 증가시키고, 59분이 60분이 되면 분을 다시 00분으로 바꾼 후에 시를 1시간 증가시키는 것입니다. 이것은 당연한 시간의 원리이니 따로 설명하지 않겠습니다. 이 부분을 구현할 때 Counter 클래스의 tick 메소드의 리턴값(True 또는 False)이 어떻게 활용될지 생각해 보세요.
값 변경하기: 이미 Counter 클래스에는 값을 설정하는 메소드가 있습니다. 시계 클래스에서 시간을 설정할 때 시, 분, 초를 각각 따로 설정하는 건 귀찮겠죠? 시, 분, 초의 값을 한번에 설정하는 메소드를 만듭시다.
이러한 속성과 행동을 가지는 Clock 클래스를 정의해 보세요!
"""

class Counter:
    """
    시계 클래스의 시,분,초를 각각 나타내는데 사용될 카운터 클래스
    """

    def __init__(self, limit):
        """
        인스턴스 변수 limit(최댓값), value(현재까지 카운트한 값)을 설정한다.
        인스턴스를 생성할 때 인스턴스 변수 limit만 파라미터로 받고, value는 초깃값 0으로 설정한다.
        """    
        self.limit = limit
        self.value = 0


    def set(self, new_value):
        """
        파라미터가 0 이상, 최댓값 미만이면 value에 설정한다.
        아닐 경우 value에 0을 설정한다.
        """
        if 0 <= new_value < self.limit:
            self.value = new_value
        else:
            self.value = 0


    def tick(self):
        """
        value를 1 증가시킨다.
        카운터의 값 value가 limit에 도달하면 value를 0으로 바꾼 뒤 True를 리턴한다.
        value가 limit보다 작은 경우 False를 리턴한다.
        """
        self.value += 1

        if self.value == self.limit:
            self.value = 0
            return True
        return False


    def __str__(self):
        """
        value를 최소 두 자릿수 이상의 문자열로 리턴한다. 
        일단 str 함수로 숫자형 변수인 value를 문자열로 변환하고 zfill을 호출한다. 
        """
        return str(self.value).zfill(2)
    

class Clock:
    """
    시계 클래스
    """
    HOURS = 24 # 시 최댓값
    MINUTES = 60 # 분 최댓값
    SECONDS = 60 # 초 최댓값

    def __init__(self, hour, minute, second):
        """
        각각 시, 분, 초를 나타내는 카운터 인스턴스 3개(hour, minute, second)를 정의한다.
        현재 시간을 파라미터 hour시, minute분, second초로 지정한다.
        """
        self.hour = Counter(Clock.HOURS)
        self.minute = Counter(Clock.MINUTES)
        self.second = Counter(Clock.SECONDS)

        self.set(hour, minute, second)
        
        

    def set(self, hour, minute, second):
        """현재 시간을 파라미터 hour시, minute분, second초로 설정한다."""
        self.hour.set(hour)
        self.minute.set(minute)
        self.second.set(second)


    def tick(self):
        """
        초 카운터의 값을 1만큼 증가시킨다.
        초 카운터를 증가시킬 때, 분 또는 시가 바뀌어야하는 경우도 처리한다.
        """
        if self.second.tick():
            if self.minute.tick():
                self.hour.tick()

    def __str__(self):
        """
        현재 시간을 시:분:초 형식으로 리턴한다. 시, 분, 초는 두 자리 형식이다.
        예시: "03:11:02"
        """
        return f"{self.hour}:{self.minute}:{self.second}"
        

# 초가 60이 넘을 때 분이 늘어나는지 확인하기
print("시간을 1시 30분 48초로 설정합니다")
clock = Clock(1, 30, 48)
print(clock)

# 13초를 늘린다
print("13초가 흘렀습니다")
for i in range(13):
    clock.tick()
print(clock)

# 분이 60이 넘을 때 시간이 늘어나는지 확인
print("시간을 2시 59분 58초로 설정합니다")
clock.set(2, 59, 58)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)

# 시간이 24가 넘을 때 00:00:00으로 넘어가는 지 확인
print("시간을 23시 59분 57초로 설정합니다")
clock.set(23, 59, 57)
print(clock)

# 5초를 늘린다
print("5초가 흘렀습니다")
for i in range(5):
    clock.tick()
print(clock)

"""
시간을 1시 30분 48초로 설정합니다
01:30:48
13초가 흘렀습니다
01:31:01
시간을 2시 59분 58초로 설정합니다
02:59:58
5초가 흘렀습니다
03:00:03
시간을 23시 59분 57초로 설정합니다
23:59:57
5초가 흘렀습니다
00:00:02
"""