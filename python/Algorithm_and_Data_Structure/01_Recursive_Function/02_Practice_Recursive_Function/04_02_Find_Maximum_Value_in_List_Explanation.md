+ 먼저 이 문제를 어떻게 재귀적으로 접근할 수 있을지 생각해 봅시다. 

+ `my_list`에 **n 개의 요소**가 있고, **첫 (n-1) 개의 요소들** 중 최댓값을 알고 있다고 가정해 볼게요. 

+ 주어진 정보를 어떻게 활용해야 전체 리스트의 최댓값을 찾을 수 있을까요?

+ 예를 들어, `my_list = [2, 5, 1, 3, 4]`이고 **첫 n-1개의 요소들** 중 최댓값 `max_list([2, 5, 1, 3]) = 5`를 찾았다고 가정한다면 

+ 이 `5`와 마지막 요소인 `4`를 비교해서 전체 리스트의 최댓값을 찾을 수 있습니다. 

+ `5 > 4`이므로 전체 리스트의 최댓값은 `5`입니다.

+ 따라서 `하위 문제`는 **첫 (n-1) 개의 요소들** 중 최댓값을 찾는 것이고, 

+ 그 최댓값과 마지막 요소를 비교하면 전체 리스트의 최댓값을 찾을 수 있습니다.

+ 다음에는 `베이스 케이스`와 `재귀 케이스`를 정해야 합니다. 

+ 어떤 리스트에 대해 최댓값을 바로 알 수 있을까요? 

+ 리스트에 요소가 **1개만 있는 경우** 최댓값은 해당 요소입니다. 

+ 따라서 `베이스 케이스`는 `len(my_list) == 1`이고 `재귀 케이스`는 `len(my_list) > 1`입니다.

```python
def max_list(my_list):
    # 베이스 케이스 
    if len(my_list) == 1:
        return my_list[0]
    
    # 재귀 케이스
```

+ 재귀 케이스의 경우 **처음 (n-1) 개 요소** 중에서 최댓값을 계산하고, 

+ 이 값을 **리스트의 마지막 요소와 비교**하여 전체 최댓값을 찾으면 되는데요. 

+ 이때 **처음 (n-1) 개 요소** 중 최댓값을 변수에 저장해 두면 편리합니다.

```python
def max_list(my_list):
    # 베이스 케이스
    if len(my_list) == 1:
        return my_list[0]
    
    # 재귀 케이스
    max_sublist = max_list(my_list[:-1]) # 첫 (n-1) 개 요소들의 최댓값
```

+ **처음 (n-1) 개 요소**를 리스트로 만들기 위해 슬라이스 연산자 `:`를 사용했습니다.

+ 이제 간단한 if문을 사용하여 **처음 (n-1) 개 요소들**의 최댓값 `max_sublist`와 마지막 요소 `my_list[-1]`의 값을 비교할 수 있습니다.

```python
def max_list(my_list):
    # 베이스 케이스
    if len(my_list) == 1:
        return my_list[0]

    # 재귀 케이스
    max_sublist = max_list(my_list[:-1])
    if max_sublist >= my_list[-1]:
        return max_sublist
    else:
        return my_list[-1]
```

# 모범 답안

```python
def max_list(my_list):
    # 베이스 케이스
    if len(my_list) == 1:
        return my_list[0]

    # 재귀 케이스
    max_sublist = max_list(my_list[:-1])
    if max_sublist >= my_list[-1]:
        return max_sublist
    else:
        return my_list[-1]


# 테스트 코드
print(max_list([1, 4, 3, 2, 5, 0, 2]))
print(max_list([-1, -3, -10, -5, -9]))
print(max_list([3, 7, 3, 7, 7]))
print(max_list([1, 2.7, -3, 2.8, 1.6]))
print(max_list([32, 2, 3, 0 , 1]))
```