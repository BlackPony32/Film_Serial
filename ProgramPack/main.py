import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Pages import Page1, Page2, Page3, MainWindow
from ProgramPack import hello, goodbye
#from ProgramPack import MyWindowFormat
from MyWindowFormat import MyMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()

    #page1 = Page1()
    #page2 = Page2()
    #page3 = Page3()

    #window.add_page(page1)
    #window.add_page(page2)
    #window.add_page(page3)

    window.show()
    sys.exit(app.exec_())
