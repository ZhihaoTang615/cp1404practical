from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app that dynamically adds labels for a list of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # This is the model (data)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]

    def build(self):
        """Build the Kivy GUI and add dynamic Labels."""
        self.root = Builder.load_file('dynamic_labels.kv')
        self.title = "Dynamic Labels"
        self.create_labels()
        return self.root

    def create_labels(self):
        """Dynamically create a label for each name."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)


DynamicLabelsApp().run()


