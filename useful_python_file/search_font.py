import matplotlib.font_manager as fm

# 모든 폰트 확인
font_list = [f.name for f in fm.fontManager.ttflist]
print(font_list)

# 특정 폰트 확인 (설치되어 있어야 함)
for f in fm.findSystemFonts():
    font = fm.FontProperties(fname=f)
    if 'Nanum' in font.get_name():  # 'Nanum' 폰트만 출력
        print(font.get_name(), f)