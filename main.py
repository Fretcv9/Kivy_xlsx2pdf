#-*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty,ListProperty
from kivy.uix.floatlayout import FloatLayout


#デバッグ用
from icecream import ic

import pathlib
import glob
import os

#日本語表示用
import japanize_kivy

from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty

#カレントディレクトリ取得
P_current = pathlib.Path()
P_current_abs = P_current.resolve()

print(str(P_current_abs.cwd()))

#ファイルを配列に格納
file_list = glob.glob(str(P_current_abs.cwd())+ str(os.sep) + r'*.txt')
#file_list = glob.glob(os.path.join(str(P_current_abs.cwd()), os.sep + '*.txt'))


print(glob.glob(str(P_current_abs.cwd())+ str(os.sep)+ r'*.txt'))
print(str(len(file_list)))

renketu_list = []

for i in range(len(file_list)):
    p_sub = pathlib.Path(file_list[i])
    p_abs = p_sub.resolve()
    print(str(p_abs.name))
    renketu_list.append(str(p_abs.name))
    #renketu = str(renketu) + str(p_abs.name)¥n

print("連結リストチェック")
print(str(len(renketu_list)))
for i in range(len(renketu_list)):
    renketu_print = renketu_list[i]
    ic(renketu_print)

#"gittest"

#print(renketu)
#renketu = "\n".join(renketu_list)
#print(renketu) 

class PopupMenu(FloatLayout):
    popup_close = ObjectProperty(None)
    load = ObjectProperty(None)

class TextWidget(Widget):
    text  = StringProperty()
    color = ListProperty([1,1,1,1])
    
    def on_command(self, **kwargs):
        content = PopupMenu(load = self.load, popup_close = self.popup_close)
        self._popup = Popup( title="読み込み中", content=content, size_hint=(0.9,0.9))
        self._popup.open()    
    
    def popup_close(self):
        self._popup.dismiss()

    def load(self, path, filename):
        self.ids['button1'].text = str(filename[0])
        self.popup_close()
        with open(os.path.join(path, filename[0])) as file:
            self.ids['button1'].text = str(file.read())
    
    def __init__(self, **kwargs):
        super(TextWidget, self).__init__(**kwargs)
        self.text = "{}".format(renketu_print) 

    def buttonClicked(self):
        self.text = str(P_current_abs.cwd())
        self.color = [1, 0, 0 , 1]

    def buttonClicked2(self):
        self.text = 'Hello'
        self.color = [0, 1, 0 , 1 ]

    def buttonClicked3(self):
        self.text = 'Good evening'
        self.color = [0, 0, 1 , 1 ]

class TestApp(App):
    def build(self):
        self.title = 'テスト'
        return TextWidget()
    #def __init__(self, **kwargs):
    #    super(TestApp, self).__init__(**kwargs)
    #    self.title = 'excel_to_PDF'

if __name__ == '__main__':
    TestApp().run()