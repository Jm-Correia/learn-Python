from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty

class Principal(BoxLayout):
    texto_principal = StringProperty('EU sou um label')
    tamanho_texto = NumericProperty(30)
    def teste(self):
        self.texto_principal ='Eu fui Clicado'
        self.tamanho_texto +=20

class Secundario(Widget):
    pass

class Teste(App):
    def build(self):
        return Principal()


Teste().run()
