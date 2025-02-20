# 해설

## 학생(Student) 클래스
```python
class Student:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major
        self.grades = []

    def change_student_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산 메소드"""
        return sum(self.grades) / len(self.grades)

    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}"\
        .format(self.name, self.id, self.major, self.get_average_gpa()))
```

## 학생 인스턴스 정의

```python
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.change_student_info("강영훈", 20130024, "컴퓨터 공학과")
```

## 학생 성적 추가

```python
younghoon.add_grade(3.0)
younghoon.add_grade(3.33)
younghoon.add_grade(3.67)
younghoon.add_grade(4.3)
```

## 학생 성적표 

```python
younghoon.print_report_card()
```

+ 단일 책임 원칙에 맞게 `Student 클래스`를 수정하려면 이 클래스가 일단 어떤 책임들을 갖고 있는지 살펴봐야겠죠? 

+ 자세히 살펴보면 `Student 클래스`는 다음 **3가지 책임을 갖는 것으로 생각**할 수 있습니다.

    + 학생의 기본 정보(이름, 학생 번호, 소속 학과 ) 관리

    + 학생의 학점 관리

    + 성적표 출력

+ 이렇게 세 가지인데요. 

+ 각 책임들을 하나씩 클래스로 만들어서 쪼개면 단일 책임 원칙을 지킬 수 있게 됩니다. 

+ 첫 번째 책임부터 하나씩 해 봅시다.

---

# 학생 기본 정보(StudentProfile) 클래스

```python
class StudentProfile:
    """학생 기본 정보 클래스"""
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def change_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major
```

+ 학생의 기본 정보 관리를 위한 `StudentProfile 클래스`입니다. 

+ 이름, 학생 번호, 소속 학과를 나타내는 인스턴스 변수와 이를 수정하는 메소드를 갖습니다.

# 학점 관리(GPAManager) 클래스

### 학점 관리(GPAManager) 클래스

```python
class GPAManager:
    """학생 학점 관리 클래스"""
    def __init__(self, grades):
        self.grades = grades

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산"""
        return sum(self.grades) / len(self.grades) 
```

+ 학점 관리를 담당하는 `GPAManager 클래스`인데요. 

+ 각 수업의 학점들이 담긴 **리스트 grades를 인스턴스 변수**로 갖습니다. 

+ 이 리스트에는 학점을 추가하는 메소드와 평균 학점을 계산하는 메소드가 있습니다.

# 성적표 출력(ReportCardPrinter) 클래스

```python
class ReportCardPrinter:
    """성적표 출력 클래스"""
    def __init__(self, student_profile, gpa_manager):
        self.student_profile = student_profile
        self.gpa_manager = gpa_manager

    def print(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}"\
        .format(self.student_profile.name, self.student_profile.id,\
                self.student_profile.major, self.gpa_manager.get_average_gpa()))   
```

+ 마지막은 성적표를 출력하는 `ReportCardPrinter 클래스`입니다. 

+ 성적표를 출력하려면 학생 기본 정보와 학점 정보가 필요합니다.  

+ 위에서 만든 `StudentProfile 클래스`와 `GPAManager 클래스`를 딱 사용하면 되겠죠? 

+ 따라서 성적표 출력 클래스에 별도의 변수나 메소드를 추가할 필요없이 필요한 부분에 이 두 가지 클래스의 인스턴스를 사용하면 됩니다. 

+ `ReportCardPrinter 클래스`는 지금 `__init__ 메소드`에서 두 클래스의 인스턴스를 받습니다. 

+ 그리고 이 인스턴스를 사용해 학생의 기본 정보와 학점 정보를 가져오면 됩니다.

+ 이렇게 하면 각 클래스가 자신의 책임에 더욱 집중할 수 있게 됩니다. 

+ 예를 들어 평균 학점을 구하는 공식이 변경되었다고 합시다. 

+ 그럼 `GPAManager 클래스`의 `get_average_gpa 메소드`의 내용만 변경하면 됩니다. 

+ `ReportCardPrinter 클래스`는 이미 `GPAManager 클래스`의 인스턴스를 통해 `get_average_gpa 메소드`를 사용하고 있었기 때문에 별도로 코드를 손댈 일이 없습니다.

# 학생(Student) 클래스

```python
class Student:
    """코드잇 대학생을 나타내는 클래스"""
    def __init__(self, name, id, major):
        self.profile = StudentProfile(name, id, major)
        self.grades = []
        self.gpa_manager = GPAManager(self.grades)
        self.report_card_printer = ReportCardPrinter(self.profile, self.gpa_manager)
```

+ `Student 클래스`의 책임을 쪼갰으니 이제 다시 `Student 클래스`를 정의해 봅시다. 

+ 위에서 만든 3가지 클래스의 인스턴스들을 `Student 클래스`의 인스턴스 변수로 두면 됩니다. 

+ `Student 클래스`가 변경되면 실행 코드도 바꿔야겠죠? 

+ 이전 실행 코드에서는 `Student 클래스`의 메소드를 직접 호출했습니다. 

+ 하지만 이제 `Student 클래스` 내부에서 각 책임을 담당하는 인스턴스를 사용하면 됩니다. 

+ `Student 클래스`의 기존 메소드에 대응하는 각 인스턴스와 그 메소드가 무엇일지 생각하며 문제의 실행코드를 수정해 보면, 아래 코드처럼 됩니다.

```python
# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.profile.change_info("강영훈", 20130024, "컴퓨터 공학과")

## 학생 성적 추가
younghoon.gpa_manager.add_grade(3.0)
younghoon.gpa_manager.add_grade(3.33)
younghoon.gpa_manager.add_grade(3.67)
younghoon.gpa_manager.add_grade(4.3)

## 학생 성적표 
younghoon.report_card_printer.print()
```

# 모범 답안

+ 완성된 코드 전체는 다음과 같습니다.

```python
class StudentProfile:
    """학생 기본 정보 클래스"""
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def change_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major
        
        
class GPAManager:
    """학생 학점 관리 클래스"""
    def __init__(self, grades):
        self.grades = grades

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산"""
        return sum(self.grades) / len(self.grades)  
    
    
class ReportCardPrinter:
    """성적표 출력 클래스"""
    def __init__(self, student_profile, gpa_manager):
        self.student_profile = student_profile
        self.gpa_manager = gpa_manager

    def print(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}"\
        .format(self.student_profile.name, self.student_profile.id,\
                self.student_profile.major, self.gpa_manager.get_average_gpa()))   
    

class Student:
    """코드잇 대학생을 나타내는 클래스"""
    def __init__(self, name, id, major):
        self.profile = StudentProfile(name, id, major)
        self.grades = []
        self.gpa_manager = GPAManager(self.grades)
        self.report_card_printer = ReportCardPrinter(self.profile, self.gpa_manager)


# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.profile.change_info("강영훈", 20130024, "컴퓨터 공학과")

# 학생 성적 추가
younghoon.gpa_manager.add_grade(3.0)
younghoon.gpa_manager.add_grade(3.33)
younghoon.gpa_manager.add_grade(3.67)
younghoon.gpa_manager.add_grade(4.3)

# 학생 성적표 
younghoon.report_card_printer.print()
```

# 실습 결과

+ 위의 코드를 실행하면 결과는 아래와 같습니다.

```python
"""
코드잇 대학 성적표

학생 이름:강영훈
학생 번호:20130024
소속 학과:컴퓨터 공학과
평균 학점:3.575
"""
```