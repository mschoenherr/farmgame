from util import bet_zero_hun
from math import pow,exp
from constants import g_empty,g_phos,g_nit,g_kal,g_pesti,g_water,g_days_of_year, g_fert_min
from plants import Plant
from fertilizer import Fertilizer

class Plot():

    def __init__(self,plant=Plant(),phos = g_phos, nit = g_nit, kal = g_kal, water = g_water,fert=Fertilizer(),pesti= g_pesti):

        self.plant = plant
        self.fertilizer = fert
        self.kalium = kal
        self.nitrogen = nit
        self.phosphor = phos
        self.pesticide = pesti
        self.water_level = water
        self.gain = 0.0
        self.days_of_growth = 0
        self.crop_is_ripe = False

    def update(self,weather):

        days = self.plant.days_to_ripeness

        # update nutritients in soil

        if self.fertilizer.quantity < g_fert_min:
                    
            self.fertilize(Fertilizer())

        if self.fertilizer.name == "Kalium":

            self.kalium += self.fertilizer.diffusionAmount(self.water_level)
        elif self.fertilizer.name == "Phosphor":

            self.phosphor += self.fertilizer.diffusionAmount(self.water_level)
        elif self.fertilizer.name == "Nitrogen":

            self.nitrogen += self.fertilizer.diffusionAmount(self.water_level)

        # if there is something planted, grow it
        if not self.plant.name == g_empty:

            # days of growth are incremented here, so that there is finite amount of time where a plant can grow, preventing indefinite growth
            self.days_of_growth += 1
            # if there are not enoug nutritients in the soil, do not grow the plant
            if self.kalium > self.plant.kalium/days and self.phosphor > self.plant.phosphor/days and self.nitrogen > self.plant.nitrogen/days and self.water_level > self.plant.water_pref[0]/days:

                # water is absorbed according to the weather


                # the gained quanitity depends on the weather
                self.gain += self.quality_based_gain(self.plant,weather)

            
            # the crop is worthless after 14 days

            if self.days_of_growth >= days + 14:
                self.sow(Plant())
                self.gain = 0
                self.crop_is_ripe = False
                self.days_of_growth = 0
            
            elif self.days_of_growth >= days:

                self.crop_is_ripe = True

        #lacks pesticide application, and contamination!
        self.kalium -= self.plant.kalium/days
        self.nitrogen -= self.plant.nitrogen/days
        self.phosphor -= self.plant.phosphor/days
        self.water_level += self.plant.water_pref[0]/days - weather.rain*1.0/g_days_of_year

        self.kalium = bet_zero_hun(self.kalium)
        self.phosphor = bet_zero_hun(self.phosphor)
        self.nitrogen = bet_zero_hun(self.nitrogen)
        self.water_level = bet_zero_hun(self.water_level)

    def fertilize(self,fert):

        self.fertilizer = fert

    def harvest(self):

        amount = self.gain
        name = self.plant.name

        self.gain = 0.0
        self.days_of_growth = 0 
        self.crop_is_ripe = False

        self.sow(Plant())

        return {"vegetable": name, "amount": amount}

    def sow(self,plant):

        self.plant = plant

    def quality_based_gain(self,plant,weather):

        max_gain_day = plant.max_gain/plant.days_to_ripeness

        wat_r = self.rangeHelper(self.water_level,plant.water_pref)
        sun_r = self.rangeHelper(weather.sun,plant.sun_pref)
        temp_r = self.rangeHelper(weather.temperature,plant.temp_pref)
        
        result = max_gain_day * (wat_r + sun_r + temp_r)/3

        #somehow soil contamination should count! and bug level

        return result

    def rangeHelper(self,x,pref):

        mean = pref[0]
        dev = pref[1]

        result = 1.0 - max(0,min(1,pow((x-mean)/dev,2)))

        return result
