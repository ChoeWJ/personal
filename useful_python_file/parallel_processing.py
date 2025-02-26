from concurrent.futures import ThreadPoolExecutor
import pandas as pd

# 병렬 처리 함수

df = pd.read_csv("data/ns_book.csv", low_memory=False)
na_rows = df['도서명'].isna() | df['저자'].isna() | df['출판사'].isna() | df['발행년도'].eq(-1)

def parallel_apply(df, func, max_workers=5):
    """
    DataFrame에 병렬 처리를 적용하는 함수
    """
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(func, [row for _, row in df.iterrows()]))
    return pd.DataFrame(results)

# 실행
update_df = parallel_apply(df[na_rows], function, max_workers=5)
update_df.head(2)