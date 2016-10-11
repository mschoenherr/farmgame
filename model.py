from plots import Plot
from plants import g_plant_dict
from weather import Weather
from date import GameDate
from copy import copy
from util import perish_func,cut_off_gauss
from constants import g_storage,g_prices,g_start_money,g_plant_list,g_empty,g_days_to_update, g_price_variance, g_price_drift
# always return copies of yourself so that object reference to gamestate is updated
# there might be a better way using dispatch but i haven't got that working, yet

class GameState():

    def __init__(self):

        self.plots = [Plot() for ind in range(9)]
        self.available_plants = g_plant_dict
        self.all_plants = g_plant_list
        self.plant_selection = self.all_plants[0]
        self.date = GameDate()
        self.weather = Weather()
        self.money = g_start_money

        self.storage = g_storage
        self.prices = g_prices

        self.since_praw_update = 0

    def update(self):

        for plot in self.plots:

            plot.update(self.weather)

        self.date.update()

        self.perish_storage()

        if self.since_praw_update == g_days_to_update:

            self.weather.update(self.date)

            self.update_prices()

            self.since_praw_update = 0

        else:

            self.since_praw_update += 1

        return copy(self)

    def activate_plot(self,index):

        if self.plots[index].plant.name == g_empty:

            seed = self.available_plants[self.plant_selection]

            if self.money >= self.prices[seed.name]["buy"]:

                self.plots[index].sow(seed)

                self.money -= self.prices[seed.name]["buy"]

        elif self.plots[index].crop_is_ripe:

            self.harvest_plot(index)

        return copy(self)

    def cycle_plant_list(self):

        last = self.all_plants.pop()

        self.all_plants = [last] + self.all_plants

        self.plant_selection = self.all_plants[0]

        return copy(self)

    def harvest_plot(self,index):

        result = self.plots[index].harvest()

        self.storage[result["vegetable"]]["amount"] += result["amount"]

        return copy(self)

    def perish_storage(self):

        for key in self.storage:

                self.storage[key]["amount"] = perish_func(self.storage[key]["amount"],self.storage[key]["days"])

    def update_prices(self):

        for key in self.prices:

            buy_tendency = self.prices[key]["buy_tendency"]
            sell_tendency = self.prices[key]["sell_tendency"]
            buy = self.prices[key]["buy"]
            sell = self.prices[key]["sell"]

            self.prices[key]["buy"] += buy_tendency
            self.prices[key]["sell"] += sell_tendency

            self.prices[key]["buy_tendency"] = cut_off_gauss(0,float("inf"),buy * g_price_drift, buy * g_price_variance) - buy
            self.prices[key]["sell_tendency"] = cut_off_gauss(0,float("inf"),sell * g_price_drift, sell * g_price_variance) - sell


    def sell(self,vegetable_name):

        amount = self.storage[vegetable_name]["amount"]

        max_gain = self.available_plants[vegetable_name].max_gain

        price_per_ton = self.prices[vegetable_name]["sell"]

        self.storage[vegetable_name]["amount"] = 0.0

        self.money += price_per_ton * amount

        return copy(self)
