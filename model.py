from kivy.properties import BoundedNumericProperty, ObjectProperty, ListProperty
from acre import *
from weather import Weather
from date import GameDate
from copy import copy
# always return copies of yourself so that object reference to gamestate is updated
# there might be a better way using dispatch but i haven't got that working, yet
class GameState():

    plots = ListProperty()


    plant_selection = ObjectProperty(None,True)

    
    def __init__(self):

        self.plots = [Plot() for ind in range(9)]
        self.plant_selection = carrots
        self.date = GameDate()
        self.weather = Weather()

    def update(self,dt):

        for plot in self.plots:

            plot.update(dt,self.weather)

        self.weather.update(dt,self.date)

        self.date.update()

        return copy(self)

    def plot_touched(self,index):

        self.plots[index] = Plot(self.plant_selection)

        return copy(self)
        
