def power(x, n):
    
    if n == 0:
        return 1
    elif n == 1:
        return x
    
    if n >= 2:
        if n % 2 == 0:
            return power(x * x, n // 2)
        return power(x, n = 1) * power(x * x, (n // 2)) 
        


# 테스트 코드
print(power(2, 3))
print(power(5, 0))
print(power(17, 5))
print(power(3, 17))
print(power(4, 18))



# 출력 결과
"""
8
1
1419857
129140163
68719476736
"""