__version__ = "0.1"
__author__ = "Paul Millar"
__description__ = "Driver App prototype"


from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivy.logger import Logger
from kivy.clock import mainthread
import requests
from threading import Thread
import json

import pauls_taxi_api as taxiapi

class LoginMDscreen(MDScreen):
    
    
    def on_login_button(self):
        username = self.ids["id_username"].text
        password = self.ids["id_password"].text
        th = Thread(target=self.login, kwargs={"username": username, "password": password})
        th.start()
    
    def login(self, username, password):
        data = {"username": username, "password": password, "imei_number": "78278728787"}
        resp = requests.post(taxiapi.DRIVER_LOGIN_URL, data=data, timeout=20)
        if resp.text:
            robj = json.loads(resp.text)
            try:
                driver = robj["response"]["driver"]
                status = driver["status"]
                if status == "passed":
                    taxiapi.save_settings({"token": driver["token"]})
                    self.on_login_success()
                else:
                    self.on_login_error(robj["response"]["driver"]["message"])
            except KeyError as err:
                self.on_login_error(err.__str__())
    
    @mainthread
    def on_login_success(self):
        self.manager.current = "main"
      
    @mainthread  
    def on_login_error(self, message):
        toast(message)
    

class MainApp(MDApp):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # tell kivymd what you theme you want for the App
        self.theme_cls.primary_palette = "Blue"
        
def main():
    MainApp().run()

if __name__ == '__main__':
    main()