+ 파이썬은 임포트 하려는 모듈을 찾기 위해서 특정 경로들을 살핀다

+ 이 경로들은 sys라는 스탠다드 모듈을 통해 확인해 볼 수 있다.

```python
import sys

print(sys.path)

"""
['c:\\Users\\qhdks\\Desktop\\The Future\\Personal\\Python\\Practice', 'C:\\Users\\qhdks\\anaconda3\\python312.zip', 'C:\\Users\\qhdks\\anaconda3\\DLLs', 'C:\\Users\\qhdks\\anaconda3\\Lib', 'C:\\Users\\qhdks\\anaconda3', 'C:\\Users\\qhdks\\AppData\\Roaming\\Python\\Python312\\site-packages', 'C:\\Users\\qhdks\\AppData\\Roaming\\Python\\Python312\\site-packages\\win32', 'C:\\Users\\qhdks\\AppData\\Roaming\\Python\\Python312\\site-packages\\win32\\lib', 'C:\\Users\\qhdks\\AppData\\Roaming\\Python\\Python312\\site-packages\\Pythonwin', 'C:\\Users\\qhdks\\anaconda3\\Lib\\site-packages', 'C:\\Users\\qhdks\\anaconda3\\Lib\\site-packages\\win32', 'C:\\Users\\qhdks\\anaconda3\\Lib\\site-packages\\win32\\lib', 'C:\\Users\\qhdks\\anaconda3\\Lib\\site-packages\\Pythonwin', 'c:\\Users\\qhdks\\.vscode\\extensions\\almenon.arepl-3.0.0\\node_modules\\arepl-backend\\python']
"""
```