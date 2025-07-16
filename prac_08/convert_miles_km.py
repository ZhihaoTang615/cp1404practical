from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """Kivy App to convert miles to kilometres."""
    output_text = StringProperty("")

    def build(self):
        """Build the app and load the kv layout."""
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_input_change(self):
        """Called when the text input changes (live)."""
        miles = self.get_miles()
        km = miles * MILES_TO_KM
        self.output_text = str(km)

    def handle_increment(self, change):
        """Increase or decrease the miles by `change` and recalculate."""
        miles = self.get_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_input_change()

    def get_miles(self):
        """Get the miles value from input, or return 0 on error."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesConverterApp().run()


