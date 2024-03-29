from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

#MacBookAirより

#デバッグ用
from icecream import ic

#merge
import PyPDF2
import xlwings as xw

#日本語表示用
import japanize_kivy


class DropFile(Button):
    def __init__(self, **kwargs):
        super(DropFile, self).__init__(**kwargs)

        # get app instance to add function from widget
        app = App.get_running_app() 

        # add function to the list
        app.drops.append(self.on_dropfile)

        ic(app)

    def on_dropfile(self, widget, filename):
        # a function catching a dropped file
        # if it's dropped in the widget's area
        if self.collide_point(*Window.mouse_pos):
            # on_dropfile's filename is bytes (py3)
            self.text = filename.decode('utf-8')
            ic(filename.decode('utf-8'))
            #read workbook
            book = xw.Book(filename.decode('utf-8'))
    
            #ブック全体
            #save book by pdf
            book.to_pdf(show=False)

            #close excel
            app = xw.apps.active 
            app.quit()


class DropApp(App):
    def build(self):
        # set an empty list that will be later populated
        # with functions from widgets themselves
        self.drops = []

        # bind handling function to 'on_dropfile'
        Window.bind(on_dropfile=self.handledrops)

        box = BoxLayout()
        dropleft = DropFile(text='EXCELファイルをDRAG&DROPしてください。')
        box.add_widget(dropleft)
        return box

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