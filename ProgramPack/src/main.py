import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Pages import Page1, Page2, Page3, MainWindow
#from ProgramPack import MyWindowFormat
from MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec_())
