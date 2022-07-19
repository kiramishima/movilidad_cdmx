# Import matplotlib.pyplot
import matplotlib.pyplot as plt
# Import geopandas
import geopandas as gpd
# import Folium
import folium
from folium import Marker, GeoJson
from folium.plugins import MarkerCluster, HeatMap


# Path de nuestro shapefile
shapefile_path = './DATASET/Area de influencia de Ecobici (500 mts)/buffer_ecobici.shp'
# Leemos el archivo
areaEcobici = gpd.read_file(shapefile_path)
# Mostramos el contenido de las primeras 5 filas
print(areaEcobici.head())

# Print the contents of the service districts geometry in the first row
# print(ejes_viales.loc[0, 'geometry'])

# Print info
print('Tipo de datos')
print(type(areaEcobici))

print('Columnas del shape')
print(areaEcobici.columns)


print('Geoseries')
print(type(areaEcobici.geometry))

print('CRS')
print(areaEcobici.crs)
# areaEcobici.geometry.set_crs(epsg=4326)
# areaEcobici.crs = {'init' :'epsg:4326'}
# areaEcobici.to_crs({'init': 'epsg:4326'})
areaEcobici = areaEcobici.to_crs(epsg=4326)
print(areaEcobici.crs)

print('SHAPE')
print(areaEcobici.shape)

print('Info')
print(areaEcobici.info())

# Coordenadas de CDMX
cdmx = [19.432608, -99.133209]

# Plot
areaEcobici.plot()
plt.show()

# Creamos el mapa
m = folium.Map(location=cdmx, zoom_start=12, tiles='cartodbpositron')

# Geojson
geopath = areaEcobici.geometry.to_json()
#print(geopath)
poligonos = folium.features.GeoJson(geopath)
print(poligonos)
m.add_child(poligonos)
folium.LayerControl().add_to(m)


m.save("D:\\Workspace\\ws_python\\semovi\\area_ecobici\\index.html")