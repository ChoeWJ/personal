import folium

from folium.plugins import MarkerCluster

m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

marker_cluster = MarkerCluster().add_to(m)

locations = [
    [37.5665, 126.9780, "서울"],
    [35.1796, 129.0756, "부산"],
    [37.4563, 126.7052, "인천"],
    [35.8714, 128.6014, "대구"],
    [36.3504, 127.3845, "대전"]
]

for lat, lon, name in locations:
    folium.Marker([lat, lon], popup=name).add_to(m)

m.save("folium/map_data/10_cluster.html")