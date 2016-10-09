from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, BoundedNumericProperty, ListProperty, BooleanProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup

from model import GameState
from constants import g_empty,g_dt

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

class WeatherDisplay(GridLayout):
    pass

class FarmScreen(Screen):

    farm = ObjectProperty(None)
    
class SellItem(GridLayout):

    name = StringProperty("Carrots")
    
    def on_touch_down(self,touch):

        if self.collide_point(*touch.pos):

            touch.grab(self)

    def on_touch_up(self,touch):

        if self.collide_point(*touch.pos) and touch.grab_current is self:
            touch.ungrab(self)
            app.root.dispatch('on_plant_sell',self.name)

class SellScreen(Screen):
    pass

class HelpButton(Button):

    def on_release(self):

        layout = GridLayout(cols=1, spacing = 10,size_hint_y = None)
        layout.bind(minimum_height=layout.setter('height'))

        fob = open("help.txt")
        
        for line in fob.readlines():
            label = Label(text=line)
            layout.add_widget(label)

        fob.close()

        content = ScrollView(size_hint=(1,0.9),pos_hint={'top':0.9})

        content.add_widget(layout)

        popup = Popup(title="Help",content=content,size_hint=(0.6,0.6)).open()

class ResetButton(Button):

    def on_release(self):

        if self.last_touch and self.last_touch.is_triple_tap:
            app.game_state = GameState()

class TitleScreen(Screen):
    pass

class AchievementScreen(Screen):
    pass

class UpgradeScreen(Screen):
    pass

class FarmGame(ScreenManager):

    swiped = BooleanProperty(False)

    def __init__(self):

        super(FarmGame,self).__init__(transition=SlideTransition())

        self.farm_screen = FarmScreen(name='game')

        self.sell_screen = SellScreen(name='sell')
        self.title_screen = TitleScreen(name='title')
        self.achievement_screen = AchievementScreen(name='achievement')
        self.upgrade_screen = UpgradeScreen(name='upgrade')

        self.add_widget(self.title_screen)
        self.add_widget(self.upgrade_screen)
        self.add_widget(self.farm_screen)
        self.add_widget(self.sell_screen)
        self.add_widget(self.achievement_screen)

        print self.screen_names

        self.register_event_type('on_plot_touched')
        self.register_event_type('on_plant_selection')
        self.register_event_type('on_plant_sell')
        
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

            ind_new = (ind_old + 4) % len(self.screen_names)

        elif direction == 'up':

            ind_new = (ind_old + 2) % len(self.screen_names)

        elif direction == 'down':

            ind_new = (ind_old + 3) % len(self.screen_names)

        else:

            ind_new = ind_old

        self.transition.direction = direction
        self.swiped = True
        
        if self.current == 'title':
            app.update_event()

        new_screen_name = self.screen_names[ind_new]

        if new_screen_name == 'title':

            app.update_event.cancel()

        self.current = new_screen_name

    def on_touch_move(self,touch):

        if not self.swiped:

            if touch.ox - touch.x > self.width/4:

                self.switch_screen('left')
                return True

            elif touch.x - touch.ox > self.width/4:

                self.switch_screen('right')
                return True

            elif touch.oy - touch.y > self.width/4:

                self.switch_screen('down')
                return True

            elif touch.y - touch.oy > self.width/4:

                self.switch_screen('up')
                return True

    def on_plot_touched(self,index):
       
        # this is completely hackish but works without too much fuss
        # note that objectproperties only propagate their updates if they are assigned a new value
        # have a look at model.py gamestate always returns a copy of itself
        app.game_state = app.game_state.activate_plot(index)

    def on_plant_selection(self):
            
        app.game_state = app.game_state.cycle_plant_list()

    def on_plant_sell(self,name):

        app.game_state = app.game_state.sell(name)

class FarmApp(App):
    
    game_state = ObjectProperty(GameState(),True)

    def build(self):
        game = FarmGame()
        self.update_event = Clock.schedule_interval(self.update,g_dt)
        self.update_event.cancel()
        return game

    def update(self,dt):

        self.game_state = self.game_state.update()

if __name__ == "__main__":
    app = FarmApp()
    app.run()
