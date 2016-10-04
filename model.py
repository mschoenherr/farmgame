from kivy.properties import BoundedNumericProperty, ObjectProperty, ListProperty
from plant import *
from weather import Weather
from date import GameDate
from copy import copy

class GameState(ObjectProperty):

    plots = ListProperty()

    plots = [Plant() for ind in range(9)]

    plant_selection = ObjectProperty(None,True)
    plant_selection = carrots

    def update(self,dt):
        pass

    def plot_touched(self,index):

        self.plots[index] = self.plant_selection

        return copy(self)
        
