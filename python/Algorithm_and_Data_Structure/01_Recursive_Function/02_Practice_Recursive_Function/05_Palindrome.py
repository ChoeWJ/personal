"""
팰린드롬(palindrome)이란 앞으로 읽는 것과 뒤로 읽는 것이 같은 문자열입니다. 
예를 들어, '기러기', '토마토', '스위스', '12344321'은 모두 팰린드롬입니다. 
빈 문자열 ''도 팰린드롬으로 간주할 수 있습니다.

문자열 my_str을 파라미터로 받아서 my_str이 팰린드롬인지 판별하는 함수 is_palindrome() 을 작성해 주세요.

for문이나 while문은 사용하지 말아 주세요!
"""

def is_palindrome(my_str):
    if len(my_str) <= 1:
        return True


    if my_str[-1] == my_str[0]:
        return is_palindrome(my_str[1:-1])
    return False


# 테스트 코드
print(is_palindrome('기러기'))
print(is_palindrome('토마토'))
print(is_palindrome('바나나'))
print(is_palindrome('racecar'))
print(is_palindrome('radar'))
print(is_palindrome('stars'))
print(is_palindrome('123321'))



# 출력 결과
"""
True
True
False
True
True
False
True
"""