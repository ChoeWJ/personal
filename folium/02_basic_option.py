import folium

# OpenStreetMap (default)

# CartoDB dark_matter
m1 = folium.Map(location=[37.5665, 126.9780], zoom_start=12, tiles='CartoDB dark_matter')
m1.save("folium/02_dark_matter.html")

# CartoDB positron
m2 = folium.Map(location=[37.5665, 126.9780], zoom_start=12, tiles='CartoDB positron')
m2.save("folium/02_positron.html")

