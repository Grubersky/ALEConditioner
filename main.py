from kivy import Config
Config.set('graphics', 'width', '250')
Config.set('graphics', 'height', '375')
Config.set('graphics', 'resizable', False)
Config.set('kivy', 'window_icon', 'ale_icon.png')
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
import os
import unicodedata

file_path_dc = ('')

class DragAndDrop(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = 'ALE Conditioner'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Lime'
        self.theme_cls.primary_hue = "800"
        self.MainScreen = Builder.load_file('main_ui.kv')
        Window.borderless = False

    path = StringProperty()

    def build(self):
        Window.bind(on_drop_file=self.on_file_drop)
        return self.MainScreen

    def on_file_drop(self, fdpara, file_path, x, y, *args):
        global file_path_dc
        file_path_dc = file_path.decode('utf-8')
        print(file_path_dc)
        alename = os.path.basename(file_path_dc)
        print(alename)
        if alename.endswith(('.ale', '.ALE')):
            alename_trunc = "{}.ale".format(alename[:13]) if len(alename) > 15 else alename
            print(alename_trunc)
            self.MainScreen.ids.dispfile.text = alename_trunc
        else:
            print('File not Supported')
            self.dialog = MDDialog(text="Hmm.. that doesn't seem to be an ALE.", radius=[10, 10, 10, 10], )
            self.dialog.open()

    def reconditioningale(self):
        if file_path_dc == (''):
            print('No file selected')
            self.dialog = MDDialog(text="Oops! Gotta Drop an ALE first!", radius=[10, 10, 10, 10],)
            self.dialog.open()

        else:
            print('read input file')
            print(file_path_dc)
            input_ale = open(file_path_dc, "rt", encoding='utf-8')
            print('read file contents to string')
            data = input_ale.read()
            print('replace all occurrences of the required string')
            data = data.replace('ä', 'ae')
            data = data.replace('ö', 'oe')
            data = data.replace('ü', 'ue')
            data = data.replace('Ä', 'Ae')
            data = data.replace('Ö', 'Oe')
            data = data.replace('Ü', 'Ue')
            data = data.replace('ß', 'ss')
            data = unicodedata.normalize('NFKD', data).encode('ascii', 'ignore').decode()
            print('close the input file')
            input_ale.close()

            print('open the input file in write mode')
            input_ale = open(file_path_dc, "wt", encoding='utf-8')
            print('overrite the input file with the resulting data')
            input_ale.write(data)
            print('close the file')
            input_ale.close()

            self.dialog = MDDialog(
                text="DONE!", radius=[10, 10, 10, 10],)
            self.dialog.open()

if __name__ == '__main__':
    DragAndDrop().run()