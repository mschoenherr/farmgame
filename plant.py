from kivy.properties import NumericProperty, StringProperty
from util import bet_zero_hun
class Plant():

    def __init__(self,name = "empty", phos= -0.001, nit = -0.001, kal = -0.001, max_gain=0):

        self.name = StringProperty("empty")
        self.name = name
        self.phosphor = NumericProperty(0)
        self.phosphor = phos
        self.nitrogen = NumericProperty(0)
        self.nitrogen = nit
        self.kalium = NumericProperty(0)
        self.kalium = kal
        self.max_gain = NumericProperty(0)
        self.max_gain = max_gain

carrots = Plant("carrots",0.01,0.01,0.01,100)
potatoes = Plant("potatoes",0.02,0.02,0.02,300)
