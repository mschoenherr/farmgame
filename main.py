from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, BoundedNumericProperty, ReferenceListProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
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

        if self.collide_point(*touch.pos) and touch.is_double_tap:
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

class VeggieScreen(Screen):


    def on_touch_move(self,dt):

        self.parent.transition.direction='up'
        self.parent.current = self.parent.next()

class FarmScreen(Screen):

    farm = ObjectProperty(None)

    def update(self,dt):
        self.farm.update(dt)

    def on_touch_move(self,dt):

        self.parent.transition.direction='right'
        self.parent.current = self.parent.next()

class FarmGame(ScreenManager):

    def __init__(self):

        super(FarmGame,self).__init__(transition=SlideTransition())

        self.farm_screen = FarmScreen(name='game')
        self.veggie_screen = VeggieScreen(name='veggie')

        self.add_widget(self.farm_screen)
        self.add_widget(self.veggie_screen)
        
    def update(self,dt):
        pass

class FarmApp(App):
    
    def build(self):
        game = FarmGame()
        Clock.schedule_interval(game.update,1.0)
        return game

if __name__ == "__main__":
    FarmApp().run()




