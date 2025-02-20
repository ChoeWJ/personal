import folium
import random

from folium.plugins import HeatMap

m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

heat_data = [[random.uniform(37.4, 37.6), random.uniform(126.8, 127.1)] for _ in range(100)]

HeatMap(heat_data).add_to(m)

m.save("folium/map_data/09_heatmap.html")