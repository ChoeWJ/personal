# data_preprocessing.py

import pandas as pd

def load_data(file_path):
    """Load a dataset from the given file path."""
    return pd.read_csv(file_path)

def preprocess_data(df):
    """Clean and preprocess the dataset."""
    # 결측값 처리
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

    # 범주형 변수 인코딩
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df['Embarked'] = df['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})

    return df