# MY SQL 시작하기
```SQL
-- coupang_main schema(DB)의 member 테이블에서 모든 열과 모든 행을 가져온다
SELECT *    
FROM coupang_main.member;
/*-----------------------------------------------------------------------------*/
SELECT email, age, address -- email, age, address 컬럼만 즉, 보고 싶은 컬럼만 보여준다
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
```
# 조건 표현식: WHERE
```SQL
SELECT *
FROM copang_main.member
WHERE email = 'taehos@hanmail.net'; -- 특정 조건만 만족하는 row들만 조회
/*-----------------------------------------------------------------------------*/
/*
    - copang_main이라는 데이터 베이스를 확실하게 사용하겠다 라고 선언하는 것
    - 주로 작은 프로젝트나 스키마가 단일 환경일 경우에 사용
*/
USE copang_main
SELECT *
FROM member
WHERE email = 'taehos@hanmail.net';
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
WHERE age >= 27; -- 나이가 27이상인 row들만 조회
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
WHERE age BETWEEN 30 AND 39; -- 나이가 30세 이상부터 39세 즉, 30대 회원들을 조회
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
WHERE age NOT BETWEEM 30 AND 39; -- 30대 회원이 아닌 경우만 조회
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
WHERE sign_up_day > '2019-01-01'; -- 2019년 1월 1일 이후로 가입한 회원 조회
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
WHERE sign_up_day BETWEEN '2018-01-01' AND '2018-12-31'; -- 2018년도에 가입한 회원 조회
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
WHERE address -- 주소 컬럼을 기준으로
LIKE '서울%'; -- 문자열의 시작이 서울로 시작하고 그 뒤에 임의의 길이를 가진 모든 문자열을 조회
/*-----------------------------------------------------------------------------*/
/* 
    유용한 조건 표현식
    - IN: 이 중에 있는~
        ex> WHERE age IN (20, 30) >>> 나이가 20살 또는 30살 인 경우
    - != | <> : 같지 않음
    - _(언더바): 문자 하나를 의마
        ex> LIKE 'c_____@%' >>> c 라는 문자 뒤에 5글자가 오고 그 뒤에 @가 오는 구조를 조회
*/
/*-----------------------------------------------------------------------------*/
```
# 날짜와 시간 관련 함수들
```SQL
SELECT *
FROM coupang_main.member
WHERE YEAR(birthday) = '1992';   -- 1992년도에 태어ㄴ 회원들만 조회
/*-----------------------------------------------------------------------------*/
SELECT * 
FROM copang_main.member
WHERE MONTH(sign_up_day) IN (6, 7, 8); -- 여름에 가입한 회원들만 조회
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
WHERE DAYOFMONTH(sign_up_day) BETWEEM 15 AND 31; -- 각 달의 후반부에 가입했던 회원들만 조회
/*-----------------------------------------------------------------------------*/
/*
    DATEDIFF(날짜 a, 날짜 b): 날짜 a - 날짜 b
*/
SELECT email, sign_up_day, DATEDIFF(sign_up_day, '2019-01-01')
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
/*
    CURDATE(): 현재 날짜
*/
SELECT email, sign_up_day, CURDATE(), DATEDIFF(sign_up_day, CURDATE())
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
-- 회원들이 몇 살에 가입을 했는지를 조회
SELECT email, sign_up_day, DATEDIFF(sign_up_day, birthday) / 365
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
-- 가입일 기준 300일 이후의 날짜
SELECT email, sign_up_day, DATE_ADD(sign_up_day, INTERVAL 300 DAY)
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
-- 가입일 기준 250일 이전의 날짜
SELECT email, sign_up_day, DATE_SUB(sign_up_day, INTERVAL 250 DAY)
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
-- 1970 1월 1일부터 가입일까지 몇 초가 지났는지 확인
SELECT email, sign_up_day, UNIX_TIMESTAMP(sign_up_day)
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
-- UNIX_TIMESTAMP로 적힌 시간을 알아보기 편하게 변경
SELECT email, sign_up_day, FROM_UNIXTIME(UNIX_TIMESTAMP(sign_up_day))
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
```
# AND / OR 연산자
```SQL
SELECT *
FROM copang_main.member
WHERE gender = 'm' -- 성별이 남자
    AND address LIKE '서울%' -- 이면서 서울에 살면서
    AND age BETWEEM 25 and 29; -- 나이가 25세 이상 29세 이하인 회원들을 조회
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
WHERE MONTH(sign_up_day) BETWEEM 3 AND 5 -- 3월에서 5월 사이에 가입한
    OR MONTH(sign_up_day) BETWEEM 9 AND 11; -- 또는 가을에 가입한 회원들
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
WHERE (gender = 'm' AND height >= 180) -- 남자이면서 키가 180 이상인 경우
    OR (gender = 'f' AND height >= 170); -- 또는 여자이면서 키가 170이상인 회원들을 조회
/*-----------------------------------------------------------------------------*/
```
# 문자열 패턴 매칭 주의
```SQL
-- \(이스케이핑)
SELECT * 
FROM copang_main.member
WHERE sentence 
LIKE "%\'%";
/*-----------------------------------------------------------------------------*/
-- BINARY: 대소문자 구분
SELECT *
FROM copang_main.member
WHERE sentence
LIKE BINARY '%g%';
/*-----------------------------------------------------------------------------*/
```
# 정렬
```SQL
SELECT *
FROM copang_main.member
ORDER BY height ASC; -- height 컬럼을 기준으로 오름차순 정렬 (ASC: ascending의 줄임말, 생략 가능)
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
ORDER BY height DESC; -- height 컬럼을 기준으로 내림차순 정렬 (DESC: decending의 줄임말)
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
WHERE gender = 'm'      -- 남자 회원 중
    AND weight >= 70    -- 몸무게가 70이상인 회원들을
ORDER BY height ASC;    -- 키를 기준으로 오름차순 정렬
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
-- 가입년도 기준으로 내림차순 정렬 후
-- 같을 경우 다시 그 안에서는 이메일 기준으로 오름차순 정렬
ORDER BY YEAR(sign_up_day) DESC, email ASC;
/*-----------------------------------------------------------------------------*/
/*
    INT 타입은 숫자의 대소를 기준으로
    TEXT 타입은 앞에서부터 순서대로 문자의 순서를 비교해서 정렬
    TEXT타입인 숫자값들을 일시적으로 INT 등의 숫자형 타입을 기준을 정렬하려면
    CAST() 함수를 사용하면된다.
        param:
        - signed: 숫자형
        - decimal: 소숫점이 있는 수
*/
SELECT *
FROM FOR_TEST.ordering_test
ORDER BY CAST(data AS signed) ASC;
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
ORDER BY sign_up_day DESC
LIMIT 10; -- 현재 조회될 데이터중 10개만 추려서 확인
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
ORDER BY sign_up_day DESC
LIMIT 8, 2; -- 8번째 row부터 시작해서 2개의 row를 확인
/*-----------------------------------------------------------------------------*/
-- 2번째 row부터 10번째 row까지 짝수 row만 출력

-- 1. 각 행에 고유 번호를 부여하기 위해 WITH 절을 사용하여 서브쿼리를 생성합니다.
WITH ranked_members AS (
    SELECT *,
            -- sign_up_day를 기준으로 내림차순 정렬하고 각 행에 번호를 부여합니다.
           ROW_NUMBER() OVER (ORDER BY sign_up_day DESC) AS rn 
    FROM copang_main.member -- copang_main.member 테이블에서 데이터를 가져옵니다.
)
-- 2. WITH 절에서 생성한 서브쿼리의 결과를 사용하여 원하는 조건을 만족하는 행만 필터링합니다.
SELECT *
FROM ranked_members -- WITH 절에서 만든 ranked_members 테이블을 참조합니다.
WHERE rn BETWEEN 2 AND 10 -- 행 번호(rn)가 2 이상 10 이하인 데이터를 선택합니다.
  AND rn % 2 = 0; -- 선택된 행 중에서 행 번호(rn)가 짝수인 행만 필터링합니다.

/*
    	1.	ROW_NUMBER():
            •	각 행에 sign_up_day DESC 기준으로 고유한 번호를 부여합니다.
        2.	WITH ranked_members:
            •	ROW_NUMBER()로 부여된 번호를 가진 결과를 임시 테이블로 저장합니다.
        3.	WHERE rn BETWEEN 2 AND 10:
            •   행 번호가 2에서 10 사이인 데이터만 선택합니다.
        4.	AND rn % 2 = 0:
            •	짝수 행 번호만 선택합니다.
*/