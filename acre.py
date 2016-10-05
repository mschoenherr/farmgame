from kivy.properties import NumericProperty, StringProperty
from util import bet_zero_hun
class Plant():

    name = StringProperty("empty")
    max_gain = NumericProperty(0)
    kalium = NumericProperty(0)
    nitrogen = NumericProperty(0)
    phosphor = NumericProperty(0)

    def __init__(self,name = "empty", phos= -0.001, nit = -0.001, kal = -0.001, max_gain=0):

        self.name = name
        self.phosphor = phos
        self.nitrogen = nit
        self.kalium = kal
        self.max_gain = max_gain

carrots = Plant("carrots",0.01,0.01,0.01,100)

potatoes = Plant("potatoes",0.02,0.02,0.02,300)
