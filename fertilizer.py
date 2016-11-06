from constants import g_empty, g_abs_rate, g_fert_quant

class Fertilizer():

    def __init__(self,name=g_empty,quantity=g_fert_quant,absorbing_rate=g_abs_rate):

        self.name = name
        self.quantity = quantity
        self.absorbing_rate = absorbing_rate

    def diffusionAmount(self,water_level):

        d_quantity = self.quantity * self.absorbing_rate

        self.quantity -= d_quantity

        if self.quantity < 0.1:

            self.name = g_empty

        return quantity

Kalium = Fertilizer("Kalium")
Nitrogen = Fertilizer("Nitrogen")
Phosphor = Fertilizer("Phosphor")

g_fert_dict = {"Kalium": Kalium, "Nitrogen": Nitrogen, "Phosphor": Phosphor}
