from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, BoundedNumericProperty, ReferenceListProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock

from plant import *

class FarmPlot(Widget):

    plant = ObjectProperty(Plant(),True)
    water_level = BoundedNumericProperty(50,min=0,errorvalue=0)
    sun_level = BoundedNumericProperty(0, min=0,errorvalue=0)
    phosphor_level = BoundedNumericProperty(100,min=0,max=100,errorvalue=100)
    nitrogen_level = BoundedNumericProperty(100,min=0,max=100,errorvalue=100)
    kalium_level = BoundedNumericProperty(100,min=0,max=100,errorvalue=100)
    bug_level = BoundedNumericProperty(100,min=0,max=100,errorvalue=100)
    contamination_level = BoundedNumericProperty(100,min=0,max=100,errorvalue=100)
  
    def on_touch_down(self,touch):

        if self.collide_point(*touch.pos):
            if self.plant.name == "empty":
                self.plant = carrots
            else:
                self.plant = Plant()

    def update(self,dt):

        self.phosphor_level = self.phosphor_level - dt * self.plant.phosphor_dt
        self.nitrogen_level = self.nitrogen_level - dt * self.plant.nitrogen_dt
        self.kalium_level = self.kalium_level - dt * self.plant.nitrogen_dt

    
class FarmField(Widget):

    plot1 = ObjectProperty(None)
    plot2 = ObjectProperty(None)
    plot3 = ObjectProperty(None)

    plot4 = ObjectProperty(None)
    plot5 = ObjectProperty(None)
    plot6 = ObjectProperty(None)

    plot7 = ObjectProperty(None)
    plot8 = ObjectProperty(None)
    plot9 = ObjectProperty(None)

    plots = ReferenceListProperty(plot1,plot2,plot3,plot4,plot5,plot6, plot7,plot8,plot9)

    def update(self,dt):
    
            for plot in self.plots:

                plot.update(dt)

class FarmGame(Widget):

    farm = ObjectProperty(None)

    def update(self,dt):
        self.farm.update(dt)

class FarmApp(App):
    
    def build(self):
        game = FarmGame()
        Clock.schedule_interval(game.update,1.0)
        return game

if __name__ == "__main__":
    FarmApp().run()





