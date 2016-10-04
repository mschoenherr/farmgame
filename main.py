from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, BoundedNumericProperty, ListProperty, BooleanProperty
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

            touch.grab(self)

    def on_touch_up(self,touch):

        if self.collide_point(*touch.pos) and touch.grab_current is self:
            touch.ungrab(self)
            app.root.dispatch('on_plot_touched',self.index)

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

    swiped = BooleanProperty(False)

    def __init__(self):

        super(FarmGame,self).__init__(transition=SlideTransition())

        self.farm_screen = FarmScreen(name='game')

        self.veggie_screen = VeggieScreen(name='veggie')

        self.add_widget(self.farm_screen)
        self.add_widget(self.veggie_screen)

        self.register_event_type('on_plot_touched')
        
    def update(self,dt):
        pass

    def on_touch_move(self,touch):

        if touch.ox - touch.x > self.width/4:
            print "swipe left"
            return True
        elif touch.x - touch.ox > self.width/4:
            print "swipe right"
            return True
        elif touch.oy - touch.y > self.width/4:
            print "swipe down"
            return True
        elif touch.y - touch.oy > self.width/4:
            print "swipe up"
            return True

    def on_plot_touched(self,index):
       
        # this is completely hackish but works without too much fuss
        # note that objectproperties only propagate their updates if they are assigned a new value
        # have a look at model.py gamestate always returns a copy of itself
        app.game_state = app.game_state.plot_touched(index)

class FarmApp(App):
    
    game_state = ObjectProperty(GameState(),True)

    def build(self):
        game = FarmGame()
        Clock.schedule_interval(game.update,1.0)
        return game

if __name__ == "__main__":
    app = FarmApp()
    app.run()
