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
        self.available_plants = plant_list
        self.plant_selection = 0
        self.date = GameDate()
        self.weather = Weather()

        # storage values are pairs of (amount,days_to_perish)
        self.storage = {"Carrots" : {"amount" : 0.0, "days":120}, "Potatoes": {"amount":0.0, "days": 200}}

    def update(self):

        for plot in self.plots:

            plot.update(self.date,self.weather)

        self.weather.update(self.date)

        self.date.update()

        return copy(self)

    def activate_plot(self,index):

        if self.plots[index].plant.name == "empty":

            self.plots[index].sow(self.available_plants[self.plant_selection])

        else:

            self.harvest_plot(index)

        return copy(self)

    def harvest_plot(self,index):

        result = self.plots[index].harvest()

        self.storage[result["vegetable"]]["amount"] += result["amount"]

        return copy(self)

    def perish_storage(self):

        for key in self.storage:

                self.storage[key] += perish_func(self.storage[key]["amount"],self.storage[key]["days"])
