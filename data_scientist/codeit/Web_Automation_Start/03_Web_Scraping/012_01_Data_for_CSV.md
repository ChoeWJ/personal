# CSV란?

+ CSV는 **Comma Separated Values**의 약자입니다. 

+ '값이 쉼표(,)로 구분되어 있다' 이런 뜻인데요. CSV는 표 데이터를 저장하는 데 많이 쓰이는 파일 형식입니다.

+ 엑셀(.xlsx)은 Microsoft Excel 전용 파일 형식이라면 

+ CSV(.csv)는 일반적으로 표 데이터를 저장하는 파일 형식입니다. 

+ CSV 파일은 메모장(Windows), Numbers(Mac), Microsoft Excel 등 여러 소프트웨어에서 잘 열립니다.

# CSV 형식

+ 사람 이름, 키, 몸무게가 들어가 있는 예시 csv 파일입니다. 파일을 열어 보면 아래와 같은 내용이 있는데요.

![Web_Automation_Start_002](../../images/Web_Automation_Start/002.png)

+ 각 데이터가 쉼표로 구분돼 있고, 행은 줄 단위로 구분돼 있습니다. 아주 직관적이죠? 이게 바로 CSV 형식입니다.

+ CSV 파일을 Microsoft Excel, Numbers, 또는 pandas(파이썬 데이터 분석 라이브러리) 같은 데이터 분석 툴로 열면 표로 인식이 됩니다. 

+ 아래는 data.csv 파일을 Numbers로 연 모습입니다.

![Web_Automation_Start_003](../../images/Web_Automation_Start/003.png)

# 파이썬으로 CSV 파일 작성하기

### CSV 모듈 임포트

+ csv라는 모듈을 사용하면 쉽게 만들 수 있습니다. 스탠다드 모듈이기 때문에 따로 설치를 안 해 주셔도 됩니다.

```python
import csv
```

### CSV 파일 생성

+ 먼저 CSV 파일을 만들어 주고, 파일에 데이터를 CSV 형식으로 전달해 주는 csv.writer라는 도구를 활용할 겁니다.

```python
# CSV 파일 생성
csv_file = open('file_name.csv', 'w')
csv_writer = csv.writer(csv_file)
```

+ open() 안에 파일 이름과 모드(mode)를 써 줍니다. 우리는 데이터를 파일에 써 줄 거니까 'w' (write)를 써 줍니다.

+ 그리고 csv.writer()안에 방금 만들어준 csv_file을 넣어 줍니다.

### 행 추가

+ CSV 파일에 행을 추가하기 위해서는 우리가 만든 csv_writer를 사용합니다.

```python
# CSV 파일에 행 추가
csv_writer.writerow([data1, data2, ...])
```

+ .writerow() 메소드를 활용하면 됩니다. 엑셀 파일에 행을 추가할 때 썼었던 ws.append()와 아주 비슷하죠? 행에 들어갈 데이터를 리스트 형식으로 넘겨 줍니다.

+ 헤더 행, 데이터 행 상관없이 csv_writer.writerow()를 사용하시면 됩니다.

### CSV 파일 닫기

+ 파이썬에서 파일을 열었으면, 사용이 끝난 후 닫아 주는 것이 좋은 습관입니다.

```python
# CSV 파일 닫기
csv_file.close()
```

+ 사실 프로그램이 종료되면 파일이 자동으로 닫히기 때문에 지금 같이 단순한 프로그램을 짤 때는 큰 상관이 없는데요. 

+ 복잡한 프로그램에서 파일을 닫아 주지 않으면, 프로그램이 실행되는 동안 그 파일을 다른 곳에서 사용할 수 없게 됩니다. (csv_writer 가 아닌 csv_file을 닫아 주셔야 합니다.)

# 티비랭킹닷컴 데이터를 CSV 파일로

+ 이전 영상에서는 티비랭킹닷컴의 데이터를 엑셀 파일로 저장해 봤는데, 이번에는 똑같은 데이터를 CSV 파일로 저장하는 코드를 보여 드릴게요.


### 엑셀 파일:

```python

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 워크북 생성
wb = Workbook(write_only=True)
ws = wb.create_sheet('Data')

# 헤더 행 추가
ws.append(['순위', '채널', '프로그램', '시청률'])

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

for tr_tag in soup.select('tr')[1:]:
    td_tags = tr_tag.select('td')
    row = [
        td_tags[0].get_text(),
        td_tags[1].get_text(),
        td_tags[2].get_text(),
        td_tags[3].get_text()
    ]
    # 데이터 행 추가
    ws.append(row)

# 워크북 저장
wb.save('시청률_2010년1월1주차.xlsx')
```

### CSV 파일:

```python
import csv
import requests
from bs4 import BeautifulSoup

# CSV 파일 생성
csv_file = open('시청률_2010년1월1주차.csv', 'w')
csv_writer = csv.writer(csv_file)

# 헤더 행 추가
csv_writer.writerow(['순위', '채널', '프로그램', '시청률'])

response = requests.get("https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

for tr_tag in soup.select('tr')[1:]:
    td_tags = tr_tag.select('td')
    row = [
        td_tags[0].get_text(),
        td_tags[1].get_text(),
        td_tags[2].get_text(),
        td_tags[3].get_text()
    ]
    # 데이터 행 추가
    csv_writer.writerow(row)

# CSV 파일 닫기
csv_file.close()
```
