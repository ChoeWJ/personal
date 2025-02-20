import folium

m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

folium.Marker([37.5665, 126.9780], popup="서울", tooltip="클릭하세요!").add_to(m)

m.save("folium/03_marker.html")