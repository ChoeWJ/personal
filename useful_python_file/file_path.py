import os


# 파일 경로 확인
file_path = "/Users/woojinchoe/Downloads/member_data.csv"
if os.path.exists(file_path):
    print("File exists:", file_path)
else:
    print("File not found:", file_path)

#########################################################################################################
# # 파일 인코딩 컨버터
# def file_encoding_conversion(input_path, output_path):
#     if not os.path.exists(input_path):  # 파일 존재 여부 먼저 확인
#         print(f"File not found: {input_path}")
#         return

#     try:
#         # 파일 읽기 시도
#         with open(input_path, "r", encoding="utf-8") as f_in:
#             data = f_in.read()

#         # 파일 쓰기 시도
#         with open(output_path, "w", encoding="euc-kr") as f_out:
#             f_out.write(data)

#         print("File conversion completed successfully.")
    
#     except UnicodeDecodeError as ude:
#         print(f"Encoding issue: {ude}. The file might not be 'euc-kr'. Try 'utf-8' instead.")
    
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

#########################################################################################################
# # 현재 작업 디렉토리 확인
# print("Current working directory:", os.getcwd())  
