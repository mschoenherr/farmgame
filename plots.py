from util import bet_zero_hun
from math import pow,exp
from constants import g_empty
from plants import Plant
from fertilizer import Fertilizer

class Plot():

    def __init__(self,plant=Plant(),phos = 75, nit = 75, kal = 75, pesti = 10, bugs = 0,fert=None):

        self.plant = plant
        self.fertilizer = fert
        self.kalium = kal
        self.nitrogen = nit
        self.phosphor = phos
        self.pesticide = pesti
        self.bug_level = bugs
        self.gain = 0.0
        self.days_of_growth = 0
        self.crop_is_ripe = False

    def update(self,weather):

        days = self.plant.days_to_ripeness

        if not self.plant.name == g_empty:


            if self.kalium > self.plant.kalium/days and self.phosphor > self.plant.phosphor/days and self.nitrogen > self.plant.nitrogen/days:
                self.kalium -= self.plant.kalium/days
                self.nitrogen -= self.plant.nitrogen/days
                self.phosphor -= self.plant.phosphor/days
                
                self.gain += self.quality_based_gain(self.plant,weather)
                self.days_of_growth += 1

                if self.days_of_growth >= self.plant.days_to_ripeness:

                    self.crop_is_ripe = True

                #lacks pesticide application, and contamination!
        else:
                self.kalium -= self.plant.kalium/days
                self.nitrogen -= self.plant.nitrogen/days
                self.phosphor -= self.plant.phosphor/days



    def fertilize(self,fert):

        self.fert = fert

    def harvest(self):

        amount = self.gain
        name = self.plant.name

        self.gain = 0.0
        self.days_of_growth = 0 

        self.plant = Plant()

        return {"vegetable": name, "amount": amount}

    def sow(self,plant):

        self.plant = plant

    def quality_based_gain(self,plant,weather):

        max_gain_day = plant.max_gain/plant.days_to_ripeness

        hum_r = self.rangeHelper(weather.rain,plant.humidity_pref)
        sun_r = self.rangeHelper(weather.sun,plant.sun_pref)
        temp_r = self.rangeHelper(weather.temperature,plant.temp_pref)
        
        result = max_gain_day * hum_r * sun_r * temp_r * exp(-self.bug_level)

        #somehow soil contamination should count!

        return result

    def rangeHelper(self,x,pref):

        mean = pref[0]
        dev = pref[1]

        result = 1.0 - max(0,min(1,pow((x-mean)/dev,2)))

        return result
