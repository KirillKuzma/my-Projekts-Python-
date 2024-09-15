from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
#:import get_color_from_hex kivy.utils.get_color_from_hex

Screen:
    MDCard:

    MDLabel:
        value: 000
        text: str(self.value)
        font_size:200
        halign: "center"
        on_touch_down: self.value+=1

        canvas.before:
            Color:
                rgba: get_color_from_hex("#4eaabe")
            Ellipse:
                pos: self.center[0] - dp(100), self.center[1] - dp(100)
                size: dp(200), dp(200)
"""

class HelloWorld(MDApp):
    def build(self):
        return Builder.load_string(KV)

HelloWorld().run()