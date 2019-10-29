# import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
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
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.ok_button = Button(text='OK')
        self.ok_button.bind(on_press=self.ok_button_on_press)
        self.add_widget(self.ok_button)

        self.cancel_button = Button(text='Cancel')
        self.cancel_button.bind(on_press=self.cancel_button_on_press)
        self.add_widget(self.cancel_button)
    
    def cancel_button_on_press(self, instance):
        chat_app.stop()

    def ok_button_on_press(self, instance):
        chat_app.main_page.update_info('message history')
        chat_app.screen_manager.current = 'Messanger'

class ScrollableLabel(ScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = GridLayout(cols=1, size_hint_y=None)
        self.add_widget(self.layout)

        self.chat_history = Label(size_hint_y=None, markup=True)
        self.scroll_to_point = Label()

        self.layout.add_widget(self.chat_history)
        self.layout.add_widget(self.scroll_to_point)

    def update_chat_history(self, message):

        self.chat_history.text += '\n' + message

        self.layout.height = self.chat_history.texture_size[1] + 15
        self.chat_history.height = self.chat_history.texture_size[1]
        self.chat_history.text_size = (self.chat_history.width * 0.98, None)

        self.scroll_to(self.scroll_to_point)

class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 2
        # self.msg = Label(halign='center', valign='middle', text='Main screen')
        # self.msg.bind(width=self.update_text_width)
        # self.add_widget(self.msg)
        self.history = ScrollableLabel(height=Window.size[1]*0.9, size_hint_y=None)
        self.add_widget(self.history)

        self.new_message = TextInput(width=Window.size[0]*0.8, size_hint_x=None, multiline=False)
        self.send = Button(text="Send")
        self.send.bind(on_press=self.send_message)

        bottom_line = GridLayout(cols=2)
        bottom_line.add_widget(self.new_message)
        bottom_line.add_widget(self.send)
        self.add_widget(bottom_line)
    
    def send_message(self, _):
        print("send a message!!!")
        self.history.update_chat_history("send a message!!!")


    def update_info(self, message):
        self.history.update_chat_history(message)

    def update_text_width(self, *_):
        self.msg.text_size = (self.msg.width*0.9, None)

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
    chat_app = MessangerApp()
    chat_app.run()
