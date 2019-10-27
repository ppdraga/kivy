# import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App

# App().run()
class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User name:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Password:'))
        self.password = TextInput(multiline=False)
        self.add_widget(self.password)

        self.ok_button = Button(text='OK')
        self.ok_button.bind(on_press=self.ok_button_on_press)
        self.add_widget(self.ok_button)

        self.cancel_button = Button(text='Cancel')
        self.cancel_button.bind(on_press=self.cancel_button_on_press)
        self.add_widget(self.cancel_button)
    
    def cancel_button_on_press(self, instance):
        pass

    def ok_button_on_press(self, instance):
        pass

class AppKivy(App): 
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    AppKivy().run()
