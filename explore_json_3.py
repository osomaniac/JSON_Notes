import json

## create/open files
infile = open("eq_data_30_day_m1.json", 'r')
outfile = open("readable_eq_data.json", 'w')

## load JSON data into dicitonary
eq_data = json.load(infile)

## dump readable dictionary data to outfile
json.dump(eq_data, outfile, indent=4)

## create lists
list_of_eqs = eq_data['features']
mags = []
lons = []
lats = []
hover_text = []

## add data to list of mags, longs, and lats
for eq in list_of_eqs:
    mag = eq['properties']['mag']
    title = eq['properties']['place']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)#
    lats.append(lat)
    hover_text.append(title)

'''
## print to see that it worked
print("MAGS:\n",mags[:10]) ## [:10] only prints the first ten items in the list, same as [0:10]
print("\nLONS:\n", lons[:10])
print("\nLATS:\n", lats[:10])
'''

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

##data = [Scattergeo(lon=lons, lat=lats)]

data = [{
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_text,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar' : {'title':'Magnitude'},
    }
    
}]
myLayout = Layout(title="Global Earthquakes")
fig = {'data':data, 'layout':myLayout}

offline.plot(fig, filename='global_earthquakes.html')