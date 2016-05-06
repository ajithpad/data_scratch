from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='merc', lat_0 = 20, lon_0 = 80,
    resolution = 'h', area_thresh = 1.,
    llcrnrlon=68.0, llcrnrlat=8.0,
    urcrnrlon=95.0, urcrnrlat=37.0)

map.drawmapboundary(fill_color='#1E90FF')
map.fillcontinents(color='#ddaa66',lake_color='#1E90FF')
map.drawcoastlines()
map.drawcountries()

#map.readshapefile('/Users/ajith/bigdata/data/IND_adm_shp/IND_adm2', 'States')
#for ii in range(len(city_lon)):
#    lat = city_lat[ii]
#    lon = city_lon[ii]
#    x,y = map(lon, lat)
#    map.plot(x, y, 'ro',markersize=6, alpha = 0.6)
plt.show()