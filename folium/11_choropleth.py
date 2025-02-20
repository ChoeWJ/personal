import folium
import geopandas as gpd

geo_data = "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json"

m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

data = {
    "California": 100,
    "Texas": 200,
    "Florida": 150
}

folium.Choropleth(
    geo_data=geo_data,
    name='choropleth',
    data=data,
    columns=["Califonia", "Texas"],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2
).add_to(m)

m.save('folium/map_data/11_choropleth.html')