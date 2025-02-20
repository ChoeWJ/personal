# 해설

+ 이번 과제에서는 `뚱뚱한 인터페이스인 IPrinter 인터페이스`를 사용하는 대가로 `LGPrinter 클래스`에서 사용하지도 않을 `scan() 메소드`를 오버라이딩해야 했는데요. 

+ `인터페이스 분리 원칙`에 따라 `IPrinter 인터페이스`를 두 개의 `더 작은 인터페이스`로 나누겠습니다. 

+ `print_file() 메소드`는 인쇄 기능을 나타내는 현재의 `IPrinter 인터페이스`에 그대로 두겠습니다. 

+ 대신 `scan() 메소드`는 `IScanner라는 새 인터페이스`를 만들어서 거기에 넣겠습니다.

## 프린터(IPrinter) 인터페이스

```python
from abc import ABC, abstractmethod
# 프린터 인터페이스
class IPrinter(ABC):
    @abstractmethod
    def print_file(self, file:str) -> bool:
        """문서 출력 메소드"""
        pass

# 스캐너 인터페이스
class IScanner(ABC):
    @abstractmethod
    def scan(self, content:str) -> bool:
        """문서 스캔 메소드"""
        pass
```

+ 이런 식으로 `인터페이스`를 `작은 단위의 인터페이스 2개`로 분리했습니다. 

+ 바뀐 코드에 맞게 다른 코드들도 수정합시다.

## 삼성 프린터(SamsungPrinter) 클래스

```python
class SamsungPrinter(IPrinter, IScanner):

    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력 중입니다!".format(file))
            return True
        return False

    def scan(self, content):
        """문서 스캔 메소드"""
        if self.is_connected:
            print("{}을/를 이미지 파일로 저장합니다.".format(content))
            return True
        return False
```

+ `SamsungPrinter 클래스`의 내용은 바꿀 게 없습니다. 

+ 하지만 `IPrinter  인터페이스`가 쪼개졌으므로 이제는 `IPrinter 인터페이스`뿐만 아니라 `IScanner 인터페이스`도 상속받아야 합니다. 

+ 지금 클래스 이름 오른쪽에 이렇게 두 인터페이스를 상속받도록 적었습니다.

```python
class SamsungPrinter(IPrinter, IScanner):
LGPrinter 클래스는 IPrinter 인터페이스만 상속받으면 되겠죠? 그냥 기존의 코드를 그대로 두면 됩니다.

LG 프린터(LGPrinter) 클래스
class LGPrinter(IPrinter):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력합니다.".format(file))
            return True
        return False
```

+ 이제 `LGPrinter 클래스`에서 `scan() 메소드`를 불필요하게 오버라이딩할 필요가 없어졌네요!

+ 그럼 이제 원래의 실행 코드에서 `LGPrinter 인스턴스`로 `scan() 메소드`를 호출하는 코드를 주석 처리 합시다. 

+ 그리고 전체 코드를 실행해 볼게요.

# 모범 답안

```python
from abc import ABC, abstractmethod


# 프린터 인터페이스
class IPrinter(ABC):
    @abstractmethod
    def print_file(self, file:str) -> bool:
        """문서 출력 메소드"""
        pass


# 스캐너 인터페이스
class IScanner(ABC):
    @abstractmethod
    def scan(self, content:str) -> bool:
        """문서 스캔 메소드"""
        pass
    

class SamsungPrinter(IPrinter, IScanner):

    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력 중입니다!".format(file))
            return True
        return False

    def scan(self, content):
        """문서 스캔 메소드"""
        if self.is_connected:
            print("{}을/를 이미지 파일로 저장합니다.".format(content))
            return True
        return False
    
    
class LGPrinter(IPrinter):
    def __init__(self, has_ink, has_paper, is_connected):
        self.has_ink = has_ink
        self.has_paper = has_paper
        self.is_connected = is_connected

    def print_file(self, file):
        """문서 출력 메소드"""
        if self.has_ink and self.has_paper and self.is_connected:
            print("문서 {}을/를 출력합니다.".format(file))
            return True
        return False
    

samsung_printer = SamsungPrinter(True, True, True)
lg_printer = LGPrinter(True, True, True)

samsung_printer.print_file("4월 보고서.docx")
lg_printer.print_file("4월 보고서.docx")

samsung_printer.scan("스캔 테스트 문서")
#lg_printer.scan("스캔 테스트 문서")    

print(SamsungPrinter.mro())
print(LGPrinter.mro())
```

# 실습 결과

```python
"""
문서 4월 보고서.docx을/를 출력 중입니다!
문서 4월 보고서.docx을/를 출력합니다.
스캔 테스트 문서을/를 이미지 파일로 저장합니다.
[<class '__main__.SamsungPrinter'>, <class '__main__.IPrinter'>, <class '__main__.IScanner'>, <class 'abc.ABC'>, <class 'object'>]
[<class '__main__.LGPrinter'>, <class '__main__.IPrinter'>, <class 'abc.ABC'>, <class 'object'>]
"""
```

+ 이전처럼 잘 실행되네요. 

+ 그런데 `mro() 메소드`의 실행 결과는 변화가 생겼을 겁니다. 

+ 그건 바로 `SamsungPrinter 클래스`가 `IScanner라는 새로운 인터페이스를 상속`받는다는 거죠.

+ `인터페이스 분리 원칙`은 **깔끔한 코딩 스타일을 유도하는 원칙**입니다. 

+ `인터페이스 분리 원칙`을 지키지 않는다고 해서 코드의 동작에 실질적인 악영향을 주지는 않습니다. 

+ 하지만 이 원칙을 지키지 않으면 코드가 불필요하게 길어지고, 

+ 객체가 가지는 기능의 범위를 정확하게 파악하기 어렵게 만듭니다. 

+ 이는 코드의 가독성을 해치는 원인이 됩니다. 

+ 코드의 가독성은 신속한 코드 이해와 유지 보수에 있어 정말 중요한 부분입니다. 

+ `인터페이스 분리 원칙`을 지키면서 누가 봐도 이해하기 쉬운 코드를 작성하도록 합시다.