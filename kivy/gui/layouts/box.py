from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout

class Principal(BoxLayout):
    pass

class Secundario(FloatLayout):
    pass

class Grid(GridLayout):
    pass

class Stack(StackLayout):
    pass

class Box(App):
    def build(self):
        return Stack()


Box().run()
