import os
import chardet


def detect_encoding(file_path, buffer_size=100000):  # 100KB까지 샘플 크기 증가
    """파일의 인코딩을 자동 감지 (샘플 크기 증가)"""
    with open(file_path, "rb") as f:
        raw_data = f.read(buffer_size)  # 더 많은 데이터를 읽음
    result = chardet.detect(raw_data)
    return result["encoding"]


def convert_encoding_to_euckr(
    folder_path, target_encoding="euc-kr", file_extensions=[".txt", ".csv"]
):
    """폴더 내 모든 파일의 인코딩을 EUC-KR로 변환"""

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # 특정 확장자만 변환
            if not any(file.lower().endswith(ext) for ext in file_extensions):
                continue

            try:
                # 원본 인코딩 감지
                original_encoding = detect_encoding(file_path)

                # 감지 실패 시 기본값 적용
                if not original_encoding:
                    print(f"⚠ 인코딩 감지 실패: {file_path}, 기본값 'utf-8' 사용")
                    original_encoding = (
                        "utf-8"  # 기본 인코딩 지정 가능 (ISO-8859-1 등으로 변경 가능)
                    )

                # 동일한 인코딩이면 건너뜀
                if original_encoding.lower() == target_encoding.lower():
                    print(f"✅ 이미 {target_encoding} 인코딩: {file_path}")
                    continue

                # 파일 읽기 (errors='replace' 추가)
                with open(
                    file_path, "r", encoding=original_encoding, errors="replace"
                ) as f:
                    content = f.read()

                # 파일 저장 (EUC-KR 변환)
                with open(
                    file_path, "w", encoding=target_encoding, errors="replace"
                ) as f:
                    f.write(content)

                print(
                    f"🔄 {original_encoding} → {target_encoding} 변환 완료: {file_path}"
                )

            except Exception as e:
                print(f"❌ 변환 실패 ({file_path}): {e}")


# 사용 예시
folder_path = "./temp_data"  # 변환할 폴더 경로 설정
convert_encoding_to_euckr(folder_path, target_encoding="euc-kr")
