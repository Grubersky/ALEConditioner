
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty



kv = '''
'''

class DragAndDrop(MDApp):

    path = StringProperty()

    def build(self):
        Window.bind(on_drop_file=self.on_file_drop)
        return Builder.load_string(kv)

    def on_file_drop(self, fdpara, file_path, x, y, *args):
        self.path = str(file_path)
        print(self.path)

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