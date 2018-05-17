import pandas
import folium

data = pandas.read_csv("Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def colour(el):
	if el < 1000:
		return 'red'
	elif el >= 1000 and el < 2000:
		return 'blue'
	elif el >= 2000 and el < 3000:
		return 'green'
	elif el >= 3000 and el < 4000:
		return 'orange'
	else:
		return  'black'

map = folium.Map(location = [38.58, -99.09], zoom_start = 5, tiles = "Mapbox Bright")

fgv = folium.FeatureGroup(name = "Volcanoes")

for lt,ln,nm,el in zip(lat,lon,name,elev):
	fgv.add_child(folium.Marker(location=[lt,ln], popup = folium.Popup(str(nm)+" ("+str(el)+"m)", parse_html = True) , icon = folium.Icon(color = colour(el))))
	# fg.add_child(folium.CircleMarker(location=[lt,ln], radius = 6,  popup = folium.Popup(str(nm)+" ("+str(el)+"m)", parse_html = True) , fill_color = colour(el), color = 'grey', fill = True, fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = 'Population')
fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding = 'utf-8-sig').read(), style_function = lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 100000000 else 'blue' if 100000000<= x['properties']['POP2005'] <= 500000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")