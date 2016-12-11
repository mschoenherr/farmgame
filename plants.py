from constants import g_reg,g_tempr,g_hum,g_sun,g_days,g_plant_list,g_empty,g_water_pref

class Plant():

    def __init__(self,name = g_empty, phos= g_reg, nit = g_reg, kal = g_reg, max_gain=0.0,tempr = g_tempr,sun = g_sun,water = g_water_pref,days=g_days):

        self.name = name
        self.phosphor = phos
        self.nitrogen = nit
        self.kalium = kal
        self.max_gain = max_gain
        self.temp_pref = tempr
        self.sun_pref = sun
        self.water_pref = water
        self.days_to_ripeness = days

# target weather values for reference
# g_target_temperature = [2,4,8,12,19,22,24,24,19,14,7,4]
# g_target_rain = [50,30,38,50,25,60,60,80,45,70,90,30]
# g_target_sun = [15,40,50,80,90,80,90,80,50,40,30,40]

carrots = Plant("Carrots",30.0,5.0,5.0,100.0,[20,9],[85,15],[53.0,20.0],180)

potatoes = Plant("Potatoes",20.0,20.0,5.0,200.0,[20,9],[85,15],[53.0,20.0],180)

strawberry = Plant("Strawberry",5.0,20.0,20.0,100.0,[21,10],[85,15],[48.0,15.0],120)

corn = Plant("Corn",20.0,5.0,20.0,200.0,[20,9],[85,15],[53.0,20.0],180)

cabbage = Plant("Cabbage",5.0,30.0,5.0,100.0,[6,10],[35,20],[51.0,30],180)

cauliflower = Plant("Cauliflower",5.0,5.0,30.0,100.0,[10,9],[37,15],[50.0,30],210)

g_plant_dict = {g_plant_list[0] : carrots, g_plant_list[1]: potatoes, g_plant_list[2]: strawberry, g_plant_list[3]: corn, g_plant_list[4]: cabbage, g_plant_list[5]: cauliflower}
