# 실습 설명

+ 이번 과제에서는 프린터 클래스들을 만들어봅시다. 

+ 요즘은 프린터의 기능이 많아져서 인쇄 기능뿐만 아니라 스캔 기능이 있는 것들도 많은데요. 

+ 이런 프린터를 `추상화한 IPrinter 인터페이스`를 만들어 봅시다. 

+ 다음 코드를 보시죠.

# 프린터(IPrinter) 인터페이스

```python
from abc import ABC, abstractmethod

class IPrinter(ABC):
    @abstractmethod
    def print_file(self, file:str) -> bool:
        """문서 출력 메소드"""
        pass

    @abstractmethod
    def scan(self, content:str) -> bool:
        """문서 스캔 메소드"""
        pass
```

+ 그런데 프린터 중에는 인쇄 기능만 있고 스캔 기능은 없는 것들도 있습니다. 

+ 그런데 이런 프린터들이 단지 프린터라는 이유만으로 `IPrinter 인터페이스`를 상속받게 되면 정작 스캔 기능이 없는데도 `scan() 메소드`를 오버라이딩해야 합니다. 

+ 예를 들어 `LGPrinter`는 스캔 기능이 없다고 가정해 볼게요. 

+ 그런데 지금 템플릿을 보면 `LGPrinter 클래스`는 불필요하게 `scan() 메소드`를 오버라이딩하고 있습니다. 

+ 이것이 바로 필요없는 메소드의 구현을 강제하는 코드 **즉, 인터페이스 분리 원칙을 위반한 코드**입니다.

+ 이번 챕터에서 배운 내용을 바탕으로 템플릿의 코드를 인터페이스 분리 원칙에 부합하는 코드로 리팩토링해 보세요!

+ 참고로 코드를 리팩토링할 때, 코드 마지막 줄의 `LGPrinter 인스턴스`로 `scan() 메소드`를 호출하는 부분은 주석 처리하시면 됩니다.

# 실습 결과

```python
"""
문서 4월 보고서.docx을/를 출력 중입니다!
문서 4월 보고서.docx을/를 출력합니다.
스캔 테스트 문서을/를 이미지 파일로 저장합니다.
[<class '__main__.SamsungPrinter'>, <class '__main__.IPrinter'>, <class '__main__.IScanner'>, <class 'abc.ABC'>, <class 'object'>]
[<class '__main__.LGPrinter'>, <class '__main__.IPrinter'>, <class 'abc.ABC'>, <class 'object'>]
"""
