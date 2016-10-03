from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, BoundedNumericProperty, ListProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout

from plant import Plant
from model import GameState

class FarmPlot(Image):

    index = NumericProperty(0)

    def on_touch_down(self,touch):
    
        if self.collide_point(*touch.pos):
            app.root.dispatch('on_plot_touched',self.index)

    def on_touch_up(self,touch):

        if self.collide_point(*touch.pos):
            app.root.dispatch('on_plot_released',self.index)

class FarmField(GridLayout):
    pass

class VeggieScreen(Screen):


    def on_touch_move(self,dt):

        self.parent.transition.direction='up'
        self.parent.current = self.parent.next()

class FarmScreen(Screen):

    farm = ObjectProperty(None)

    def on_touch_move(self,dt):

        self.parent.transition.direction='right'
        self.parent.current = self.parent.next()

class FarmGame(ScreenManager):

    def __init__(self):

        self.state = ObjectProperty(GameState(),True)
        self.last_plot_touched = NumericProperty(-1)

        super(FarmGame,self).__init__(transition=SlideTransition())

        self.farm_screen = FarmScreen(name='game')

        self.veggie_screen = VeggieScreen(name='veggie')

        self.add_widget(self.farm_screen)
        self.add_widget(self.veggie_screen)

        self.register_event_type('on_plot_touched')
        self.register_event_type('on_plot_released')

        
    def update(self,dt):
        pass

    def on_touch_move(self,touch):

        if abs(touch.ox - touch.x) > 96:
            print "swipe"
            return True
        else:
            return False

    def on_plot_touched(self,index):
        print "plot touched: " + str(index)

    def on_plot_released(self,index):

        if self.last_plot_touched == index:
            print "plot touched: " + str(index)
        else:
            self.last_plot_touched = index

class FarmApp(App):
    
    def build(self):
        game = FarmGame()
        Clock.schedule_interval(game.update,1.0)
        return game

if __name__ == "__main__":
    app = FarmApp()
    app.run()
