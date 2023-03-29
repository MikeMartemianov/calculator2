import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button


class CalculatorApp(App):
    def build(self):
        self.title = 'калькулятор'
        self.icon = 'Wineass-Ios7-Redesign-Calculator.512.png'
        box_layout = BoxLayout(orientation="vertical")

        self.text_input = TextInput()
        box_layout.add_widget(self.text_input)

        self.execute_button = Button(text="Execute", on_press=self.execute_code)
        box_layout.add_widget(self.execute_button)

        self.result_label = Label()
        box_layout.add_widget(self.result_label)

        return box_layout

    def execute_code(self, instance):
        t = self.text_input.text
        try:
            self.result_label.text = str(eval(t))
        except Exception as e:
            self.result_label.text = str(e)


if __name__ == "__main__":
    CalculatorApp().run()
