import numpy as np
import pandas as pd
import operator

from collections import Counter
from functools import reduce

def random_number():
    count = 0
    new_number = []

    while count < 6:
        num = np.random.randint(1, 45)
        if num not in new_number:
            new_number.append(num)
            count += 1
    new_number.sort()
    return new_number

def lotto():
    # 과거 로또 당첨 번호 데이터 로드
    df = pd.read_csv('lotto_data.csv')

    # 모든 당첨 번호를 하나의 리스트로 결합
    all_numbers = df[['번호1', '번호2', '번호3', '번호4', '번호5', '번호6']].values.flatten()

    # 각 번호의 출현 빈도 계산
    number_counts = Counter(all_numbers)

    # 총 추첨 횟수
    total_draws = len(df)

    # 각 번호의 출현 확률 계산
    number_probabilities = {num: count / total_draws for num, count in number_counts.items()}


    # 사용자가 생성한 번호


    user_numbers = random_number()

    # 사용자가 생성한 번호의 출현 확률 계산
    user_probabilities = [number_probabilities.get(num, 0) for num in user_numbers]

    # 사용자가 생성한 번호가 모두 당첨될 확률 (독립 사건으로 가정하고 확률을 곱함)
    user_win_probability = reduce(operator.mul, user_probabilities, 1)

    print(f"사용자가 생성한 번호 {user_numbers}가 다음 회차에서 모두 당첨될 확률: {user_win_probability:.12%}")

today_number = lotto()