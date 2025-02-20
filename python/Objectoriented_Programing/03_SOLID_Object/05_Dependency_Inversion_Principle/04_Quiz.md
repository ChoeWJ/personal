# 실습 설명

+ 컴퓨터로 작업을 하다보면 작업한 문서를 다른 형식으로 변환해야 하는 경우가 많은데요. 

+ 이번 과제에서는 주어진 문서를 원하는 파일 형식으로 변환하는 프로그램을 만들어 보겠습니다. 

+ 변환 프로그램을 몇 가지 기능으로 쪼개서 각각의 클래스로 만들어 볼게요. 

+ 일단 아래 세가지 클래스를 정의하도록 하겠습니다.

    + 문서 클래스

    + 변환기 컨트롤러 클래스

    + CSV 변환기 클래스

# 문서(Document) 클래스

```python
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
        return "문서 이름: {}\n문서 내용:\n{}".format(self.name, self.content)
```

+ `Document 클래스`는 **문서의 이름**과 **내용을 담고 있는 클래스**입니다. 

+ 이 클래스에는 문서의 내용을 리턴하는 *getter 메소드*, *content*와 문서 정보를 문자열로 리턴하는 *__str__ 메소드*가 있습니다.

# CSV 변환기(CSVExporter) 클래스

```python
class CSVExporter:
    """문서를 csv 형식으로 변환하는 클래스"""
    def export(self, new_name, document):
        """문서를 변환한 후 주어진 이름으로 리턴한다"""
        print("\nCSV 파일로 변환 중~")

        new_content = document.content.replace("|", ",")
        exported_document = Document(new_name, new_content)

        print("변환 완료!\n")

        return exported_document
```

+ `CSVExporter 클래스`의 *export() 메소드*는 파라미터로 받는 문서를 CSV 파일로 변환합니다.

+ *replace() 메소드*는 파이썬에서 문자열을 나타내는 **str 클래스의 메소드**이고, 

+ 주어진 문자열 중 첫 번째 파라미터로 받은 문자열을 모두 두 번째 문자열로 바꿔 줍니다. 

+ 그러니까 아래 부분은 문서 내용 중 | 문자열을 모두 ,로 바꾼다는 뜻입니다.

```python
document.content.replace("|", ",")
```

+ 문자열은 불변 타입이기 때문에 이 메소드를 호출해도 메소드를 호출한 기존 문자열 인스턴스가 바뀌지는 않고 새로운 문자열 인스턴스를 리턴합니다.

+ *export() 메소드*는 그리고 나서 아래 부분처럼 새로운 **Document 인스턴스를 생성**해서 리턴합니다.
```python
exported_document = Document(new_name, new_content)
```

# 변환기 컨트롤러(ExportController) 클래스

```python
class ExportController:
    """문서를 특정 파일 형식으로 변환하는 클래스"""
    def __init__(self):
        self.exporter = None

    def set_exporter(self, exporter):
        """변환하고 싶은 파일 타입에 맞는 변환기를 설정한다"""
        self.exporter = exporter

    def run_export(self, new_name, document):
        """파일을 변환해서 리턴한다"""
        if self.exporter == None:
            print("변환기를 정해주세요")
            return document

        return self.exporter.export(new_name, document)
```

+ `ExportController 클래스`는 설정된 문서 변환기를 사용해서 문서를 변환합니다. 

+ *set_exporter()*를 통해서 원하는 문서 변환기를 설정할 수 있고, 

+ *run_export() 메소드*는 설정된 문서 변환기를 사용해서 문서를 변환하고 리턴합니다.

# 테스트 코드

+ 앞에서 작성한 내용들을 테스트해 보겠습니다.

```python
# 변환기 컨트롤러 인스턴스 정의
export_handler = ExportController()

# csv 변환기 인스턴스 정의
csv_exporter = CSVExporter()

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
"""
```

+ 주어진 파일을 csv 파일로 변환했죠? 

+ 하지만 안타깝게도 이 코드는 이번 챕터에서 배운 **의존 관계 역전 원칙을 어긴 코드**입니다.

+ `ExportController 클래스`라는 **상위 모듈**이, 

+ `CSVExporter 클래스`라는 **하위 모듈**의 구현 내용(export() 메소드)에 직접적으로 의존하고 있기 때문입니다.

+ **상위 모듈**이 **하위 모듈**의 구현 내용에 직접적으로 의존하게 되면 그 **하위 모듈**의 구현 내용에 문제가 생기는 순간, 그 **상위 모듈**이 언제 오작동할지 모르는 불안한 상태에 빠지게 됩니다. 

+ 이 과제에서 그런 예시를 생각해 봅시다.

+ 아래와 같이 `HTML 변환기 클래스`를 정의했다고 가정해 봅시다.

```python
HTML 변환기(HTMLExporter) 클래스
class HTMLExporter:
    """문서를 HTML 형식으로 변환하는 클래스"""
    def convert(self, new_name, document):
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

+ `ExportController 클래스`가 `HTMLExporter 클래스`를 사용하려면 어떻게 해야 할까요? 

+ 지금 `ExportController 클래스`는 아래 코드처럼 *run_export() 메소드*에서 `CSVExporter 클래스`의 *export() 메소드*를 사용하고 있습니다.

```python
def run_export(self, new_name, document):
        """파일을 변환해서 리턴한다"""
        if self.exporter == None:
            print("변환기를 정해주세요")
            return document

        return self.exporter.export(new_name, document)\
```

+ 그래서 지금 상태에서 `HTMLExporter 클래스`를 사용하려면 `ExportController 클래스`의 코드를 수정해야 합니다. 

+ `ExportController 클래스`의 기존 코드를 수정하지 않고도 `HTMLExporter 인스턴스`를 사용할 수는 없을까요?

+ 이번 챕터에서 배운 내용을 바탕으로 의존 관계 역전 원칙에 맞게 `ExportController 클래스`와 `CSVExporter 클래스`, `HTMLExporter 클래스`의 코드를 수정하세요.

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
"""
```

# 문제 풀이
```python
from abc import ABC, abstractmethod

class Exporter(ABC):
    @abstractmethod
    def convert(self, new_name, new_content):
        pass

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


class CSVExporter(Exporter):
    """문서를 csv 형식으로 변환하는 클래스"""
    def convert(self, new_name, document):
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

        return self.exporter.convert(new_name, document)


class HTMLExporter(Exporter):
    """문서를 HTML 형식으로 변환하는 클래스"""
    def convert(self, new_name, document):
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