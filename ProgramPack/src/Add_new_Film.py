import sys
#from MainWindow import MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QDesktopWidget, QLabel, QApplication
from PyQt5.QtGui import QFont, QPixmap
from MyButton import MyButton
from MyWindowFormat import MyWindowFormat

class new_Film(MyWindowFormat):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Моя програма PyQt5")
        self.setGeometry(0, 0, 1000, 700)

        self.setStyleSheet("background-image: url(../img/popcorn4.png);")

        # Створення кнопок і додавання їх до контейнера
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(10)
        self.setCentralWidget(central_widget)

        # Створення кнопок і додавання їх до контейнера
        font = QFont()
        font.setPointSize(16)  # Встановлюємо розмір тексту кнопки

        button1 = MyButton()

        def btn_back_action(self):
            print("Виконано дію для кнопки 'Назад'")
            self.close()
            main = MainWindow()
            main.show()
        button1.setText("Button 1")
        button1.setFont(font)
        button1.setFixedSize(450, 70)
        button1.start_animation()
        button1.clicked.connect(self.openPage2)

        layout.addWidget(button1)


        self.center()
        self.initialize()

    def paintEvent(self, event):
        for button in self.findChildren(MyButton):  # Отримати всі кнопки MyButton
            button.paintEvent(event)  # Викликати метод paintEvent для кожної кнопки

        super().paintEvent(event)  # Викликати метод paintEvent вікна MainWindow

    def center(self):
        frame_geometry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def initialize(self):
        pass