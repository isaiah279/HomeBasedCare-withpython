from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (450, 500)
from kivymd.uix.snackbar import Snackbar

class Tutorials(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.config.primary_color = "Green"
        login_page = Builder.load_file('adminsigin.kv')

        return login_page

    def verify(self, email, password):
        if email != "admin":
            err = Snackbar(text="Enter correct Detail", md_bg_color=[0, 0.3, 0, 1])
            err.open()
        else:
            if password != "1234":
                err = Snackbar(text="Enter correct Detail", md_bg_color=[0, 0.3, 0, 1])
                err.open()
            else:
                err = Snackbar(text="Success")
                err.open()


if __name__ == "__main__":
    Tutorials().run()
