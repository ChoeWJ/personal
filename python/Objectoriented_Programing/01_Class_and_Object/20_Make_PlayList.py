"""
멜론이나 유튜브 뮤직과 같은 음악 재생 프로그램을 만들려고 합니다. 
이 프로그램에서 사용할 음악을 나타낼 Song 클래스와 플레이리스트를 나타낼 PlayList 클래스를 작성 중인데요.

Song 클래스는 노래 제목(문자열)을 나타내는 title, 
가수(문자열)를 나타내는 artist, 
그리고 발매년도(정수)를 나타내는 year를 인스턴스 변수로 갖습니다.

PlayList 클래스는 Song 인스턴스가 담긴 파이썬 리스트인 songs라는 인스턴스 변수를 갖습니다.

두 클래스의 인스턴스들이 어떻게 작동하는지는 코드를 실행시켜 보면서 익숙해져 보세요.

지금 있는 코드를 바탕으로 계속 프로그램에 여러 기능들을 추가하려고 하는데요. 
사용자들이 손쉽게 두 플레이리스트를 합칠 수 있는 기능을 가장 높은 우선순위로 제공하려고 합니다.

이걸 개발자들이 손쉽게 할 수 있게 하기 위해서 두 플레이리스트를 + 연산자를 통해서 더할 수 있게 하고 싶은데요.

us_pop_2010s이 2010년대 미국 팝 플레이리스트, 
k_pop_2010s가 2010년대 한국 대중 음악 플레이리스트 인스턴스일 때, 
아래 코드로 두 플레이리스트에 있는 모든 노래가 들어있는 새로운 플레이리스트를 리턴되게 하고 싶습니다.

"us_pop_2010s + k_pop_2010s"

바로 전 두 노트 내용들을 참고해서 이 기능을 한번 구현해보세요.
"""

# Song 클래스 생성
class Song:
    # 인스턴스 변수 초기화
    def __init__(self, title, artist, year):
        self.title = title      # 제목
        self.artist = artist    # 가수
        self.year = year        # 연도

    # 인스턴스 변수를 문자열로 변환한 값을 리턴
    def __str__(self):
        return f"{self.title} - {self.artist} ({self.year})"

# 플레이리스트 클래스 생성
class PlayList:
    # 인스턴스 변수 초기화
    def __init__(self, songs):
        self.songs = songs  # 노래 정보 

    # 인스턴스 변수를 문자열로 변환한 값을 리턴
    def __str__(self):
        result = f"플레이리스트 안 노래들:\n\n" # result 변수 생성
        for song in self.songs:     # 전체 노래 정보 리스트에서 순환
            result += f"{song}\n"   # result 변수 안에 노래를 저장
        return result   # 순환한 result 값을 리턴

    # 두 플레이리스트를 하나로 합치는 함수
    def __add__(self, other):
        return PlayList(self.songs + other.songs)

# 실행 코드
rolling_in_the_deep = Song("Rolling in the Deep", "Adele", 2011)
call_me_maybe = Song("Call Me Maybe", "Carly Rae Jepsen", 2012)
get_lucky = Song("Get Lucky", "Daft Punk", 2013)
uptown_funk = Song("Uptown Funk", "Mark Ronson", 2015)

palette = Song("Pallete(팔레트)", "아이유", 2017)
blood_sweat_and_tears = Song("피 땀 눈물", "방탄소년단", 2016)
tt = Song("TT", "트와이스", 2016)

us_pop_2010s = PlayList([rolling_in_the_deep, call_me_maybe, get_lucky, uptown_funk])
k_pop_2010s = PlayList([palette, blood_sweat_and_tears, tt])

pop_2010s = us_pop_2010s + k_pop_2010s
print(pop_2010s)
