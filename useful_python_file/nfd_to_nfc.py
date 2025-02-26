import os  # 파일 및 디렉토리 작업(파일 이름 변경 등)을 위해 os 모듈을 가져옵니다.
import glob  # 특정 패턴에 맞는 파일 리스트를 찾기 위해 glob 모듈을 가져옵니다.
import unicodedata  # 문자열의 유니코드 표준화를 수행하기 위해 unicodedata 모듈을 가져옵니다.

# glob.glob('*.csv')로 현재 디렉토리에서 모든 '.csv' 확장자를 가진 파일을 찾습니다.
for filename in glob.glob('*.csv'):  
    # filename을 NFC(Normalization Form C) 형태로 표준화하여 유니코드 문자열의 일관성을 보장합니다.
    nfc_filename = unicodedata.normalize('NFC', filename)  
    
    # 기존 파일 이름(filename)을 NFC 표준화된 이름(nfc_filename)으로 변경합니다.
    os.rename(filename, nfc_filename)