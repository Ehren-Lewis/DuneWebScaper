from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from main import search_with_selenium
"""
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

# Buttons for each different kind of graph

 # Seperate page for each film.
"""


class PageLayout(PageLayout):
    def __init__(self):

        super(PageLayout, self).__init__()

        btn1 = Button(text='Button 1')
        btn2 = Button(text='Button 2')
        btn3 = Button(text='Button 3')

        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)


class PageLayoutApp(App):

    def build(self):

        return PageLayout()

PageLayoutApp().run()