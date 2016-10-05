from kivy.properties import BoundedNumericProperty, ObjectProperty, ListProperty
from acre import *
from weather import Weather
from date import GameDate
from copy import copy

from util import perish_func
# always return copies of yourself so that object reference to gamestate is updated
# there might be a better way using dispatch but i haven't got that working, yet

class GameState():

    plots = ListProperty()


    plant_selection = ObjectProperty(None,True)

    
    def __init__(self):

        self.plots = [Plot() for ind in range(9)]
        self.available_plants = plant_dict
        self.plant_selection = "Carrots"
        self.date = GameDate()
        self.weather = Weather()
        self.money = 100

        # storage values are pairs of (amount,days_to_perish)
        self.storage = {"Carrots" : {"amount" : 0.0, "days":120}, "Potatoes": {"amount":0.0, "days": 200}}
        self.prices = {"Carrots" : {"buy" : 25, "sell": 30},"Potatoes" : {"buy" : 30, "sell": 40}}

    def update(self):

        for plot in self.plots:

            plot.update(self.date,self.weather)

        self.weather.update(self.date)

        self.date.update()

        self.perish_storage()

        return copy(self)

    def activate_plot(self,index):

        if self.plots[index].plant.name == "empty":

            seed = self.available_plants[self.plant_selection]

            if self.money >= self.prices[seed.name]["buy"]:

                self.plots[index].sow(seed)

                self.money -= self.prices[seed.name]["buy"]

        else:

            self.harvest_plot(index)

        return copy(self)

    def harvest_plot(self,index):

        result = self.plots[index].harvest()

        self.storage[result["vegetable"]]["amount"] += result["amount"]

        return copy(self)

    def perish_storage(self):

        for key in self.storage:

                self.storage[key]["amount"] = perish_func(self.storage[key]["amount"],self.storage[key]["days"])

    def sell(self,vegetable_name):

        amount = self.storage[vegetable_name]["amount"]

        max_gain = self.available_plants[vegetable_name].max_gain

        price_per_ton = self.prices[vegetable_name]["sell"]

        self.storage[vegetable_name]["amount"] = 0.0

        self.money += price_per_ton * amount / max_gain

        return copy(self)
