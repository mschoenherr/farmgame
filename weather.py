from random import randint

class Weather():

    def __init__(self,date):

        self.sun = randint(0,100)
        self.temperature = randint(-10,40)
        self.rain = randint(0,100)

        # in the future, calculate everything depending on date and prev weather

        
