import folium

m = folium.Map(location=[37.5665, 126.9780], 
               zoom_start=7,
               zoom_control=False,       # 확대/축소 버튼 제거
               scrollWheelZoom=False,    # 마우스 휠 확대/축소 비활성화
               dragging=False            # 지도 드래그 이동 비활성화
)

locations = [
    [37.5665, 126.9780, "서울"],
    [35.1796, 129.0756, "부산"],
    [37.4563, 126.7052, "인천"]
]

for lat, lon, name in locations:
    folium.Marker([lat, lon], popup=name).add_to(m)
    
m.save('folium/map_data/05_poly_circlemarker.html')