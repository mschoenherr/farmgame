class Fertilizer():

    def __init__(self,name="Kalium",quantity=10,absorbing_rate=0.01):

        self.name = name
        self.quantity = quantity
        self.absorbing_rate=0.01

    def diffusionAmount(self,fert_level,water_level):

        quantity = self.quantity * self.absorbing_rate

        self.quantity -= quantity

        return quantity

Kalium = Fertilizer("Kalium",10,0.01)
Nitrogen = Fertilizer("Nitrogen",10,0.01)
Phosphor = Fertilizer("Phosphor",10,0.01)

g_fert_dict = {"Kalium": Kalium, "Nitrogen": Nitrogen, "Phosphor": Phosphor}
