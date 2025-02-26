import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm


# Seaborn 스타일 설정
sns.set_theme(
    style='whitegrid',
    rc={
        'axes.unicode_minus': False,  # 마이너스 기호 깨짐 방지
        'figure.figsize': (12, 6),    # 그래프 크기 설정
        'axes.labelsize': 14,         # 축 레이블 크기
        'xtick.labelsize': 12,        # x축 눈금 크기
        'ytick.labelsize': 12,        # y축 눈금 크기
        'legend.fontsize': 12,        # 범례 폰트 크기
        'axes.titleweight': 'bold',   # 제목 굵게
        'axes.titlesize': 16          # 제목 크기
    }
)


class SamplingAnalysis:
    def __init__(self, data: pd.DataFrame, columns: list[str]):
        """
        데이터와 분석할 여러 컬럼을 입력받아 초기화
        :param data: 분석할 데이터 (DataFrame)
        :param columns: 분석할 대상 컬럼 리스트 (list)
        """
        self.data = data
        self.columns = columns
        self.true_means = {col: data[col].mean() for col in columns}  # 각 컬럼의 전체 평균 저장
        self.samples = {}
        self.sample_means = {}
        self.sample_stds = {}
        self.sample_sizes = {}
        self.confidence_intervals = {}
        self.errors = {}

    def sample_data(self, frac: float = 0.1, random_state: int = 42):
        """
        여러 컬럼에서 샘플링 수행
        :param frac: 샘플링 비율 (기본값: 10%)
        :param random_state: 랜덤 시드 값 (기본값: 42)
        """
        self.samples = self.data.sample(frac=frac, random_state=random_state)
        
        for col in self.columns:
            self.sample_means[col] = self.samples[col].mean()
            self.sample_stds[col] = self.samples[col].std()
            self.sample_sizes[col] = len(self.samples)
            self.errors[col] = abs(self.sample_means[col] - self.true_means[col]) / self.true_means[col] * 100
            
            print(f"[{col}] 전체 평균: {self.true_means[col]:.2f}, 샘플 평균: {self.sample_means[col]:.2f}, 오차율: {self.errors[col]:.4f}%")

    def compute_confidence_intervals(self, confidence: float = 0.95):
        """
        각 컬럼의 신뢰구간 계산
        :param confidence: 신뢰수준 (0.95 = 95% 신뢰구간)
        """
        if self.samples is None or self.samples.empty:
            raise ValueError("샘플을 먼저 생성하세요. sample_data()를 실행하세요.")

        z_score = norm.ppf(1 - (1 - confidence) / 2)  # Z 값 계산
        
        for col in self.columns:
            margin_of_error = z_score * (self.sample_stds[col] / np.sqrt(self.sample_sizes[col]))
            self.confidence_intervals[col] = (self.sample_means[col] - margin_of_error, self.sample_means[col] + margin_of_error)
            
            print(f"[{col}] {int(confidence * 100)}% 신뢰 구간: {self.confidence_intervals[col]}")

    def plot_error_vs_sample_size(self, sample_sizes=[0.01, 0.05, 0.1, 0.2, 0.5]):
        """
        여러 컬럼에 대해 샘플 크기에 따른 평균 오차율 변화를 시각화
        :param sample_sizes: 샘플 비율 리스트 (기본값: [1%, 5%, 10%, 20%, 50%])
        """
        plt.figure(figsize=(12, 6))

        for col in self.columns:
            errors = []
            for frac in sample_sizes:
                sample = self.data.sample(frac=frac, random_state=42)
                sample_mean = sample[col].mean()
                error = abs(sample_mean - self.true_means[col]) / self.true_means[col] * 100
                errors.append(error)

            plt.plot(sample_sizes, errors, marker="o", label=col)

        plt.xlabel("샘플 비율")
        plt.ylabel("평균 오차율 (%)")
        plt.title("샘플 크기에 따른 평균 오차율 변화")
        plt.legend()
        plt.show()

    def recommend_optimal_frac(self, sample_sizes=[0.01, 0.05, 0.1, 0.2, 0.5], error_threshold=1.0):
        """
        최적의 샘플 비율을 추천 (오차율이 error_threshold 이하인 가장 작은 frac 선택)
        :param sample_sizes: 테스트할 샘플 비율 리스트
        :param error_threshold: 허용 가능한 최대 오차율 (기본값 1%)
        """
        optimal_fracs = {}

        for col in self.columns:
            for frac in sample_sizes:
                sample = self.data.sample(frac=frac, random_state=42)
                sample_mean = sample[col].mean()
                error = abs(sample_mean - self.true_means[col]) / self.true_means[col] * 100
                
                if error <= error_threshold:  # 오차율이 기준 이하인 경우
                    optimal_fracs[col] = frac
                    break  # 가장 작은 적정 frac 값을 찾으면 종료
            
            if col not in optimal_fracs:  # 만약 모든 frac에서도 기준 이하가 안되면 가장 큰 값 사용
                optimal_fracs[col] = max(sample_sizes)

        for col, opt_frac in optimal_fracs.items():
            print(f"📌 최적의 샘플 비율 추천 ({col}): {opt_frac:.2f} (오차율 ≤ {error_threshold}%)")

        return optimal_fracs


# 데이터 로드
df = pd.read_csv('health_info.csv', encoding='euc-kr')

# 샘플링 분석 클래스 생성 (여러 개의 컬럼 지정 가능!)
analyzer = SamplingAnalysis(df, columns=["신장(5cm단위)", "체중(5kg단위)", "허리둘레", "수축기혈압"])

# 최적의 샘플 크기 추천 (오차율 1% 이하)
optimal_fracs = analyzer.recommend_optimal_frac(error_threshold=1.0)