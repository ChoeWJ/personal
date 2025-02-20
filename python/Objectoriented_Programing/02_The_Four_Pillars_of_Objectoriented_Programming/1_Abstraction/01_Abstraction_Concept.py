"""
프로그래밍에서의 추상화는 코드를 사용하거나 쓸때
몰라도 되는 정보는 감추고, 꼭 알아야 할 부분만 드러내는 것
"""

# 함수 추상화
# 화면의 리스트를 오름차순으로 정렬해 주는 함수
def sort(my_list):
    for i in range(1, len(my_list)):    # 1부터 리스트 내 변수 갯수만큼을 i로 순환
        value = my_list[i]  # value 변수에 리스트의 i번 인덱스를 대입
        j = i - 1   # j 변수는 i에서 1만큼 뺀 숫자
        while j >= 0 and value < my_list[j]:    # j가 0보다 크거나 같고, value가 j번 인덱스의 값보다 작으면
            my_list[j + 1] = my_list[j] # j + 1 번째 리스트를 j번째 리스트로 저장
            j -= 1 # j를 -1 만큼 감소
        my_list[j + 1] = value  # j + 1 번째 인덱스는 value값으로 저장
    return my_list  # 순환한 리스트를 리턴

my_list = [10, 5, 13, 8, 2]
print("정렬하기 전 리스트", my_list)

sort(my_list)
print("정렬한 후 리스트", my_list)

"""
def sort(my_list):
    # 리스트의 두 번째 요소부터 마지막 요소까지 반복 (첫 번째 요소는 이미 정렬된 상태로 간주)
    for i in range(1, len(my_list)):    
        # 현재 위치의 값을 변수에 저장 (정렬된 부분과 비교할 값)
        value = my_list[i]  
        # 정렬된 부분의 마지막 요소를 가리키는 인덱스
        j = i - 1
        # 정렬된 부분을 역순으로 탐색하며, 현재 값(value)이 정렬된 값보다 작은 경우 위치를 이동
        while j >= 0 and value < my_list[j]:
            # 정렬된 부분에서 값을 한 칸씩 오른쪽으로 이동
            my_list[j + 1] = my_list[j]
            # 이전 인덱스로 이동하여 계속 비교
            j -= 1
        # 올바른 위치에 현재 값(value)을 삽입
        my_list[j + 1] = value
    # 정렬이 완료된 리스트 반환
    return my_list
"""
# 빈 리스트 인스턴스 생성
list = []

# append함수를 이용해서 리스트를 채운다.
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

print(list)

# reverst함수를 리스트내의 값을 역순으로 뒤집는다
list.reverse()

print(list)

# pop함수를 이용해서 1번 인덱스 값을 지운다
list.pop(1)

print(list)