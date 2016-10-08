from random import randint
from math import trunc

class Weather():

    def __init__(self):

        self.target_temperature = [0,3,5,9,15,19,20,19,18,11,8,7]
        self.target_rain = [50,30,38,50,25,60,60,80,45,70,90,30]
        self.target_sun = [15,40,50,80,90,80,90,80,50,40,30,40]

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
        rand_trend = randint(0,100) - self.sun
        
        self.sun_tendency = trunc(0.7 * det_trend + 0.3 * rand_trend)

    def setRainTendency(self,date):

        month = date.month

        det_trend = self.target_rain[month] - self.rain
        rand_trend = randint(0,100) - self.rain
        
        self.rain_tendency = trunc(0.7 * det_trend + 0.3 * rand_trend)

    def setTemperatureTendency(self,date):

        month = date.month

        det_trend = self.target_temperature[month] - self.temperature
        rand_trend = randint(-10,40) - self.temperature
        
        self.temperature_tendency = trunc(0.7 * det_trend + 0.3 * rand_trend)


        # in the future, calculate everything depending on date and prev weather

        
