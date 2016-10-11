from constants import g_reg,g_tempr,g_hum,g_sun,g_days,g_plant_list,g_empty

class Plant():

    def __init__(self,name = g_empty, phos= g_reg, nit = g_reg, kal = g_reg, max_gain=0.0,tempr = g_tempr,hum=g_hum,sun = g_sun,days=g_days):

        self.name = name
        self.phosphor = phos
        self.nitrogen = nit
        self.kalium = kal
        self.max_gain = max_gain
        self.temp_pref = tempr
        self.humidity_pref = hum
        self.sun_pref = sun
        self.days_to_ripeness = days

carrots = Plant("Carrots",10,20,10,100.0)

potatoes = Plant("Potatoes",20,10,10,100.0)

strawberry = Plant("Strawberry")

corn = Plant("Corn")

cabbage = Plant("Cabbage")

cauliflower = Plant("Cauliflower")

g_plant_dict = {g_plant_list[0] : carrots, g_plant_list[1]: potatoes, g_plant_list[2]: strawberry, g_plant_list[3]: corn, g_plant_list[4]: cabbage, g_plant_list[5]: cauliflower}
