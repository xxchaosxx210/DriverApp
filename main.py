__version__ = "0.1"
__author__ = "Paul Millar"
__description__ = "Driver App prototype"


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager


class AppScreenManager(ScreenManager):
    pass


class LoginMDscreen(MDScreen):
    
    username = StringProperty('')
    password = StringProperty('')
    
    def on_login(self):
        print(self.username)
        print(self.password)
        self.manager.current = "main"
    

class MainApp(MDApp):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # tell kivymd what you theme you want for the App
        self.theme_cls.primary_palette = "Blue"
        
def main():
    MainApp().run()

if __name__ == '__main__':
    main()