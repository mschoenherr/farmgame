# g_dt gives time between two update ticks
g_dt = 0.8
# Mean values for weathers deterministic part
g_target_temperature = [2,4,8,12,19,22,24,24,19,14,7,4]
g_target_rain = [50,30,38,50,25,60,60,80,45,70,90,30]
g_target_sun = [15,40,50,80,90,80,90,80,50,40,30,40]

# bounds give the values between which sun, temperature and rain vary
g_temp_bounds = [-10,40]
g_sun_bounds = [0,100]
g_rain_bounds = [0,100]

# date ranges holds "intervals" of days numbers belonging to the respective month
g_date_ranges = [[0,30],[31,58],[59,89],[90,119],[120,150],[151,180],[181,211],[212,242],[243,272],[273,303],[304,333],[334,365]]
g_month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
g_start_year = 2016

# storage values are pairs of (amount,days_to_perish)
g_storage = {"Carrots" : {"amount" : 0.0, "days":120}, "Potatoes": {"amount":0.0, "days": 200}}
g_prices = {"Carrots" : {"buy" : 25, "sell": 0.3, "buy_tendency": 0.0, "sell_tendency": 0.0} \
        ,"Potatoes" : {"buy" : 30, "sell": 0.4 , "buy_tendency": 0.0, "sell_tendency": 0.0}}
g_start_money = 100.0

# default values for plant initialisation
g_reg = -10.0
g_tempr = [15,7] 
g_hum = [40,30] 
g_sun = [40,30]
g_days = 120.0
g_plant_list = ["Carrots","Potatoes"]

# name for null-plant, used to check wether plot has a plant and so on
g_empty = "empty"
