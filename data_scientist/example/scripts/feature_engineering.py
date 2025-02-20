# feature_engineering.py
import pandas as pd


def create_family_size(df):
    """Create a new feature 'FamilySize' based on SibSp and Parch."""
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    return df

def categorize_fare(df):
    """Categorize 'Fare' into bins."""
    df['FareCategory'] = pd.cut(df['Fare'], bins=[0, 7.91, 14.454, 31, float('inf')], labels=[0, 1, 2, 3])
    return df