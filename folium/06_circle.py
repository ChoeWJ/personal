import folium

m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

folium.Circle(
    location=[37.5665, 126.9780],
    radius=5000,
    color='green',
    fill=True,
    fill_color='green'
).add_to(m)

m.save("folium/map_data/06_circle.html")