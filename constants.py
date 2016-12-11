# g_dt gives time between two update ticks
g_dt = 0.5
g_days_of_year = 365
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
g_storage = {"Carrots" : {"amount" : 0.0, "days":120}, "Potatoes": {"amount":0.0, "days": 200} \
        , "Strawberry": {"amount" : 0.0, "days": 30}, "Cabbage": {"amount" : 0.0, "days": 120} \
        , "Corn": {"amount": 0.0, "days": 100}, "Cauliflower": {"amount": 0.0, "days": 99}}

# money stuff
g_prices = {"Carrots" : {"buy" : 25, "sell": 0.3, "buy_tendency": 0.0, "sell_tendency": 0.0} \
        ,"Potatoes" : {"buy" : 30, "sell": 0.4 , "buy_tendency": 0.0, "sell_tendency": 0.0} \
        ,"Strawberry" : {"buy" : 30, "sell": 0.4 , "buy_tendency": 0.0, "sell_tendency": 0.0} \
        ,"Corn" : {"buy" : 30, "sell": 0.4 , "buy_tendency": 0.0, "sell_tendency": 0.0} \
        ,"Cabbage" : {"buy" : 30, "sell": 0.4 , "buy_tendency": 0.0, "sell_tendency": 0.0} \
        ,"Cauliflower" : {"buy" : 30, "sell": 0.4 , "buy_tendency": 0.0, "sell_tendency": 0.0}}

g_fert_prices = {"Kalium": {"buy": 5.0, "buy_tendency": 0.0} \
                ,"Nitrogen": {"buy": 5.0, "buy_tendency": 0.0} \
                ,"Phosphor": {"buy": 5.0, "buy_tendency": 0.0}}

g_start_money = 100.0

# default values for plant initialisation
g_reg = -5.0
g_tempr = [15,7] 
g_hum = [40,30] 
g_sun = [40,30]
g_days = 120
g_water_pref = [50.0,20]
g_plant_list = ["Carrots","Potatoes","Strawberry","Corn","Cabbage","Cauliflower"]

# default values for fertilizers

g_fert_list = ["Kalium","Nitrogen","Phosphor"]
g_abs_rate = 0.1
g_fert_quant = 10.0

#value under which a fertilizer is removed
g_fert_min = 0.1

# initialization parameters for plots

g_phos = 75
g_kal = 75
g_nit = 75
g_pesti = 0
g_water = 40

# name for null-objects, used to check wether plot has a plant and is equal to the name of an empty image
g_empty = "empty"
g_nil = "Nil"

# days between price and weather updates
g_days_to_update = 7
g_tempvar = 2.0

# default values for price progression

g_price_variance = 0.01
g_price_drift = pow(1.025,g_days_to_update/g_days_of_year)
