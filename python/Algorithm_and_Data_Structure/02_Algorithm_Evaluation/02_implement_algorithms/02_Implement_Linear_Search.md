+ 반복문을 사용해 선형 탐색 함수를 구현해 보세요.

+ `linear_search()` 함수는 두 개의 파라미터를 받습니다.

    + `target`: 찾고 있는 요소

    + `data`: 탐색할 리스트

+ `data`에 `target` 값이 있는 경우 함수는 `target` 값이 위치한 **인덱스를 리턴**합니다. 

+ `data`에 `target` 값이 없는 경우 `None`을 리턴합니다.

```python
def linear_search(target, data):
    # 여기에 코드를 작성하세요.


# 테스트 코드
print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))

```

## 문제 풀이

```python
def linear_search(target, data):
    if target in data:
        return data.index(target)


# 테스트 코드
print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))
```

# 모범 답안

```python
def linear_search(target, data):
    for i in range(len(data)):
        if data[i] == target:
            return i

# 테스트 코드
print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))
```