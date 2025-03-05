import yfinance as yf
import mysql.connector
import schedule
import time
import sys

# 📌 MySQL 연결 설정 (자동 커밋 활성화)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="stocks",
    autocommit=True,  # ✅ 자동 커밋 추가
)
cursor = conn.cursor()

# 📌 테이블 생성 (한 번만 실행하면 됨)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS stock_prices (
        id INT AUTO_INCREMENT PRIMARY KEY,
        symbol VARCHAR(10),
        price DECIMAL(10,2),
        volume BIGINT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
"""
)
conn.commit()


# 📌 주가 데이터 가져오기 & MySQL 저장
def fetch_and_store_stock():
    stock_symbol = "AAPL"
    stock = yf.Ticker(stock_symbol)

    # ✅ `interval="1m"`로 설정하여 더 많은 데이터 가져오기
    data = stock.history(interval="1m", period="1d")

    print("📌 yfinance 데이터 개수:", len(data))  # ✅ 개수 확인

    if not data.empty:
        try:
            for index, row in data.iterrows():  # ✅ 모든 행을 반복하며 저장
                price = float(row["Close"])
                volume = int(row["Volume"])
                timestamp = index.strftime("%Y-%m-%d %H:%M:%S")  # ✅ 인덱스(시간) 저장

                print(f"📊 저장 중: 시간: {timestamp}, 가격: {price}, 거래량: {volume}")

                cursor.execute(
                    """
                    INSERT INTO stock_prices (symbol, price, volume, timestamp)
                    VALUES (%s, %s, %s, %s)
                    """,
                    (stock_symbol, price, volume, timestamp),
                )
            print(f"✅ {len(data)}개의 데이터가 MySQL에 저장됨!")

        except mysql.connector.Error as err:
            print(f"⚠️ MySQL 오류 발생: {err}")

    else:
        print("⚠️ 데이터가 없습니다. yfinance API 확인 필요!")


# 📌 1분마다 자동 실행 (schedule 라이브러리 활용)
schedule.every(1).minutes.do(fetch_and_store_stock)

# 📌 타이머 & 자동 종료 기능 추가
start_time = time.time()  # 시작 시간 기록
duration = 10  # 실행 시간 (초)

while True:
    schedule.run_pending()

    elapsed_time = int(time.time() - start_time)  # 경과 시간 (초)
    remaining_time = duration - elapsed_time  # 남은 시간 (초)

    # 📌 터미널에 실시간 타이머 표시
    sys.stdout.write(f"\r⏳ 자동 업데이트 진행 중... 남은 시간: {remaining_time}초  ")
    sys.stdout.flush()

    time.sleep(1)  # 1초마다 실행

    # 📌 60초 후 자동 종료
    if elapsed_time >= duration:
        print("\n⏹ 자동 업데이트 종료!")

        # ✅ Python에서 MySQL 데이터 확인
        cursor.execute(
            "SELECT * FROM stock_prices ORDER BY timestamp DESC LIMIT 5"
        )
        rows = cursor.fetchall()
        print("📌 MySQL 데이터 확인:", rows)

        break

fetch_and_store_stock()
