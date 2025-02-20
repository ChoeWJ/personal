# 실습 설명

+ 다음은 코드잇 대학의 학생 관리 프로그램에서 사용되는 `학생(Student) 클래스`입니다. 

+ `학생 클래스`에는 다음과 같은 기능들이 있습니다.

    + 학생 기본 정보 수정

    + 학점 추가

    + 평균 학점 계산

    + 성적표 출력

+ 그런데 `학생 클래스`는 너무 많은 책임을 갖고 있는 `신 객체(God object)`에 해당합니다. 

+ `학생 클래스`를 단일 책임 원칙에 맞게 바꿔 보세요. 

+ 책임을 나누는 방식은 다양할 수 있습니다. 

+ 일단은 여러분이 생각하는 기준으로 책임을 나눠서 과제를 풀어 보세요. 

+ 그 다음 해설을 참고로 보시기 바랍니다.

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
        

## 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

## 학생 성적 추가
younghoon.add_grade(3.0)
younghoon.add_grade(3.33)
younghoon.add_grade(3.67)
younghoon.add_grade(4.3)

## 학생 성적표 
younghoon.print_report_card()
```
# 실습 결과
```python
"""
코드잇 대학 성적표

학생 이름:강영훈
학생 번호:20130024
소속 학과:컴퓨터 공학과
평균 학점:3.575
"""
```
+ 단일 책임 원칙을 적용하면 현재 `Student 클래스`를 사용하는 실행 코드도 수정해 주어야 합니다. 

+ 하지만 실행 결과가 바뀌는 것은 아닙니다.

# 문제 풀이

```python
class Student:
    def __init__(self, name, id, major):
        self.info = Info(name, id, major)
        self.grade = Grade()
        self.print = Print(self.info, self.grade)

class Info:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

    def change_student_info(self, new_name, new_id, new_major):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.major = new_major
class Grade:
    
    def __init__(self):
        self.grades = []
    
    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산 메소드"""
        return sum(self.grades) / len(self.grades)
    
class Print:
    
    def __init__(self, info, grade):
        self.info = info
        self.grade = grade
        
    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}"\
        .format(self.info.name, self.info.id, self.info.major, self.grade.get_average_gpa()))
    
        

## 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.info.change_student_info("강영훈", 20130024, "컴퓨터 공학과")

## 학생 성적 추가
younghoon.grade.add_grade(3.0)
younghoon.grade.add_grade(3.33)
younghoon.grade.add_grade(3.67)
younghoon.grade.add_grade(4.3)

## 학생 성적표 
younghoon.print.print_report_card()
```