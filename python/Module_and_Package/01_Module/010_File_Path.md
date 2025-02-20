+ 이번 토픽에는 파일 경로를 이해해야 하는 영상들이 몇 개 있기 때문에 파일 경로를 노트로 설명해 드리겠습니다. 

+ `파일의 절대 경로`, `상대 경로`에 대해 아시는 분들은 이 노트를 건너 뛰셔도 됩니다.

# 컴퓨터 파일 시스템의 구조

+ 컴퓨터의 파일 시스템은 하나의 뿌리에서 시작해서 여러 개의 가지로 뻗어나가는, 나무 같은 구조를 가지고 있습니다.

![Module_and_Package_015](../../images/Module_and_Package/015.jpg)

+ root라는 폴더 안에 my, your 폴더들이 있고 my 폴더 안에는 folder라는 폴더와 file1.py라는 파일이 있고...

+ 파일 시스템의 뿌리는 항상 '루트(root)'라고 합니다. 

+ 결국 컴퓨터의 모든 파일은 루트 안에 있는 거죠. 

+ 그리고 프로그래밍에서는 폴더를 `디렉토리(directory)`라고도 합니다.

# 파일 경로

+ 파일 경로는 컴퓨터에 있는 파일의 정확한 위치를 뜻합니다. 

+ 파일의 경로를 표기하는 방법은 아래와 같습니다.

+ `Windows`

    + 디렉토리 안을 `\`로 표기합니다. 

    + 예를 들어 folder 디렉토리 안의 file2.py는 `folder\file2.py`로 표기합니다.

    + 루트 디렉토리 안은 하드 드라이브에 따라서 C:\ 혹은 D:\로 표기합니다. 
    
    + 하드 드라이브마다 각자의 파일 시스템이 있습니다.

+ `macOS`

    + 디렉토리 안을 `/`로 표기합니다. 
    
    + 예를 들어 folder 디렉토리 안의 file2.py는 `folder/file2.py`로 표기합니다.
    
    + 루트 디렉토리 안은 /로 표기합니다.

# 절대 경로

+ 파일의 절대 경로는 루트에서 시작하는 파일의 전체 경로입니다. 

+ 몇 가지 예를 봅시다.

![Module_and_Package_016](../../images/Module_and_Package/016.jpg)

+ `Windows`

    + file1.py의 경로: `C:\my\file1.py`

    + file2.py의 경로: `C:\my\folder\file2.py`

    + direcotry 디렉토리의 경로: `C:\your\directory`

+ `macOS`

    + file1.py의 경로: `/my/file1.py`
    + file2.py의 경로: `/my/folder/file2.py`
    + direcotry 디렉토리의 경로: `/your/directory`

# 상대 경로

+ 상대 경로는 현재 위치를 기준으로 다른 파일의 위치를 나타내는 걸 뜻합니다. 

+ 상대 경로는 항상 . (점) 아니면 .. (점점) 으로 시작합니다.

+ . (점) 은 현재 디렉토리를 뜻하고 

+ .. (점점) 은 상위 디렉토리 (현재 디렉토리를 포함하고 있는 디렉토리)를 뜻합니다. 

+ 몇 가지 예를 봅시다.

![Module_and_Package_017](../../images/Module_and_Package/017.jpg)

+ `Windows`

    + my 디렉토리에서 file2.py의 상대 경로: `.\folder\file2.py`
    + my 안의 folder 디렉토리에서 file2.py의 상대 경로: `.\file2.py`
    + file1.py에서 file2.py의 상대 경로: `.\folder\file2.py` (file2.py는 my 디렉토리에 위치해 있기 때문에 . 은 my 디렉토리를 뜻합니다)
    + file3.txt에서 file4.csv의 상대 경로: `.\file4.csv`
    + my 안의 folder 디렉토리에서 file1.py의 상대 경로: `..\file1.py`
    + file3.txt에서 your 디렉토리 안의 folder 디렉토리: `..\folder`

+ `Mac OS`

    + my 디렉토리에서 file2.py의 상대 경로: `./folder/file2.py`
    + my 안의 folder 디렉토리에서 file2.py의 상대 경로: `./file2.py`
    + file1.py에서 file2.py의 상대 경로: `./folder/file2.py` (file2.py는 my 디렉토리에 위치해 있기 때문에 . 은 my 디렉토리를 뜻합니다)
    + file3.txt에서 file4.csv의 상대 경로: `./file4.csv`
    + my 안의 folder 디렉토리에서 file1.py의 상대 경로: `../file1.py`
    + file3.txt에서 your 디렉토리 안의 folder 디렉토리: `../folder`