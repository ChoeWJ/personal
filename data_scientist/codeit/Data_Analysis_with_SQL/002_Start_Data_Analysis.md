# 데이터 특성
```SQL
SELECT COUNT(email) -- email 컬럼의 값을 가진 row의 갯수, Null의 갯수는 제외
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
SELECT COUNT(*) -- member 테이블의 전체 row값
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
SELECT MAX(height)  -- height 컬럼 중 가장 큰 값
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
SELECT MIN(weight) -- weight 컬럼 중 가장 작은 값
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
SELECT AVG(weight) -- weight 컬럼의 평균 값, Null 값 제외
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
/*
    사용 가능 함수 정리

    SUM(): 합계
    STD(): 표준편차
    ABS(): 절대값
    SQRT(): 제곱근
    CEIL(): 올림
    FLOOR(): 내림
    ROUND(): 반올림
*/
```
# NULL 값 다루기
```SQL
SELECT *
FROM copang_main.member
WHERE address IS NULL; -- address 컬럼에 NULL값이 있는 row들을 조회
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
WHERE address IS NOT NULL; -- address 컬럼에 실제로 값이 들어있는 경우만 출력
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
WHERE height IS NULL
    OR weight IS NULL
    OR address IS NULL; -- 셋 중 하나의 컬럼이라도 NULL 이 들어있다면 출력 제외
/*-----------------------------------------------------------------------------*/
SELECT 
    COALESCE(height, '####'), -- NULL 값에 #### 출력
    COALESCE(weight, '---'), -- NULL 값에 --- 출력
    COALESCE(address, '@@@') -- NULL 값에 @@@ 출력
FROM copang_main.member;
```
# 이상치 처리
```SQL
SELECT AVG(age) -- age 컬럼의 평균 값
FROM copang_main.member
WHERE age BETWEEN 5 AND 100; -- age 컬럼이 5 이상 100 이하인 값들 중
/*-----------------------------------------------------------------------------*/
SELECT *
FROM copang_main.member
WHERE address 
NOT LIKE '%호';
/*-----------------------------------------------------------------------------*/
```
# 컬럼 다루기
```SQL
SELECT 
    email, 
    height, 
    weight, 
    weight / ((height/100) * (height/100))
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
SELECT 
    email, 
    height AS 키, 
    weight AS 몸무게, 
    ROUND(weight / ((height/100) * (height/100)), 2) AS BMI -- 컬럼 alias (AS)
FROM copang_main.member
/*-----------------------------------------------------------------------------*/
/*
    AS없이 띄어쓰기만으로도 사용이 가능하지만
    가급적 가독성을 위해 붙여주는 것이 좋다.
*/ 
SELECT 
    email, 
    height 키, 
    weight 몸무게, 
    ROUND(weight / ((height/100) * (height/100)), 2) BMI
FROM copang_main.member
/*-----------------------------------------------------------------------------*/
SELECT 
    email,
    -- CONCAT(): concatenate의 약자로 여러 컬럼들을 하나로 합쳐서 보여줄때 사용
    CONCAT(height, 'cm', ', ', weight, 'kg') AS '키와 몸무게',
    ROUND(weight / ((height/100) * (height/100)), 2) AS BMI
FROM copang_main.member
/*-----------------------------------------------------------------------------*/
SELECT 
    email,
    CONCAT(height, 'cm', ', ', weight, 'kg') AS '키와 몸무게',
    ROUND(weight / ((height/100) * (height/100)), 2) AS BMI,

(CASE
    WHEN weight IS NULL OR height IS NULL 
        THEN '비만 여부 알 수 없음'
    WHEN ROUND(weight / ((height/100) * (height/100)), 2) >= 25 
        THEN '과체중 또는 비만'
    WHEN ROUND(weight / ((height/100) * (height/100)), 2) >= 18.5 
        AND ROUND(weight / ((height/100) * (height/100)), 2) < 25
        THEN '정상'
    ELSE '저체중'
END) AS obesity_check
FROM copang_main.member
ORDER BY obesity_check ASC;
/*-----------------------------------------------------------------------------*/
SELECT 
    DISTINCT(gender) -- gender 컬럼의 고유값 확인
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
SELECT 
    DISTINCT(SUBSTRING(address, 1, 2))
    /*
        SUBSTRING(): 문자열의 일부를 추출하는 함수
            param:
            - column
            - 시작 위치
            - 추출할 문자열 갯수
    */
FROM copang_main.member;
/*-----------------------------------------------------------------------------*/
/*
    다양한 문자열 관련 함수들
    - LENGTH(): 문자열의 길이
    - UPPER(): 문자열을 모두 대문자로 치환
    - LOWER(): 문자열을 모두 소문자로 치환
    - LPAD() | RPAD(): 문자열의 왼쪽 또는 오른쪽을 특정 문자열로 채우는 함수
        ex> LPAD(age, 10, '0'): age 컬럼의 값의 왼쪽에 문자 0을 붙여서 총 10자리로 만든다
    - TRIM(): 왼쪽과 오른쪽의 모든 공백 삭제
    - LTRIM() | RTRIM(): 왼쪽 또는 오른쪽의 모든 공백 삭제
*/
```
# 그루핑
```SQL
SELECT gender
FROM copang_main.member
GROUP BY gender;    -- gender 컬럼을 기준으로 그루핑
/*-----------------------------------------------------------------------------*/
SELECT 
    gender, 
    COUNT(*)
FROM copang_main.member
GROUP BY gender;
/*-----------------------------------------------------------------------------*/
SELECT 
    gender, 
    COUNT(*), -- gender 컬럼의 각 그루핑된 그룹들의 합
    AVG(height) -- 각 그룹들의 키의 평균
FROM copang_main.member
GROUP BY gender;
/*-----------------------------------------------------------------------------*/
SELECT 
	gender, 
    COUNT(*), 
    AVG(height),
    MIN(weight) -- 각 그룹들의 몸무게 중 최솟값
FROM copang_main.member
GROUP BY gender;
/*-----------------------------------------------------------------------------*/
SELECT 
	SUBSTRING(address, 1, 2) AS region,
    COUNT(*)
FROM copang_main.member
GROUP BY SUBSTRING(address, 1, 2); -- address 컬럼에서 특정 부분 추출 후 그루핑
/*-----------------------------------------------------------------------------*/
SELECT 
	SUBSTRING(address, 1, 2) AS region,
    gender,
    COUNT(*)
FROM copang_main.member
GROUP BY 
	SUBSTRING(address, 1, 2),
    gender  -- gender 컬럼을 그룹으로 추가
/*-----------------------------------------------------------------------------*/
SELECT 
	SUBSTRING(address, 1, 2) AS region,
    gender,
    COUNT(*)
FROM copang_main.member
GROUP BY 
	SUBSTRING(address, 1, 2),
    gender
HAVING region = '서울'; -- region 그룹이 서울인 값들만 조회
/*-----------------------------------------------------------------------------*/
SELECT 
	SUBSTRING(address, 1, 2) AS region,
    gender,
    COUNT(*)
FROM copang_main.member
GROUP BY 
	SUBSTRING(address, 1, 2),
    gender
HAVING 
	region = '서울'
    AND gender = 'm';   -- region 그룹의 gender가 m인 그룹들만 조회
/*-----------------------------------------------------------------------------*/
SELECT 
	SUBSTRING(address, 1, 2) AS region,
    gender,
    COUNT(*)
FROM copang_main.member
GROUP BY 
	SUBSTRING(address, 1, 2),
    gender
HAVING region IS NOT NULL;  -- region 그룹에서 NULL값을 제외하고 조회
/*-----------------------------------------------------------------------------*/
/*
    1. GROUP BY 절 뒤에 쓴 컬럼 이름들만, SELECT 절 뒤에도 쓸 수 있다.
    2. 대신 SELECT 절 뒤에서 집계 함수에 그 외의 컬럼 이름을 인자로 넣는 것은 허용된다.
*/
/*-----------------------------------------------------------------------------*/
SELECT 
	SUBSTRING(address, 1, 2) AS region,
    gender,
    COUNT(*)
FROM copang_main.member
GROUP BY 
	SUBSTRING(address, 1, 2),
    gender
WITH ROLLUP -- 그루핑한 COUNT(*) 값의 총 합계 계산
HAVING region IS NOT NULL
ORDER BY region ASC, gender DESC;
```
| 작성 순서 |  | 실행 순서 |
| --- | --- | --- |
| SELECT| `1` |FROM |
| FROM| `2` |WHERE |
| WHERE| `3` |GROUP BY |
| GROUP BY| `4` |HAVING |
| HAVING | `5` |SELECT |
| ORDER BY| `6` |ORDER BY |
| LIMIT| `7` |LIMIT |
```SQL
SELECT
    YEAR(sign_up_day) AS s_year,
    gender, 
    SUBSTRING(address, 1, 2) AS region,
	GROUPING(YEAR(sign_up_day)), GROUPING(gender), GROUPING(SUBSTRING(address, 1, 2)),
    COUNT(*)
FROM copang_main.member
GROUP BY
	YEAR(sign_up_day),
    gender,
    SUBSTRING(address, 1, 2)
WITH ROLLUP
ORDER BY s_year DESC;
```