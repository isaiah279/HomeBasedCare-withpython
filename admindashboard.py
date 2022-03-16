import tkinter
from tkintermapview import TkinterMapView
from tkinter import ttk
from tkinter import *
import threading
from kivymd.uix.datatables import MDDataTable
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import dp
import kivy
import json
import requests
from kivymd.uix.list import TwoLineListItem
from kivymd.app import MDApp
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.lang import Builder
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.snackbar import Snackbar
# Floatlayout allows us to place the elements
# relatively based on the current window
# size and height especially in mobiles
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import mainthread
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

root_tk = tkinter.Tk()

from kivy.animation import Animation, AnimationTransition, CompoundAnimation


class Tab(MDFloatLayout, MDTabsBase):
    """Class implementing content for a tab."""


class Home(MDFloatLayout, MDTabsBase):
    pass


class Location(MDFloatLayout, MDTabsBase):
    pass


class Database(MDFloatLayout, MDTabsBase):
    pass


class Register(MDFloatLayout, MDTabsBase):
    def registered(self, register):
        print("yess")


class RootLayout(MDFloatLayout):
    stop = threading.Event()


class comments(MDFloatLayout, MDTabsBase):
    pass


TRIPS_SELECTED = []


class MainMDApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        self.auth_key = "lj6Vvz1LRVOjS4u5bG25GNGL6uap2WJF9NRlPbpk"
        super().__init__(**kwargs)

    def on_starting(self):
        self.instart()

    id = 1

    def instart(self, *args):
        anim = Animation(opacity=1, duration=1)
        anim += Animation(opacity=1, duration=3)
        anim += Animation(opacity=0, duration=1)
        anim.bind(on_complete=self.instart)
        anim.instart(self.root.ids[f"text{self.id}"])

        if self.id < 4:
            self.id += 1
        else:
            self.id -= 3

    def on_start(self):
        self.root.ids.database.text = "up dated"

    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('admindash.kv')

    def databaseRegistry(self, database):
        url = "https://isaifirst-434b9-default-rtdb.firebaseio.com/.json"
        from_database = requests.get(url=url + '?auth=' + self.auth_key)
        new_label = self.root.ids.list

        for key, value in enumerate(from_database):
            print(key, value)
            print("hello wleon")
            widget = TwoLineListItem(text=f"{value}")
            new_label.add_widget(widget)
            new_label.text = str(key)

        # for data in database.json():
        # new_label.text =x.text
        # db = new_label.text="

    def delete(self, database):
        requests.delete(url=self.url[:-1] + database + ".json")

    auth_key = 'bTwFAO5zo89eyXpTu30B4C3Fh2hsw3p3JBDZOgYA'  # Refer to the YouTube video on where to find this.

    def update(self, database):
        requests.put(url=self.url[:-1] + database + ".json")

    auth_key = 'bTwFAO5zo89eyXpTu30B4C3Fh2hsw3p3JBDZOgYA'  # Refer to the YouTube video on where to find this.

    def registered(self, register):
        print("am working well")

    def emergencies(self, emergency):
        print()

    def get_location(self, location):

        root_tk.geometry(f"{1000}x{900}")
        root_tk.title("Location of The Target point")
        # create map widget
        map_widget = TkinterMapView(root_tk, width=600, height=400, corner_radius=0)
        map_widget.pack(fill="both", expand=True)

        # google normal tile server
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)

        map_widget.set_address(location, marker=True)

        root_tk.mainloop()

        def findLocation(self, location):
            self.url = "https://isaifirst-434b9-default-rtdb.firebaseio.com/.json"
            if len(location) == 2:
                err = Snackbar(text="NO Blank Space Allowed")
                err.open()
            else:
                if len(location) >= 3:
                    err = Snackbar(text="Sucess")

                    JSON = {"userLocation": f"{location}"}
                    re = requests.patch(url=self.url, json=JSON)

    def add_Records(self, get_patient_record):
        print("Records are:")

    def commenting(self, comments):
        print(" here are the comments:")


MainMDApp().run()
