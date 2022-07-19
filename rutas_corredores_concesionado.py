# Import matplotlib.pyplot
import matplotlib.pyplot as plt
# Import geopandas
import geopandas as gpd
from shapely.geometry import Point, LineString
# import Folium
import folium
from folium import Marker, GeoJson
from folium.plugins import MarkerCluster, HeatMap
# import gdal
from osgeo import gdal


# Path de nuestro shapefile
shapefile_path = './DATASET/Area de influencia del Sistema de Transporte Colectivo, Metro (800 mts)/buffer_metro.shp'
# Leemos el archivo
rutasConcesionadas = gpd.read_file(shapefile_path)
# Mostramos el contenido de las primeras 5 filas
print(rutasConcesionadas.head())

# Print the contents of the service districts geometry in the first row
# print(ejes_viales.loc[0, 'geometry'])

# Print info
print('Tipo de datos')
print(type(rutasConcesionadas))

print('Columnas del shape')
print(rutasConcesionadas.columns)


print('Geoseries')
print(type(rutasConcesionadas.geometry))

print('CRS')
print(rutasConcesionadas.crs)
#ejes_viales.set_crs(epsg=4326)
rutasConcesionadas.crs = {'init' :'epsg:4326'}
# ejes_viales = ejes_viales.to_crs(epsg=4326)
print(rutasConcesionadas.crs)

print('SHAPE')
print(rutasConcesionadas.shape)

print('Info')
print(rutasConcesionadas.info())

# Coordenadas de CDMX
cdmx = [19.432608, -99.133209]

# Plot
rutasConcesionadas.plot()
plt.show()

# Creamos el mapa
m = folium.Map(location=cdmx, zoom_start=12, tiles='cartodbpositron')

# Geojson
geopath = rutasConcesionadas.geometry.to_json()
#print(geopath)
poligonos = folium.features.GeoJson(geopath)
print(poligonos)
m.add_child(poligonos)
folium.LayerControl().add_to(m)


m.save("D:\\Workspace\\ws_python\\semovi\\ruta_concesionada\\index.html")