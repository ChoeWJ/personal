# EDA 요약 저장
eda_summary = """
Exploratory Data Analysis (EDA) Summary:

1. Total Passengers: 891
2. Missing Values:
   - Age: 177
   - Cabin: 687
3. Gender Distribution:
   - Male: 577
   - Female: 314
4. Survival Rate:
   - Survived: 38.3%
   - Did Not Survive: 61.7%
"""

# 파일 저장
with open("results/reports/EDA_summary.txt", "w") as file:
    file.write(eda_summary)
print("EDA summary saved.")