from plant import *
from weather import Weather
from date import GameDate

class GameState():

    def __init__(self):

        self.plots = [ Plant() for i in range(9)]

        self.money = 100

        self.plant_selection = carrots

        self.date = GameDate()

        self.weather = Weather(self.date)

    def update(self,dt)
        pass
        
