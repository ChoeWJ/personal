class Clock:
    
    # 시, 분, 초에 해당하는 인스턴스 변수 초기화
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def set(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        
        return(Clock(hour, minute, second))
    
    def tick(self, second):
        for i in len(second) and i <= second:
            self.second += 1
            if self.second == 60:
                self.minute += 1
                self.second = 0
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
            if self.hour == 24:
                self.hour = 0
    
    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"





# 1시 30분 48초인 시계 인스턴스 생성
clock = Clock(1, 30, 48)
    
# 13초를 센다
for i in range(13):
    clock.tick()
    
print(clock)  # 출력: 01:31:01
    
# 2시 3분 58초로 시계 세팅
clock.set(2, 3, 58)
    
# 5초를 늘린다
for i in range(5):
    clock.tick()
    
print(clock)  # 출력: 02:04:03
    
# 23시 59분 57초로 세팅
clock.set(23, 59, 57)
    
# 5초를 센다
for i in range(5):
    clock.tick()
    
print(clock)  # 출력: 00:00:02