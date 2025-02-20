import folium

m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

folium.CircleMarker(
    location=[37.5665, 126.9780],
    radius=40,  # 원의 크기 조절
    color='blue',  # 테두리 색
    fill=True,
    fill_color='red', # 원 내부 색상
    fill_opacity=0.5  # 투명도
).add_to(m)

m.save("folium/map_data/04_circlemarker.html")