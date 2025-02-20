"""
실습 설명
한국의 최대 온라인 게임업체 넥손에서 일하는 대위는 최근 새 프로젝트인 '은행스토리'에 개발자로 참여하게 되었는데요. 
대위가 맡은 부분은 게임 캐릭터를 '클래스'로 작성하는 것입니다. 
이미 객체의 속성과 행동을 어떻게 할지에 대해서는 생각을 마친 상태입니다.

다음 조건들과 출력 예시에 맞게 GameCharacter 클래스를 작성하세요.

    - 인스턴스 변수(타입)

        - name(문자열): 캐릭터의 이름
        - hp(숫자형): 캐릭터의 체력
        - power(숫자형): 캐릭터의 공격력
        
    - 인스턴스 메소드

        - __init__: 사용할 모든 인스턴스 변수를 설정한다.
        - is_alive: 게임 캐릭터의 체력이 0보다 큰지(살았는지 죽었는지) 확인한다.
            - 0 초과이면 True를, 0 이하라면 False를 리턴한다.
        - get_attacked: 게임 캐릭터의 체력이 0보다 큰 상태라면 파라미터로 받은 공격력만큼 체력을 깎는다.
            - 조건:
                - is_alive 메소드를 사용해서 인스턴스가 살아있을 때만 체력을 깎는다. 이미 캐릭터가 죽었으면 죽었다는 메시지를 출력한다.
                - 남은 체력보다 공격력이 더 크면 체력(hp)을 0으로 설정한다.
        -attack: 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다.
            - 조건:
                - is_alive 메소드를 이용해서 살아있는 인스턴스만 공격을 할 수 있도록 한다.
                - get_attacked 메소드를 사용한다.
        - __str__: 게임 캐릭터의 의미 있는 정보를 포함한 문자열을 리턴한다.
"""
# 게임 캐릭터 클래스
class GameCharacter:
    
    # 인스턴스 변수 생성
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
        
    # 게임 캐릭터의 체력이 0보다 큰지(살았는지 죽었는지) 확인
    def is_alive(self):
        return self.hp > 0    # 살아있다면 True, 죽었다면 False를 리턴
    
    # 게임 캐릭터가 살아있으면 공격한 캐릭터의 공격력만큼 체력을 깎는 메소드
    def get_attacked(self, damage):
        """
        조건:    
            1. 이미 캐릭터가 죽었으면 죽었다는 메시지를 출력한다
            2. 남은 체력보다 공격력이 더 크면 체력은 0이 된다
        """
        if self.is_alive():    # 캐릭터가 살아있다면
            self.hp = self.hp - damage if self.hp >= damage else 0    # hp가 공격력보다 크다면 공격력만큼 hp를 깎고 아닐시 체력은 0이 된다.
        else:    # 캐릭터가 죽었다면
            print(f"{self.name}님은 이미 죽었습니다.")    # 캐릭터가 죽었다는 메시지를 출력
    
    # 게임 캐릭터가 살아있으면 파라미터로 받은 다른 캐릭터의 체력을 자신의 공격력만큼 깎는다
    def attack(self, other_character):
        if self.is_alive():    # 캐릭터가 살아있다면
            other_character.get_attacked(self.power)    # 공격하는 캐릭터의 공격력만큼 상대의 hp를 감소시키기 위해 get_attacked메서드를 호출한다.
        
    # 게임 캐릭터의 의미있는 정보를 포함한 문자열을 리턴한다
    def __str__(self):
        return f"{self.name}님의 hp는 {self.hp}만큼 남았습니다."
        

# 게임 캐릭터 인스턴스 생성                        
character_1 = GameCharacter("Ww영훈전사wW", 200, 30)
character_2 = GameCharacter("Xx지웅최고xX", 100, 50)

# 게임 캐릭터 인스턴스들 서로 공격
character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)

# 게임 캐릭터 인스턴스 출력
print(character_1)
print(character_2)