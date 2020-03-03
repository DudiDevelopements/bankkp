from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import json

global email_user
global password_user


class File:

    @staticmethod
    def login_file(user_email, user_pas):

        inf_user = {
            'email': user_email,
            'password': user_pas
        }

        users_datas = json.dumps(inf_user)

        loginArchive = open('info_user.json', 'wb')
        loginArchive.write(users_datas.encode())

        loginArchive.close()

        loginArchive = open('info_user.json', 'rb')
        file_datas = loginArchive.readline()

        loginArchive.close()

        print(type(file_datas))
        print(file_datas)


class LoginScreen(FloatLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.user_email = str()
        self.user_password = str()

    def login(self):
        self.user_email = self.ids.user_email.text
        self.user_password = self.ids.user_password.text

        File.login_file(self.user_email, self.user_password)


class BankApp(App):

    def build(self):
        self.title = 'Bank Simulator'
        Window.size = (720, 1280)
        return LoginScreen()


if __name__ == '__main__':
    BankApp().run()
