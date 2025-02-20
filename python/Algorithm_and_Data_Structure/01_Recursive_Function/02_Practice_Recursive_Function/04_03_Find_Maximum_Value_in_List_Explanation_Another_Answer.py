def max_list(my_list):
    # 베이스 케이스
    if len(my_list) == 1:
        return my_list[0]  
    #가장 왼쪽과 오른쪽 값 비교
    elif my_list[0] > my_list[-1]:  
        return max_list(my_list[:-1])   # 가장 왼쪽값이 크면 가장 오른쪽 값 빼고 max_list 함수 호출
    return max_list(my_list[1:])        # 가장 오른쪽값이 크면 가장 왼쪽 값 빼고 max_list 함수 호출


# 테스트 코드
print(max_list([1, 4, 3, 2, 5, 0, 2]))
print(max_list([-1, -3, -10, -5, -9]))
print(max_list([3, 7, 3, 7, 7]))
print(max_list([1, 2.7, -3, 2.8, 1.6]))
print(max_list([32, 2, 3, 0 , 1]))
