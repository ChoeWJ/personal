# 선형 탐색 (Linear Search)

## **정의**
선형 탐색(Linear Search)은 배열 또는 리스트와 같은 데이터 구조에서 **첫 번째 요소부터 시작하여 순차적으로 탐색**하며 목표 값을 찾는 알고리즘입니다.  
데이터가 정렬되어 있지 않아도 사용할 수 있는 가장 기본적인 탐색 방법입니다.

---

## **특징**
1. **직접 접근 방식**:
   - 데이터를 순차적으로 하나씩 비교하기 때문에 단순하고 직관적입니다.
2. **정렬 여부와 무관**:
   - 배열이 정렬되어 있지 않아도 작동합니다.
3. **효율성**:
   - 데이터의 크기가 커질수록 비효율적입니다.
4. **시간 복잡도**:
   - **최선의 경우**: \(O(1)\) (탐색 값이 첫 번째 요소에 있는 경우)
   - **최악의 경우**: \(O(n)\) (탐색 값이 마지막 요소에 있거나 없는 경우)
   - **평균의 경우**: \(O(n/2) \approx O(n)\)

---

## **동작 원리**
1. 배열의 첫 번째 요소부터 시작하여 탐색 값을 비교.
2. 탐색 값과 일치하는 요소를 찾으면 인덱스를 반환.
3. 배열의 끝까지 탐색했음에도 값을 찾지 못하면 실패로 간주.

---

## **장점**
1. 구현이 간단하고 직관적입니다.
2. 정렬 여부에 상관없이 사용할 수 있습니다.
3. 작은 데이터셋에서는 유용합니다.

---

## **단점**
1. 데이터 크기가 커지면 탐색 시간이 길어질 수 있습니다.
2. 비효율적이며, 고급 탐색 알고리즘(예: 이진 탐색)보다 느립니다.

---

## **구현 예제 (C 언어)**

```c
#include <stdio.h>

// 선형 탐색 함수
int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) { // 목표 값과 현재 요소 비교
            return i; // 인덱스 반환
        }
    }
    return -1; // 값이 없으면 -1 반환
}

int main() {
    int data[] = {5, 8, 12, 14, 18, 22};
    int size = sizeof(data) / sizeof(data[0]);
    int target = 14;

    int result = linearSearch(data, size, target);
    if (result != -1) {
        printf("값 %d는 인덱스 %d에 있습니다.\n", target, result);
    } else {
        printf("값 %d는 배열에 없습니다.\n", target);
    }
    return 0;
}
```

## **구현 예제 (Python)**
```python
# 선형 탐색 함수
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # 값을 찾으면 해당 인덱스 반환
    return -1  # 값을 찾지 못하면 -1 반환

# 배열 및 대상 값
data = [10, 20, 30, 40, 50]
target = 30

# 선형 탐색 실행
result = linear_search(data, target)
if result != -1:
    print(f"값 {target}은 인덱스 {result}에 위치합니다.")
else:
    print(f"값 {target}은 배열에 없습니다.")
```
