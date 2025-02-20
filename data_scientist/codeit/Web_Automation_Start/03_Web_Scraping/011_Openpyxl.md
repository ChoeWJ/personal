# 라이브러리 임포트

```python
from openpyxl import Workbook
```

# 워크북 생성

```python
wb = Workbook()
wb = Workbook(write_only=True)
```

+ 워크북을 만들기 위해선 Workbook()을 쓰면 되는데요. 

+ 파일에서 데이터를 읽어 오지 않고, **데이터를 저장하기만 하는 경우 write only 모드를 써 주는 것이 퍼포먼스에 도움**이 됩니다. 

+ write only 모드는 write_only=True로 설정해 줄 수 있습니다.

# 워크시트 생성

```python
ws = wb.create_sheet()
ws = wb.create_sheet('워크시트_이름')
```
 
+ 워크시트는 데이터가 저장돼 있는 시트(sheet) 하나를 뜻합니다. 

+ 워크북에는 여러 워크시트가 있을 수 있습니다. 워크시트를 만들려면 wb.create_sheet() 메소드를 사용합니다. 

+ 파라미터로 워크시트 이름을 넣어 줄 수 있고, 안 넣어 주면 디폴트 이름 'Sheet1'(혹은 순서에 따라 'SheetN')이 사용됩니다.

# 행 추가

```python
ws.append([data1, data2, data3])
```

+ 워크시트에 행을 추가하려면 행 요소를 리스트로 만들어서 ws.append()에 넣어 줍니다.

# 워크북 저장

```python
wb.save('워크북_이름.xlsx')
```

+ 워크북에 모든 데이터를 써 줬으면, 워크북을 저장해 줘야 합니다. 

+ wb.save() 메소드를 쓰고, 파일 이름을 파라미터로 넣어 줍니다. 파일 이름에 .xlsx 확장자도 잊지 마세요!