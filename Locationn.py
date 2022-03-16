"""import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from tobelocated import number
from opencage.geocoder import OpenCageGeocode
import folium
sanumber = phonenumbers.parse(number)
your_location = geocoder.description_for_number(sanumber, "en")
# getting service provide
print(your_location)
Key = 'eda1bd6e70254ffc968fb99a3f4eece1'
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))
geocoder = OpenCageGeocode(Key)
query=str(your_location)
result=geocoder.geocode(query)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)
myMap=folium.Map(location=[lat,lng],zoom_start=20)
folium.Marker([lat,lng],popup=your_location).add_to((myMap))
myMap.save("myLocation.html")
"""

import tkinter
from tkintermapview import TkinterMapView
from tkinter import ttk
from tkinter import *
def new_fun(self,*args):
    root_tk = tkinter.Tk()
    root_tk.geometry(f"{600}x{400}")
    root_tk.title("map_view_simple_example.py")
    # create map widget
    map_widget = TkinterMapView(root_tk, width=600, height=400, corner_radius=0)
    map_widget.pack(fill="both", expand=True)

    # google normal tile server
    self = map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

    map_widget.set_address('Nairobi', marker=True)

    root_tk.mainloop()
new_fun('yt')