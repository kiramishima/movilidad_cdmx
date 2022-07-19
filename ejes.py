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
shapefile_path = './DATASET/Principales Ejes viales/ejes_viales.shp'
# Leemos el archivo
ejes_viales = gpd.read_file(shapefile_path)
# Mostramos el contenido de las primeras 5 filas
print(ejes_viales.head())
print(ejes_viales.head(-5))

# Print the contents of the service districts geometry in the first row
# print(ejes_viales.loc[0, 'geometry'])

# Print info
print('Tipo de datos')
print(type(ejes_viales))

print('Columnas del shape')
print(ejes_viales.columns)

print('Geoseries')
print(type(ejes_viales.geometry))

print('CRS')
print(ejes_viales.crs)
# ejes_viales.set_crs(epsg=4326)
# ejes_viales.crs = {'init' :'epsg:4326'}
# ejes_viales = ejes_viales.to_crs(epsg=4326)
ejes_viales = ejes_viales.to_crs(epsg=4326)
print(ejes_viales.crs)

print('SHAPE')
print(ejes_viales.shape)

print('Info')
print(ejes_viales.info())

# Coordenadas de CDMX
cdmx = [19.432608, -99.133209]

# Creamos el mapa
m = folium.Map(location=cdmx, zoom_start=12, tiles='cartodbpositron')


def shapeFile2GeoJSON(infile, outfile):
    '''Convierte un shapefile a geojson'''
    options = gdal.VectorTranslateOptions(format="GeoJSON", dstSRS="EPSG:4326")
    gdal.VectorTranslate(outfile, infile, options=options)


# Convertimos
infile = './DATASET/Principales Ejes viales/ejes_viales.shp'
outfile = 'D:\Workspace\ws_python\semovi\DATASET\Principales Ejes viales\ejes_viales.geojson'


# shapeFile2GeoJSON(infile, outfile)

# g = folium.GeoJson(
#    outfile,
#    name='geojson'
# ).add_to(m)

# folium.GeoJsonTooltip(fields=['Name']).add_to(g)
def getColor(feature):
    match int(feature['id']):
        case 1:
            return 'red'
        case 2:
            return 'green'
        case _:
            return 'red'


# Geojson
geopath = ejes_viales.geometry.to_json()
# print(geopath)
poligonos = folium.features.GeoJson(geopath, style_function=lambda x: {
    'color': getColor(x)
})
print(poligonos)
m.add_child(poligonos)
folium.LayerControl().add_to(m)

ejes_viales.plot("Name", legend=True)
plt.show()

# for _, r in ejes_viales.iterrows():
# Without simplifying the representation of each borough,
# the map might not be displayed
#    sim_geo = gpd.GeoSeries(r['geometry']).simplify(tolerance=0.001)
#    print(sim_geo)
#    geo_j = sim_geo.to_json()
#    print(geo_j)
#    geo_j = folium.GeoJson(data=geo_j,
#                           style_function=lambda x: {'fillColor': 'orange'})
#    folium.Popup(r['Name']).add_to(geo_j)
#    geo_j.add_to(m)

# g = folium.GeoJson(
#    poligonos,
#    name='geojson'
# ).add_to(m)

# folium.GeoJsonTooltip(fields=['Name']).add_to(m)
ejes_viales.explore()

m.save("D:\Workspace\ws_python\semovi\ejes\index.html")
