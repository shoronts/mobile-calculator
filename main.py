from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window


# Set App Size
Window.size = (400,500)

# Load Design
Builder.load_file('calculator_design.kv')


class Calculator(Widget):

    def calc_clear(self):
        self.ids.calc_input.text = '0'

    def press_button(self, value):
        privious = self.ids.calc_input.text

        if privious == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f"{value}"
        elif len(privious) < 500:
            self.ids.calc_input.text = f"{privious}{value}"

    def add_value(self):
        privious = self.ids.calc_input.text
        if privious[-1] != '+':
            self.ids.calc_input.text = f'{privious}+'
        else:
            pass

    def subtract_value(self):
        privious = self.ids.calc_input.text
        if privious[-1] != '-':
            self.ids.calc_input.text = f'{privious}-'
        else:
            pass

    def divide_value(self):
        privious = self.ids.calc_input.text
        if privious[-1] != '/':
            self.ids.calc_input.text = f'{privious}/'
        else:
            pass
    
    def multiply_value(self):
        privious = self.ids.calc_input.text
        if privious[-1] != '*':
            self.ids.calc_input.text = f'{privious}*'
        else:
            pass

    def equals_value(self):
        privious = self.ids.calc_input.text



class CalculatorApp(App):
    def build(self):
        self.title = 'Simple Calculator'
        return Calculator()


if __name__ == '__main__':
    CalculatorApp().run()
