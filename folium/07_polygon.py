import folium

m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

folium.Polygon(
    locations=[
        [37.5665, 126.9780],
        [37.5700, 126.9800],
        [37.5680, 126.9900]
    ],
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(m)

m.save("folium/map_data/07_polygon.html")