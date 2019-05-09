from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KILOMETERS = 1.60934


class MilesConverterApp(App):
    def build(self):
        Window.size = (650, 180)
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_m_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * MILES_TO_KILOMETERS
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """Error checks the program"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()
