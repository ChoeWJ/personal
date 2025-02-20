from fpdf import FPDF

# PDF 생성
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# 제목
pdf.set_font("Arial", size=16)
pdf.cell(200, 10, txt="Analysis Summary Report", ln=True, align="C")

# 내용 작성
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="""
This report summarizes the findings from the Titanic survival dataset analysis:

1. Survival Rate:
   - Female passengers had a higher survival rate (74%) compared to male passengers (18%).
2. Passenger Class:
   - 1st class passengers had a higher survival rate (63%) compared to 3rd class (24%).
3. Key Factors:
   - Gender, age, and ticket class were significant predictors of survival.
""")

# 저장
pdf.output("results/reports/summary_report.pdf")
print("PDF report saved.")