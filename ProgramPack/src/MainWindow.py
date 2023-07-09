from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QDesktopWidget, QLabel, QApplication
from PyQt5.QtGui import QFont, QPixmap
from MyButton import MyButton
from MyWindowFormat import MyWindowFormat
from ProgramPack.src.Add_new_Film import new_Film


class _MainWindow(MyWindowFormat):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ваша фільмотека")
        self.setGeometry(0, 0, 1000, 700)

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
        # self.setStyleSheet("background-image: url(../img/popcorn4.png);")
        # Створення контейнера
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(8)
        self.setCentralWidget(central_widget)

        # Створення кнопок і додавання їх до контейнера
        font = QFont()
        font.setPointSize(16)  # Встановлюємо розмір тексту кнопки
        button1 = MyButton()

        button1.setText("Button 1")
        button1.setFont(font)
        button1.setFixedSize(450, 70)
        button1.start_animation()
        button1.clicked.connect(self.open_new_Film)

        button2 = MyButton()
        button2.setText("Button 2")
        button2.setFont(font)
        button2.setFixedSize(450, 70)
        button2.start_animation()
        button3 = MyButton()
        button3.setText("Button 3")
        button3.setFont(font)
        button3.setFixedSize(450, 70)
        button3.start_animation()
        button4 = MyButton()
        button4.setText("Button 4")
        button4.setFont(font)
        button4.setFixedSize(450, 70)
        button5 = MyButton()
        button5.setText("Button 5")
        button5.setFont(font)
        button5.setFixedSize(450, 70)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)

    def open_new_Film(self):
        self.new_film_window = new_Film()
        self.new_film_window.show()
        self.close()
