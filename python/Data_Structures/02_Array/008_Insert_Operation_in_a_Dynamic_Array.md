+ 동적 배열의 끝에 

    + 추가하는 것은 `append`

    + 삽입하는 것은 `insertion`

# 1. 정적 배열에 여유 공간이 있을때

+ 시간 복잡도: $O(n)$

# 2. 배열이 가득 차 있을떄

+ 시간 복잡도: $O(n)$

### C 언어 구현

```c
#include <stdio.h>
#include <stdlib.h>

// 동적 배열 구조체 정의
typedef struct {
    int *array;
    int size;
    int capacity;
} DynamicArray;

// 동적 배열 초기화
DynamicArray* initArray(int initialCapacity) {
    DynamicArray* arr = (DynamicArray*)malloc(sizeof(DynamicArray));
    arr->array = (int*)malloc(initialCapacity * sizeof(int));
    arr->size = 0;
    arr->capacity = initialCapacity;
    return arr;
}

// 동적 배열 삽입 함수
void insert(DynamicArray* arr, int value) {
    if (arr->size == arr->capacity) {
        // 용량 증가 (2배 크기)
        arr->capacity *= 2;
        arr->array = (int*)realloc(arr->array, arr->capacity * sizeof(int));
    }
    arr->array[arr->size++] = value;
}

// 테스트 코드
int main() {
    DynamicArray* arr = initArray(2);
    insert(arr, 10);
    insert(arr, 20);
    insert(arr, 30); // 크기 재조정 발생

    for (int i = 0; i < arr->size; i++) {
        printf("%d ", arr->array[i]);
    }

    // 메모리 해제
    free(arr->array);
    free(arr);
    return 0;
}
```

### Python 언어 구현
```python
class DynamicArray:
    def __init__(self):
        self.array = [None] * 2  # 초기 용량 2
        self.size = 0
        self.capacity = 2

    def insert(self, value):
        # 배열 크기 초과 시 크기 재조정
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = value
        self.size += 1

    def _resize(self):
        # 배열 크기 2배로 늘리기
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def __str__(self):
        return str([self.array[i] for i in range(self.size)])

# 테스트 코드
if __name__ == "__main__":
    dyn_array = DynamicArray()
    dyn_array.insert(10)
    dyn_array.insert(20)
    dyn_array.insert(30)  # 크기 재조정 발생
    dyn_array.insert(40)

    print("동적 배열:", dyn_array)  # 출력: [10, 20, 30, 40]
```

+ 파이썬의 기본 리시트는 이미 동적 배열로 동작한다

+ 따라서 별도의 구현 없이 리스트의 `append()` 메서드를 사용하면 동일한 동작 수행이 가능하다

```python
# 파이썬 내장 리스트 사용
dyn_array = []

# 삽입 연산 (append)
dyn_array.append(10)
dyn_array.append(20)
dyn_array.append(30)  # 내부적으로 크기 재조정이 발생
dyn_array.append(40)

print("동적 배열:", dyn_array)  # 출력: [10, 20, 30, 40]
```