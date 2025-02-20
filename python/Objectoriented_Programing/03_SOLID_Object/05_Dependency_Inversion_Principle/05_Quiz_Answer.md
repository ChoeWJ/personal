# 해설

+ 일단 `의존 관계 역전 원칙`을 지키려면 일단 추상화 레이어 역할을 할 **추상 클래스**를 만들어야 합니다. 

+ `상위 모듈인 ExportController 클래스`와 하위 모듈이 될 다양한 종류의 변환기 클래스 사이에서 추상화 레이어가 될 `추상 클래스 Exporter`를 만들어 봅시다. 

+ 아래 코드처럼 `Exporter 추상 클래스`를 만들었습니다.

# 변환기(Exporter) 추상 클래스

```python
from abc import ABC, abstractmethod

class Exporter(ABC):
    @abstractmethod
    def export(self, new_name:str, document: Document):
        """각 변환 타입에 맞는 형식으로 문서를 변환한 후 리턴한다"""
        pass
```

+ `상위 모듈인 ExportController 인스턴스`는 이 `추상 클래스`를 상속받은 클래스의 인스턴스만을 변환기로 사용해야 합니다. 

+ 그리고 그 인스턴스를 사용할 때 `Exporter 추상 클래스`에 있는 메소드만을 호출해야 합니다.


+ 그리고 하위 모듈이 될 여러 종류의 변환기 클래스들은 모두 `Exporter 추상 클래스`를 상속받아야 합니다. 

+ 이런 식으로 상위 모듈과 **하위 모듈 모두 추상화 레이어에 의존하게 해야** 하는 겁니다.

# CSV 변환기(CSVExporter) 클래스

```python
class CSVExporter(Exporter):
    """문서를 csv 형식으로 변환하는 클래스"""
    def export(self, new_name, document):
        """문서를 변환한 후 주어진 이름으로 리턴한다"""
        print("\nCSV 파일로 변환 중~")

        new_content = document.content.replace("|", ",")
        exported_document = Document(new_name, new_content)

        print("변환 완료!\n")

        return exported_document
```

+ 일단 `CSVExporter 클래스`가 `Exporter 추상 클래스`를 상속받도록 만듭시다. 

+ 그리고 `추상 메소드 export()` 를 오버라이딩해야 하는데요. 

+ 그런데 `export() 메소드`는 `CSVExporter클래스`에 원래 있었기 때문에 그냥 두면 되겠죠?

# HTML 변환기(HTMLExporter) 클래스

```python
class HTMLExporter(Exporter):
    """문서를 HTML 형식으로 변환하는 클래스"""
    def export(self, new_name, document):
        """문서를 변환한 후 주어진 이름으로 리턴한다"""
        print("\nHTML 문서 변환 중~")

        new_content = """
<!DOCTYPE html>
<html>
<head>
<title>Title of the document</title>
</head>

<body>
{}
</body>

</html>
        """.format(document.content)
        exported_document = Document(new_name, new_content)

        print("변환 완료!\n")

        return exported_document
```

+ `HTMLExporter 클래스`도 마찬가지로 `Exporter 추상 클래스`를 상속받게 합니다. 

+ 그리고 `convert() 메소드`의 이름을 `export()`로 바꿔 주기만 하면 됩니다.

+ 이제 `ExportController 클래스`의 `set_exporter() 메소드`의 파라미터 부분에 `type hinting`을 추가합시다.

```python
def set_exporter(self, exporter: Exporter):
    """변환하고 싶은 파일 타입에 맞는 변환기를 설정한다"""
    self.exporter = exporter
```
+ 이렇게 하면 이제 다른 개발자들이 `ExportController 클래스`는 변환기로 `Exporter 추상 클래스`를 상속받는 인스턴스만 사용해야 한다는 걸 알 수 있겠죠?

# 변환기 컨트롤러(ExportController) 클래스

```python
class ExportController:
    """문서를 특정 파일 형식으로 변환하는 클래스"""
    def __init__(self):
        self.exporter = None

    def set_exporter(self, exporter: Exporter):
        """변환하고 싶은 파일 타입에 맞는 변환기를 설정한다"""
        self.exporter = exporter

    def run_export(self, new_name, document):
        """파일을 변환해서 리턴한다"""
        if self.exporter == None:
            print("변환기를 정해주세요")
            return document

        return self.exporter.export(new_name, document)
```

+ `ExportController 클래스`의  `run_export() 메소드`는 `Exporter 추상 클래스`에 정의된 `export() 메소드`를 사용해야 합니다. 

+ 그래야 `추상 클래스 Exporter`에 의존하게 되겠죠? 

+ 그런데 이미` export()`라는 메소드를 쓰고 있으니 그냥 두면 됩니다.

+ 자, 이제 의존 관계 역전 원칙을 지키도록 모든 코드를 수정했습니다.

# 모범 답안

