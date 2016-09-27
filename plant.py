class Plant():

    def __init__(self,name = "empty", phos= -0.001, nit = -0.001, kal = -0.001, max_gain=0):

        self.name = name
        self.phosphor_dt = phos
        self.nitrogen_dt = nit
        self.kalium_dt = kal
        self.gain = 0
        self.max_gain = max_gain

carrots = Plant("carrots",0.01,0.01,0.01,100)
potatoes = Plant("potatoes",0.02,0.02,0.02,300)
