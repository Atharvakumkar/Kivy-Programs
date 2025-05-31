from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window  # Import Window

class LoginApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # Set background to white (RGBA)

        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.window.add_widget(Image(source="main.png"))

        self.greeting = Label(
            text="Tell us your name!",
            font_size=35,
            color=(0.96, 0.76, 0.76, 1)  # Converted #F4C2C2 to RGBA
        )

        self.window.add_widget(self.greeting)

        self.user = TextInput(
            multiline=False,
            padding_y=(20, 20),
            size_hint=(1, 0.5),
        )

        self.window.add_widget(self.user)

        self.button = Button(
            text="Submit",
            size_hint=(1, 0.5),
            bold=True,
            background_color=(0.96, 0.76, 0.76, 1),  # Converted #F4C2C2 to RGBA
            background_normal=""
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        self.greeting.text = "Hello " + self.user.text + " Good to see you!"

if __name__ == "__main__":
    LoginApp().run()
