from random import randint
from math import trunc
from constants import g_target_rain,g_target_sun,g_target_temperature,g_temp_bounds,g_sun_bounds,g_rain_bounds

class Weather():

    def __init__(self):

        self.target_temperature = g_target_temperature
        self.target_rain = g_target_rain
        self.target_sun = g_target_sun

        self.rain_tendency = 0
        self.sun_tendency = 0
        self.temperature_tendency = 0
        
        self.sun = self.target_sun[0]
        self.rain = self.target_rain[0]
        self.temperature = self.target_temperature[0]


    def update(self,date):

        self.sun += self.sun_tendency
        self.rain += self.rain_tendency
        self.temperature += self.temperature_tendency

        self.setSunTendency(date)
        self.setRainTendency(date)
        self.setTemperatureTendency(date)

    
    def setSunTendency(self,date):

        month = date.month

        det_trend = self.target_sun[month] - self.sun 
        rand_trend = randint(g_sun_bounds[0],g_sun_bounds[1]) - self.sun
        prev_tendency = self.sun_tendency
        
        self.sun_tendency = self.trendHelper(det_trend,rand_trend,prev_tendency)

    def setRainTendency(self,date):

        month = date.month

        det_trend = self.target_rain[month] - self.rain
        rand_trend = randint(g_rain_bounds[0],g_rain_bounds[1]) - self.rain
        prev_tendency = self.rain_tendency
        
        self.rain_tendency = self.trendHelper(det_trend,rand_trend,prev_tendency)

    def setTemperatureTendency(self,date):

        month = date.month

        det_trend = self.target_temperature[month] - self.temperature
        rand_trend = randint(g_temp_bounds[0],g_temp_bounds[1]) - self.temperature
        prev_tendency = self.temperature_tendency
        
        self.temperature_tendency = self.trendHelper(det_trend,rand_trend,prev_tendency)

    def trendHelper(self,det,ran,prev):

        trend = 0.7 * det + 0.15 * ran + 0.15 * prev

        return trunc(trend)

        # in the future, calculate everything depending on date and prev weather

        
