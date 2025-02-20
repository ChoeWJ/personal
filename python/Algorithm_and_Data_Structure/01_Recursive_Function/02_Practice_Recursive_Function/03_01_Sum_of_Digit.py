"""
실습 설명
0보다 큰 정수 n을 파라미터로 받아서 n의 각 자릿수의 합을 구해서 
리턴하는 함수 sum_digits()를 작성해 주세요.

예를 들어, sum_digits(123)은 1 + 2 + 3 = 6을 리턴합니다.
"""

def sum_digits(n):
    result = 0
    num = str(n)
    index = int(num[-1:])
    result += index
    if len(num) <= 1:
        return result
    return result + sum_digits(num[:-1])

# 테스트 코드
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

# 출력 결과
"""
14
15
16
11
20
"""

"""
def sum_digits(n):
    # 베이스 케이스
    if n < 10:
        return n
    
    # 재귀 케이스
    return sum_digits(n // 10) + (n % 10)
"""

