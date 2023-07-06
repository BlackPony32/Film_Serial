from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QDesktopWidget
from PyQt5.QtGui import QFont
from MyButton import MyButton

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Додаткові налаштування вашого власного вікна
        self.setWindowTitle("Моя програма PyQt5")
        self.setGeometry(0, 0, 1000, 700)

        # Створення кнопок і додавання їх до контейнера
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(10)
        self.setCentralWidget(central_widget)

        # Створення кнопок і додавання їх до контейнера
        font = QFont()
        font.setPointSize(16)  # Встановлюємо розмір тексту кнопки
        button1 = MyButton("Button 1")
        button1.setFont(font)
        button1.setFixedSize(450, 70)
        button2 = MyButton("Button 2")
        button2.setFixedSize(450, 70)
        button2.setFont(font)
        button3 = MyButton("Button 3")
        button3.setFont(font)
        button3.setFixedSize(450, 70)
        button4 = MyButton("Button 4")
        button4.setFont(font)
        button4.setFixedSize(450, 70)
        button5 = MyButton("Button 5")
        button5.setFont(font)
        button5.setFixedSize(450, 70)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)
        # Розміщення вікна посередині екрана
        self.center()

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
        # Додайте ваші власні елементи інтерфейсу користувача та функціональність тут
        pass
