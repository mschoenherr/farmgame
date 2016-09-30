from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, BoundedNumericProperty, ReferenceListProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.clock import Clock

from plant import Plant
from model import GameState

class FarmPlot(Widget):

    def __init__(self,ind):

        index = NumericProperty(0)
        index = ind

    def on_touch_down(self,touch):

        if self.collide_point(*touch.pos) and touch.is_double_tap:
            app.root.dispatch('on_plot_touched',self.index)

class FarmField(Widget):

    plots = ObjectProperty(None)

class VeggieScreen(Screen):


    def on_touch_move(self,dt):

        self.parent.transition.direction='up'
        self.parent.current = self.parent.next()

class FarmScreen(Screen):

    farm = ObjectProperty(None,True)

    def on_touch_move(self,dt):

        self.parent.transition.direction='right'
        self.parent.current = self.parent.next()

class FarmGame(ScreenManager):

    def __init__(self):

        self.state = GameState()

        super(FarmGame,self).__init__(transition=SlideTransition())

        self.farm_screen = FarmScreen(name='game')

        for ind, plot in enumerate(self.state.plots):
            # reference plots somewhere and add plots with ind
            pass

        self.veggie_screen = VeggieScreen(name='veggie')

        self.add_widget(self.farm_screen)
        self.add_widget(self.veggie_screen)

        # Calling EventDispatcher constructor
        self.register_event_type('on_plot_touched')

        
    def update(self,dt):
        pass

    def on_plot_touched(self,index):
        pass

class FarmApp(App):
    
    def build(self):
        game = FarmGame()
        Clock.schedule_interval(game.update,1.0)
        return game

if __name__ == "__main__":
    app = FarmApp()
    app.run()





