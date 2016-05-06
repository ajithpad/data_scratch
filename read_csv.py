import numpy as np
import csv
import re
import pylab as pl
import seaborn as sbn
from mpld3 import plugins
import mpld3
#mpld3.enable_notebook()

city_name = []
city_pop_2000 = []
city_pop_2010 = []
city_pop_2020 = []
city_lat = []
city_lon = []

with open('/Users/ajith/bigdata/data/indicator_data_IN.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if "urban_population_cities" in row:
            if row[-2] == '2000':
                city_name.append(row[-3])
                city_pop_2000.append(int(row[-1]))
                city_lat.append(float(row[-7]))
                city_lon.append(float(row[-6]))
            if row[-2] == '2010':   
                city_pop_2010.append(int(row[-1]))
            if row[-2] == '2020':   
                city_pop_2020.append(int(row[-1]))
                
                

#city_arr = np.zeros([len(city_name),4], dtype = ([('keys','|S1'), ('data1','f8'), ('data2','f8'),('data3','f8')]))
fig = pl.figure(1)
ax = fig.add_axes([0.1,0.25,0.8,0.7])
records = np.rec.fromarrays((np.array(city_name), np.array(city_pop_2000),np.array(city_pop_2010),np.array(city_pop_2020), np.array(city_lat),np.array(city_lon)), names=('keys', 'data1', 'data2','data3','lat', 'lon'))
records.sort(order = 'data1')
#records.sort(reverse = True)
#city_arr[:,0] = city_name[:] 
#sbn.barplot(x = city_name, y = city_pop_2000 )
p3 = sbn.barplot(records['keys'],records['data3'], color = '#7B68EE', label = '2020')
p1 = sbn.barplot(records['keys'],records['data2'], color = '#2E8B57', label = '2010')
p2 = sbn.barplot(records['keys'],records['data1'], color = '#FF6347', label = '2000')
#pl.xticks(range(len(city_name)), city_name, rotation = 90)
pl.xticks(rotation = 90, size = 16)
pl.yticks(size = 17)
#pl.yscale('log')
pl.ylabel('Population in 000s', size = 18)
legend = pl.legend(title = 'Year', loc = 2, prop = {'size':18})
pl.setp(legend.get_title(),fontsize=18)
fig.text(0.95,0.7,'Source: UN Habitat - Urban Data', rotation = 90)

fig2 = pl.figure(2)
ax2 = fig2.add_axes([0.1,0.15,0.8,0.8])
percent_growth = (records['data2'] - records['data1'])*100./records['data1']

scatter = ax2.scatter(records['data1'], percent_growth, s = 100., alpha = 0.4, c = records['lat']*20, cmap = pl.cm.Reds)
ax2.set_xlim(0,20000)
pl.xticks(size = 16)
pl.yticks(size = 16)
pl.ylabel('% Increase in population (2000-10)', size = 18)
pl.xlabel('Population in year 2000 in 000s', size = 18)
labels = [i for i in records['keys']]
#fig2.plugins = [plugins.PointLabelTooltip(scatter, labels)]
tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
mpld3.plugins.connect(fig2, tooltip)
mpld3.save_html(fig2, 'mpld3_test.html')                     
#pl.show()
#mpld3.show()

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
fig3 = pl.figure(3)
map = Basemap(projection='merc', lat_0 = 20, lon_0 = 80,
    resolution = 'h', area_thresh = 1.,
    llcrnrlon=68.0, llcrnrlat=8.0,
    urcrnrlon=95.0, urcrnrlat=37.0)

map.drawmapboundary(fill_color='#1E90FF')
map.fillcontinents(color='#ddaa66',lake_color='#1E90FF')
map.drawcoastlines()
map.drawcountries()

#map.readshapefile('/Users/ajith/bigdata/data/IND_adm_shp/IND_adm2', 'States')
#map.scatter(records['lat'], records['lon'], latlon = False, s = 10.)
#for ii in range(len(city_lon)):
#    lat = records['lat'][ii]
#    lon = records['lon'][ii]
#    col_val = int(percent_growth[ii]*4)
#    x,y = map(lon, lat)
#    map.plot(x, y,'o',markersize=8, alpha = 0.5,color = pl.cm.Reds(col_val))
plt.show()