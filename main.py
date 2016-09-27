from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.image import Image

class FarmPlot(Widget):

    plant = StringProperty("empty")
    water_level = NumericProperty(50)
    sun_level = NumericProperty(0)
    phosphor_level = NumericProperty(100)
    nitrate_level= NumericProperty(100)
    slurry_level = NumericProperty(0)
    bug_level = NumericProperty(0)
  
    def on_touch_down(self,touch):

        if self.collide_point(*touch.pos):
            if self.plant == "empty":
                self.plant = "carrots"
            else:
                self.plant = "empty"
    
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

class FarmGame(Widget):

    farm = ObjectProperty(None)

class FarmApp(App):
    
    def build(self):
        game = FarmGame()
        return game

if __name__ == "__main__":
    FarmApp().run()





