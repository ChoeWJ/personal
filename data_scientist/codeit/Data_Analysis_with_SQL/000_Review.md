```sql
-- 데이터 정의 언어 (DDL: Data Definition Language)
CREATE DATABASE company; -- 데이터베이스 생성
USE company;             -- 데이터베이스 선택

CREATE TABLE employees ( -- 테이블 생성
    id INT PRIMARY KEY, 
    name VARCHAR(50), 
    salary DECIMAL(10, 2), 
    department VARCHAR(50), 
    hire_date DATE,        -- 고용 날짜
    last_promotion DATE    -- 최근 승진 날짜
);

ALTER TABLE employees ADD COLUMN birth_date DATE; -- 열 추가

DROP TABLE employees; -- 테이블 삭제

-- 데이터 조작 언어 (DML: Data Manipulation Language)
INSERT INTO employees (id, name, salary, department, hire_date, last_promotion, birth_date) 
VALUES (1, 'Alice', 70000, 'HR', '2020-01-15', '2022-03-01', '1990-05-20'); -- 데이터 삽입

UPDATE employees 
SET last_promotion = '2023-12-01' 
WHERE id = 1; -- 특정 날짜 수정

DELETE FROM employees 
WHERE hire_date < '2019-01-01'; -- 특정 날짜 이전의 데이터 삭제

-- 데이터 조회 (DQL: Data Query Language)
SELECT name, salary 
FROM employees 
WHERE hire_date BETWEEN '2020-01-01' AND '2021-12-31'; -- 날짜 범위 조건

SELECT name, 
       DATEDIFF(NOW(), hire_date) AS days_since_hired -- 고용된 지 며칠 되었는지 계산
FROM employees;

SELECT name, 
       YEAR(hire_date) AS hire_year, 
       MONTH(hire_date) AS hire_month, 
       DAY(hire_date) AS hire_day -- 날짜를 연, 월, 일로 분리
FROM employees;

SELECT * 
FROM employees 
WHERE MONTH(hire_date) = 12; -- 특정 월(12월)에 고용된 직원 조회

SELECT * 
FROM employees 
WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR); -- 지난 1년 내에 고용된 직원 조회

-- 데이터 제어 언어 (DCL: Data Control Language)
GRANT SELECT, INSERT ON employees TO user1; -- 사용자 권한 부여

REVOKE INSERT ON employees FROM user1; -- 사용자 권한 취소

-- 트랜잭션 제어 언어 (TCL: Transaction Control Language)
BEGIN; -- 트랜잭션 시작
UPDATE employees 
SET salary = salary + 10000 
WHERE hire_date < '2020-01-01';

SAVEPOINT before_bonus; -- 롤백 지점 저장

UPDATE employees 
SET salary = salary + 5000 
WHERE last_promotion < '2023-01-01';

ROLLBACK TO before_bonus; -- 특정 시점으로 롤백
COMMIT; -- 변경 사항 저장

-- 기타 명령어
SHOW TABLES; -- 데이터베이스 내 테이블 보기
DESCRIBE employees; -- 테이블 구조 확인
CREATE INDEX idx_hire_date ON employees(hire_date); -- 인덱스 생성
DROP INDEX idx_hire_date ON employees; -- 인덱스 삭제
```
## DATE 관련 주요 함수
	•	NOW(): 현재 날짜와 시간을 반환.
	•	CURDATE(): 현재 날짜만 반환.
	•	DATEDIFF(date1, date2): 두 날짜 간의 차이를 일(day) 단위로 반환.
	•	DATE_ADD(date, INTERVAL expr unit): 특정 날짜에 기간을 추가.
	•	DATE_SUB(date, INTERVAL expr unit): 특정 날짜에서 기간을 뺌.
	•	YEAR(date), MONTH(date), DAY(date): 날짜에서 연도, 월, 일을 추출.
	•	BETWEEN ‘start_date’ AND ‘end_date’: 날짜 범위 조건.
	•	MONTH(date): 특정 월에 해당하는 데이터 조회.

## DDL: 데이터 정의 언어
	•	CREATE TABLE: 테이블 생성 시 날짜 형식의 열 추가.
	•	ALTER TABLE: 날짜 데이터를 다룰 열 추가/수정.

## DML: 데이터 조작 언어
	•	INSERT: 날짜 데이터를 삽입.
	•	UPDATE: 특정 날짜 데이터를 수정.
	•	DELETE: 조건에 따라 날짜 데이터를 삭제.

## DQL: 데이터 조회 언어
	•	날짜 관련 조건과 함수 사용:
	•	DATEDIFF(): 날짜 차이 계산.
	•	YEAR(), MONTH(), DAY(): 날짜를 연/월/일로 분리.
	•	DATE_SUB(): 특정 기간 이전의 데이터 조회.
	•	NOW()와 CURDATE(): 현재 날짜 기준 데이터 조회.

## DCL: 데이터 제어 언어
	•	권한 설정 및 관리.

## TCL: 트랜잭션 제어 언어
	•	트랜잭션을 통해 날짜 데이터 변경을 관리.

## 기타 명령어
	•	SHOW, DESCRIBE: 테이블 및 구조 정보 확인.
	•	CREATE INDEX: 날짜 열에 인덱스 생성으로 조회 성능 개선.