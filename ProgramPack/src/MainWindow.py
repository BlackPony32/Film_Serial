from PyQt5.QtWidgets import QDesktopWidget, QLabel, QApplication
from PyQt5.QtGui import QFont, QPixmap
from MyButton import MyButton
from MyWindowFormat import MyWindowFormat


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
        self.setStyleSheet("background-image: url(../img/popcorn4.png);")

        # Створення кнопок і додавання їх до контейнера
        font = QFont()
        font.setPointSize(16)  # Встановлюємо розмір тексту кнопки
        button1 = MyButton(self)

        button1.setText("Додати новий фільм")
        button1.setFont(font)
        button1.setFixedSize(450, 70)
        button1.start_animation()
        button1.move(20,100)
        button1.clicked.connect(self.add_new_Film)

        button2 = MyButton(self)
        button2.setText("Додати новий серіал")
        button2.setFont(font)
        button2.setFixedSize(450, 70)
        button2.start_animation()
        button2.move(20, 200)
        button2.clicked.connect(self.add_new_Series)

        button3 = MyButton(self)
        button3.setText("Button 3")
        button3.setFont(font)
        button3.setFixedSize(450, 70)
        button3.start_animation()
        button3.move(20, 300)

        button4 = MyButton(self)
        button4.setText("Button 4")
        button4.setFont(font)
        button4.setFixedSize(450, 70)
        button4.move(20, 400)

        button5 = MyButton(self)
        button5.setText("Button 5")
        button5.setFont(font)
        button5.setFixedSize(450, 70)
        button5.move(20, 500)

    def add_new_Film(self):
        from ProgramPack.src.Add_new_Film import new_Film
        self.new_film_window = new_Film()
        self.new_film_window.show()
        self.close()

    def add_new_Series(self):
        from ProgramPack.src.Add_new_Series import new_Series
        self.new_series_window = new_Series()
        self.new_series_window.show()
        self.close()