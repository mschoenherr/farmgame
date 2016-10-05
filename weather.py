from random import randint

class Weather():

    def __init__(self):

        self.sun = randint(0,100)
        self.rain = randint(0,100)
        self.temperature = randint(-13,41)


    def update(self,dt,date):

        self.sun = randint(0,100)
        self.rain = randint(0,100)
        self.temperature = randint(-13,41)
        # in the future, calculate everything depending on date and prev weather

        
