from util import bet_zero_hun

# some global variables

g_reg = -10
g_tempr = range(10,30)
g_hum = range(25,60)
g_days = 120

class Plant():

    def __init__(self,name = "empty", phos= g_reg, nit = g_reg, kal = g_reg, max_gain=0.0,tempr = g_tempr,hum=g_hum,days=g_days):

        self.name = name
        self.phosphor = phos
        self.nitrogen = nit
        self.kalium = kal
        self.max_gain = max_gain
        self.temp_range = tempr
        self.humidity_range = hum
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

    def update(self,date,weather):

        self.gain += self.plant.max_gain/self.plant.days_to_ripeness
        self.days_of_growth += 1

    def harvest(self):

        amount = self.gain
        name = self.plant.name

        self.gain = 0
        self.days_of_growth = 0 

        self.plant = Plant()

        return {"vegetable": name, "amount": amount}

    def sow(self,plant):

        self.plant = plant


carrots = Plant("Carrots",10,20,10,100.0)

potatoes = Plant("Potatoes",20,10,10,100.0)

plant_dict = {"Carrots" : carrots, "Potatoes": potatoes}
plant_list = ["Carrots","Potatoes"]
