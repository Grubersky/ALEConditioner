from kivy import Config
Config.set('graphics', 'width', '225')
Config.set('graphics', 'height', '275')
Config.set('graphics', 'resizable', False)
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty



kv = '''
FloatLayout:
    MDRaisedButton:
        text: "Clean Up!"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_press: app.reconditioningale()

    Image:
        size_hint: 0.95, 0.95
        source: "Backdrop.png"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        opacity: 1
'''

file_path_dc = ()

class DragAndDrop(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = 'ALE Conditioner'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Lime'
        self.theme_cls.primary_hue = "800"

    path = StringProperty()

    def build(self):
        Window.bind(on_drop_file=self.on_file_drop)
        return Builder.load_string(kv)

    def on_file_drop(self, fdpara, file_path, x, y, *args):
        file_path_dc = file_path.decode('utf-8')
        print(file_path_dc)



    def reconditioningale(self):
        # read input file
        input_ale = open(file_path_dc_str, "rt")
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
        input_ale = open(file_path_dc_str, "wt")
        # overrite the input file with the resulting data
        input_ale.write(data)
        # close the file
        input_ale.close()



if __name__ == '__main__':
    DragAndDrop().run()


'''
#read input file
input_ale = open("Test1.ale", "rt")
#read file contents to string
data = input_ale.read()
#replace all occurrences of the required string
data = data.replace('ä', 'ae')
data = data.replace('ö', 'oe')
data = data.replace('ü', 'ue')
data = data.replace('Ä', 'Ae')
data = data.replace('Ö', 'Oe')
data = data.replace('Ü', 'Ue')
data = data.replace('„', '"')
data = data.replace('“', '"')
#close the input file
input_ale.close()


#open the input file in write mode
input_ale = open("Test1.ale", "wt")
#overrite the input file with the resulting data
input_ale.write(data)
#close the file
input_ale.close()
'''