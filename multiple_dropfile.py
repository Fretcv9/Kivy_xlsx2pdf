from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider

#デバッグ用
from icecream import ic

#merge
import PyPDF2
import xlwings as xw

#日本語表示用
import japanize_kivy

import logout

#log
outputlog = logout.Logger()

class DropFile(Button):
    def __init__(self, **kwargs):
        super(DropFile, self).__init__(**kwargs)

        # get app instance to add function from widget
        app = App.get_running_app() 
        
        # add function to the list
        app.drops.append(self.on_dropfile)

    def on_dropfile(self, widget, filename):
        # a function catching a dropped file
        # if it's dropped in the widget's area
        if self.collide_point(*Window.mouse_pos):
            # on_dropfile's filename is bytes (py3)
            self.text = filename.decode('utf-8')
            ic(filename.decode('utf-8'))
            outputlog.info(filename.decode('utf-8'))
            #read workbook
            book = xw.Book(filename.decode('utf-8'))
    
            #ブック全体
            #save book by pdf
            book.to_pdf(show=False)

            #close excel
            app_excel = xw.apps.active 
            app_excel.quit()


class DropWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(DropWidget, self).__init__(**kwargs)
        print('hellooooooooooooooooo')
        box = BoxLayout()
        #box.orientation = 'vertical' #縦配置
        box.orientation = 'horizontal' #横配置
        dropleft = DropFile(text='EXCELファイルをDRAG&DROPしてください。')
        box.add_widget(dropleft)
        self.add_widget(box)
    
    def actionbutton_closeCliked(self):
        DropApp().stop()

class DropApp(App):
    def __init__(self, **kwargs):
        super(DropApp, self).__init__(**kwargs)
        # set an empty list that will be later populated
        # with functions from widgets themselves
        print('in DropApp before seld.drops = []')
        self.drops = []



    def build(self):
        self.title = 'xlsx2pdf'
        # bind handling function to 'on_dropfile'
        Window.bind(on_dropfile=self.handledrops)
        c = DropWidget()
        return c
        
    def handledrops(self, *args):
        # this will execute each function from list with arguments from
        # Window.on_dropfile
        #
        # make sure `Window.on_dropfile` works on your system first,
        # otherwise the example won't work at all
        for func in self.drops:
            func(*args)

    


if __name__ == '__main__':
    DropApp().run()