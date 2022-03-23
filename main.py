from kivy import Config
Config.set('graphics', 'width', '250')
Config.set('graphics', 'height', '350')
Config.set('graphics', 'resizable', False)
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
import os


class DragAndDrop(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = 'ALE Conditioner'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Lime'
        self.theme_cls.primary_hue = "800"
        self.MainScreen = Builder.load_file('main_ui.kv')

    path = StringProperty()

    def build(self):
        Window.bind(on_drop_file=self.on_file_drop)
        return self.MainScreen

    def on_file_drop(self, fdpara, file_path, x, y, *args):
        global file_path_dc
        file_path_dc = file_path.decode('utf-8')
        print(file_path_dc)
        self.MainScreen.ids.dispfile.text = os.path.basename(file_path_dc)



    def reconditioningale(self):
        # read input file
        print(file_path_dc)
        input_ale = open(file_path_dc, "rt")
        # read file contents to string
        data = input_ale.read()
        # replace all occurrences of the required string
        data = data.replace('ä', 'ae')
        data = data.replace('ö', 'oe')
        data = data.replace('ü', 'ue')
        data = data.replace('Ä', 'Ae')
        data = data.replace('Ö', 'Oe')
        data = data.replace('Ü', 'Ue')
        data = data.replace('„', '"')
        data = data.replace('“', '"')
        # close the input file
        input_ale.close()

        # open the input file in write mode
        input_ale = open(file_path_dc, "wt")
        # overrite the input file with the resulting data
        input_ale.write(data)
        # close the file
        input_ale.close()



if __name__ == '__main__':
    DragAndDrop().run()