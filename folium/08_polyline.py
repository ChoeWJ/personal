import folium

m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

folium.PolyLine(
    locations=[
        [37.5665, 126.9780],  # 서울
        [35.1796, 129.0756],  # 부산
        [37.4563, 126.7052]   # 인천
    ],
    color='red',
    weight=5
).add_to(m)

m.save("folium/map_data/08_polyline.html")