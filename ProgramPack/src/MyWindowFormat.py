from IPython.external.qt_for_kernel import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
from PyQt5.QtGui import  QIcon


class MyWindowFormat(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Додаткові налаштування вашого власного вікна
        self.setWindowTitle("Моя програма PyQt5")
        self.setGeometry(0, 0, 1000, 700)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.MSWindowsFixedSizeDialogHint)  # Заборона зміни розміру
        # Розміщення вікна посередині екрана
        self.center()

        # Завантажуємо картинку
        icon = QIcon(":/images/MovieIcon.jpg")

        # Встановлюємо картинку як іконку вікна

        width = 32  # Desired width
        height = 32  # Desired height
        resized_icon = icon.pixmap(width, height).scaled(width, height)

        # Set the resized icon as the taskbar icon for the main window
        self.setWindowIcon(QtGui.QIcon(resized_icon))
        # Додаткова ініціалізація вашого власного вікна
        self.initialize()

    def center(self):
        # Отримання розміру екрана
        screen = QDesktopWidget().availableGeometry()
        window_size = self.geometry()

        # Розрахунок положення вікна
        x = (screen.width() - window_size.width()) // 2
        y = (screen.height() - window_size.height()) // 2

        # Встановлення положення вікна
        self.move(x, y)

    def initialize(self):
        pass

    def paintEvent(self, event):
        super().paintEvent(event)  # Викликати метод paintEvent вікна MainWindow



