# import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
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

class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 1
        self.msg = Label(text='Main screen')
        self.msg.bind(width=self.update_test_width)
        self.add_widget(self.msg)

class MessangerApp(App): 
    def build(self):
        self.screen_manager = ScreenManager()

        self.login_page = LoginScreen()
        screen = Screen(name='Login')
        screen.add_widget(self.login_page)
        self.screen_manager.add_widget(screen)

        self.main_page = MainScreen()
        screen = Screen(name='Messanger')
        screen.add_widget(self.main_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == '__main__':
    MessangerApp().run()
