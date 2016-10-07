from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, BoundedNumericProperty, ListProperty, BooleanProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout

from plant import Plant
from model import GameState

class PlantSelection(Widget):

    def on_touch_down(self,touch):

        if self.collide_point(*touch.pos):

            touch.grab(self)

    def on_touch_up(self,touch):

        if self.collide_point(*touch.pos) and touch.grab_current is self:

            touch.ungrab(self)
            app.root.dispatch('on_plant_selection')

class FarmPlot(Widget):

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


class FarmScreen(Screen):

    farm = ObjectProperty(None)
    
class SellItem(GridLayout):

     name = StringProperty("Carrots")

class SellScreen(Screen):
    pass

class FarmGame(ScreenManager):

    swiped = BooleanProperty(False)

    def __init__(self):

        super(FarmGame,self).__init__(transition=SlideTransition())

        self.farm_screen = FarmScreen(name='game')

        self.veggie_screen = SellScreen(name='sell')

        self.add_widget(self.farm_screen)
        self.add_widget(self.veggie_screen)

        self.register_event_type('on_plot_touched')
        self.register_event_type('on_plant_selection')
        
    def update(self,dt):
        pass

    def on_touch_down(self,touch):

        self.swiped = False

        return super(FarmGame,self).on_touch_down(touch)


    def switch_screen(self,direction):

        ind_old = self.screen_names.index(self.current)

        if direction == 'left':
            
            ind_new = (ind_old + 1) % len(self.screen_names)

        elif direction == 'right':

            ind_new = (ind_old + 1) % len(self.screen_names)

        elif direction == 'up':

            ind_new = (ind_old + 1) % len(self.screen_names)

        elif direction == 'down':

            ind_new = (ind_old + 1) % len(self.screen_names)

        else:

            ind_new = ind_old

        self.transition.direction = direction
        self.swiped = True
        self.current = self.screen_names[ind_new]

    def on_touch_move(self,touch):

        if not self.swiped:

            if touch.ox - touch.x > self.width/4:

                self.switch_screen('left')

            elif touch.x - touch.ox > self.width/4:

                self.switch_screen('right')

            elif touch.oy - touch.y > self.width/4:

                self.switch_screen('down')

            elif touch.y - touch.oy > self.width/4:

                self.switch_screen('up')

        return super(FarmGame,self).on_touch_move(touch)
            
    def on_plot_touched(self,index):
       
        # this is completely hackish but works without too much fuss
        # note that objectproperties only propagate their updates if they are assigned a new value
        # have a look at model.py gamestate always returns a copy of itself
        app.game_state = app.game_state.activate_plot(index)
        app.game_state = app.game_state.sell(app.game_state.plant_selection)

    def on_plant_selection(self):
            
        app.game_state.cycle_plant_list()

class FarmApp(App):
    
    game_state = ObjectProperty(GameState(),True)

    def build(self):
        game = FarmGame()
        Clock.schedule_interval(self.update,1.0)
        return game

    def update(self,dt):

        self.game_state = self.game_state.update()

if __name__ == "__main__":
    app = FarmApp()
    app.run()
