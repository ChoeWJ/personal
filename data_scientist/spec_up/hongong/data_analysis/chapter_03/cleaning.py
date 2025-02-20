import pandas as pd
import os

os.chdir('chapter_03')

def data_cleaning(filename):
    """
    남산 도서관 장서 CSV 데이터 전처리 함수
    :param filename: CSV 파일 이름
    """
    # 파일을 데이터프레임으로 읽는다.
    ns_df = pd.read_csv(f'data/{filename}', low_memory=False)
    
    # NaN인 열을 삭제
    ns_book = ns_df.dropna(axis=1, how='all')
    
    # 대출 건수를 합치기 위해 필요한 행만 추출하여 count_df 데이터프레임 생성
    count_df = ns_book[['도서명', '저자', 'ISBN', '권', '대출건수']]
    
    # 도서명, 저자, ISBN, 권을 기준으로 대출건수를 groupby
    loan_count = count_df.groupby(by=['도서명', '저자', 'ISBN', '권'], dropna=False).sum()
    
    # 원본 데이터프레임에서 중복된 행을 제외하고, 고유한 행만 추출 후 복사
    dup_rows = ns_book.duplicated(subset=['도서명', '저자', 'ISBN', '권'])
    unique_rows = ~dup_rows
    ns_book3 = ns_book[unique_rows].copy()
    
    # 도서명, 저자, ISBN, 권을 인덱스로 설정
    ns_book3.set_index(['도서명', '저자', 'ISBN', '권'], inplace=True)
    
    # loan_count와 ns_book3의 인덱스를 정렬
    loan_count = loan_count.sort_index()
    ns_book3 = ns_book3.sort_index()

    # 정렬된 상태에서 업데이트
    ns_book3.update(loan_count)
    
    # 인덱스 재설정
    ns_book4 = ns_book3.reset_index()
    
    # 원본 데이터프레임의 열 순서로 변경
    ns_book4 = ns_book4[ns_book.columns]
    return ns_book4

ns_book4 = pd.read_csv("data/ns_book4.csv", low_memory=False)
new_ns_book4 = data_cleaning('ns_202104.csv')

print(ns_book4.equals(new_ns_book4))