```python
from abc import ABC, abstractmethod

class Document:
    def __init__(self, name, content):
        self._name = name
        self._content = content

    @property
    def content(self):
        """문서의 내용을 리턴한다"""
        return self._content

    def __str__(self):
        """문서의 정보를 문자열로 리턴한다"""
        return "문서 이름: {}\n문서 내용:\n{}".format(self._name, self._content)


class Exporter(ABC):
    @abstractmethod
    def export(self, new_name:str, document: Document):
        """각 변환 타입에 맞는 형식으로 문서를 변환한 후 리턴한다"""
        pass


class CSVExporter(Exporter):
    """문서를 csv 형식으로 변환하는 클래스"""
    def export(self, new_name, document):
        """문서를 변환한 후 주어진 이름으로 리턴한다"""
        print("\nCSV 파일로 변환 중~")

        new_content = document.content.replace("|", ",")
        exported_document = Document(new_name, new_content)

        print("변환 완료!\n")

        return exported_document


class ExportController:
    """문서를 특정 파일 형식으로 변환하는 클래스"""
    def __init__(self):
        self.exporter = None

    def set_exporter(self, exporter: Exporter):
        """변환하고 싶은 파일 타입에 맞는 변환기를 설정한다"""
        self.exporter = exporter

    def run_export(self, new_name, document):
        """파일을 변환해서 리턴한다"""
        if self.exporter == None:
            print("변환기를 정해주세요")
            return document

        return self.exporter.export(new_name, document)


class HTMLExporter(Exporter):
    """문서를 HTML 형식으로 변환하는 클래스"""
    def export(self, new_name, document):
        """문서를 변환한 후 주어진 이름으로 리턴한다"""
        print("\nHTML 문서 변환 중~")

        new_content = """
<!DOCTYPE html>
<html>
<head>
<title>Title of the document</title>
</head>

<body>
{}
</body>

</html>
        """.format(document.content)
        exported_document = Document(new_name, new_content)

        print("변환 완료!\n")

        return exported_document
        

# 변환기 컨트롤러 인스턴스 정의
export_handler = ExportController()

# csv 변환기 인스턴스 정의
csv_exporter = CSVExporter()
html_exporter = HTMLExporter()

# 변환할 문서 인스턴스 정의
document = Document(
        "직원정보.txt",
        """
이름|이메일
강영훈|younghoon@codeit.kr
이윤수|yoonsoo@codeit.kr
손동욱|dongwook@codeit.kr"""
        )
        

# 기존 문서 출력
print(document)

# 변환기를 csv 변환기로 설정
export_handler.set_exporter(csv_exporter)

# 주어진 문서를 csv 문서로 변환
exported_document = export_handler.run_export("직원정보.csv", document)
# 변환된 문서 출력
print(exported_document)

export_handler.set_exporter(html_exporter)
exported_document = export_handler.run_export("직원정보.html", document)
print(exported_document)

print(CSVExporter.mro())
print(HTMLExporter.mro())
```

```python
"""
실습 결과
문서 이름: 직원정보.txt
문서 내용:

이름|이메일
강영훈|younghoon@codeit.kr
이윤수|yoonsoo@codeit.kr
손동욱|dongwook@codeit.kr

CSV 파일로 변환 중~
변환 완료!

문서 이름: 직원정보.csv
문서 내용:

이름,이메일
강영훈,younghoon@codeit.kr
이윤수,yoonsoo@codeit.kr
손동욱,dongwook@codeit.kr

HTML 문서 변환 중~
변환 완료!

문서 이름: 직원정보.html
문서 내용:

<!DOCTYPE html>
<html>
<head>
<title>Title of the document</title>
</head>

<body>

이름|이메일
강영훈|younghoon@codeit.kr
이윤수|yoonsoo@codeit.kr
손동욱|dongwook@codeit.kr
</body>

</html>
        
[<class '__main__.CSVExporter'>, <class '__main__.Exporter'>, <class 'abc.ABC'>, <class 'object'>]
[<class '__main__.HTMLExporter'>, <class '__main__.Exporter'>, <class 'abc.ABC'>, <class 'object'>]
"""
```
+ 의존 관계 역전 원칙을 따르도록 코드를 고쳐서 `ExportController 클래스`의 코드를 수정하지 않아도 새로운 변환기 클래스를 사용할 수 있게 되었습니다. 

+ 그리고 코드의 마지막 부분을 보면 `CSVExporter 클래스`의 상속 관계와 `HTMLExporter 클래스`의 상속 관계를 보기 위해 `mro() 메소드`를 호출했는데요. 

+ 실행 결과를 보니 두 클래스 모두 `Exporter 추상 클래스`를 잘 상속받고 있네요.

+ 아래처럼 간단하게 확인해 볼 수 있어요.

    + 상위 모듈이 추상화 레이어(Exporter 추상 클래스)에 의존한다는 것은 아래의 `type hinting`으로 알 수 있습니다.

    ```python
        def set_exporter(self, exporter: Exporter):
            """변환하고 싶은 파일 타입에 맞는 변환기를 설정한다"""
            self.exporter = exporter
    ```

+ 하위 모듈이 추상화 레이어(Exporter 추상 클래스)에 의존한다는 것은 아래같은 mro 메소드의 실행 결과로 알 수 있습니다.

```python
"""
[<class '__main__.CSVExporter'>, <class '__main__.Exporter'>, <class 'abc.ABC'>, <class 'object'>]
[<class '__main__.HTMLExporter'>, <class '__main__.Exporter'>, <class 'abc.ABC'>, <class 'object'>]
"""
```

