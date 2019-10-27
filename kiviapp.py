import kivy

from kivy.uix.label import Label
from kivy.app import App

# App().run()

class AppKivy(App): 
    def build(self):
        return Label(text='Hello World!')

if __name__ == '__main__':
    AppKivy().run()
