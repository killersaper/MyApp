from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class Box(BoxLayout):

    def enter_text(self):
        print(self.ids["textid"].text)

    def click(self, instance):
        self.ids["buttonid"].text = self.ids["textid"].text
        print(self.ids["buttonid"].text)

class MainApp(App):

    def build(self):
        box1 = Box()
        print(box1.ids["buttonid"].text)
        return box1

if __name__ == '__main__':
    MainApp().run()
