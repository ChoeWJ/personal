# 동적 배열 (Dynamic Array)

+ 동적 배열은 실행 중에 크기를 변경할 수 있는 배열입니다. 

+ 정적 배열과 달리, 메모리 크기를 프로그램 실행 중에 동적으로 할당하거나 해제할 수 있는 특징이 있습니다. 

+ `C 언어`에서는 동적 메모리 할당 라이브러리를 사용하여 구현하며, 

+ `Python`에서는 기본적으로 제공되는 리스트가 동적 배열처럼 작동합니다.

---

### **1. C 언어에서 동적 배열 구현**
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i;
    printf("동적 배열의 크기를 입력하세요: ");
    scanf("%d", &n);

    // 메모리 할당
    int* array = (int*)malloc(n * sizeof(int));
    if (array == NULL) {
        printf("메모리 할당 실패!\n");
        return 1;
    }

    // 배열 요소 입력
    printf("배열의 값을 입력하세요:\n");
    for (i = 0; i < n; i++) {
        printf("array[%d]: ", i);
        scanf("%d", &array[i]);
    }

    // 배열 출력
    printf("배열 요소:\n");
    for (i = 0; i < n; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");

    // 메모리 해제
    free(array);

    return 0;
}
```

### 2. Python에서 동적 배열 구현
```python
# 동적 배열 구현 (Python 리스트 사용)

# 사용자로부터 배열 크기 입력
n = int(input("동적 배열의 크기를 입력하세요: "))

# 빈 리스트 생성
array = []

# 배열 요소 입력
print("배열의 값을 입력하세요:")
for i in range(n):
    value = int(input(f"array[{i}]: "))
    array.append(value)

# 배열 출력
print("배열 요소:")
for value in array:
    print(value, end=" ")
print()
```

### **3. 비교**

+ `C 언어`: 메모리를 명시적으로 할당(malloc)하고 해제(free)해야 합니다.

+ `Python`: 메모리 관리가 자동화되어 있고, 리스트(list)는 기본적으로 동적 배열의 성격을 가집니다.

+ 위 코드를 실행하여 **C에서는 메모리 관리의 중요성**을, **Python에서는 간편함**을 체험할 수 있습니다.