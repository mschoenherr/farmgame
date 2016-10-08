from util import bet_zero_hun
from math import pow,exp

# some global variables

g_reg = -10.0
g_tempr = [20,10] 
g_hum = [40,20] 
g_sun = [40,20]
g_days = 120.0

class Plant():

    def __init__(self,name = "empty", phos= g_reg, nit = g_reg, kal = g_reg, max_gain=0.0,tempr = g_tempr,hum=g_hum,sun = g_sun,days=g_days):

        self.name = name
        self.phosphor = phos
        self.nitrogen = nit
        self.kalium = kal
        self.max_gain = max_gain
        self.temp_pref = tempr
        self.humidity_pref = hum
        self.sun_pref = sun
        self.days_to_ripeness = days

class Plot():

    def __init__(self,plant=Plant(),phos = 75, nit = 75, kal = 75, pesti = 10, bugs = 0):

        self.plant = plant
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

        if not self.plant.name == "empty":


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



    def harvest(self):

        amount = self.gain
        name = self.plant.name

        self.gain = 0
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

        result = max(0,pow(x-mean,2) - pow(dev,2))

        return result


carrots = Plant("Carrots",10,20,10,100.0)

potatoes = Plant("Potatoes",20,10,10,100.0)

plant_dict = {"Carrots" : carrots, "Potatoes": potatoes}
plant_list = ["Carrots","Potatoes"]
