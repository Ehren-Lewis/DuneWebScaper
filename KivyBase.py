from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class baseApp(App):
    def build(self):
        layout1 = GridLayout(cols=2, rows=2)
        layout1.add_widget(Button(text='Hello 1'))
        layout1.add_widget(Button(text='World 1'))
        return layout1

    def build2(self):
        layout2 = GridLayout(cols=2, rows=2)
        layout2.add_widget(Button(text='Hello 2'))
        layout2.add_widget(Button(text='World 2'))
        return layout2


baseApp().run()
