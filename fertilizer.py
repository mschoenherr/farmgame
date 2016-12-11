from constants import g_nil, g_abs_rate, g_fert_quant

class Fertilizer():

    def __init__(self,name=g_nil,quantity=g_fert_quant,absorbing_rate=g_abs_rate):

        self.name = name
        self.quantity = quantity
        self.absorbing_rate = absorbing_rate

    def diffusionAmount(self,water_level):

        d_quantity = self.quantity * min(self.absorbing_rate,1.0)

        self.quantity -= d_quantity

        return d_quantity

Kalium = Fertilizer("Kalium")
Nitrogen = Fertilizer("Nitrogen")
Phosphor = Fertilizer("Phosphor")

g_fert_dict = {"Kalium": Kalium, "Nitrogen": Nitrogen, "Phosphor": Phosphor}
