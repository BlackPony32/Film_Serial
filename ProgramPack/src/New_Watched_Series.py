from PyQt5.QtWidgets import QVBoxLayout, QWidget, QDesktopWidget, QLabel, QApplication, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from MyButton import MyButton
from MyWindowFormat import MyWindowFormat



class _new_Watched_Series(MyWindowFormat):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Новий переглянутий серіал")
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
        self.setStyleSheet("background-image: url(../img/light_cinema.png);")
        font = QFont()
        font.setPointSize(16)  # Встановлюємо розмір тексту кнопки

        button1 = MyButton(self)
        button2= MyButton(self)

        button1.setText("Назад")
        button1.setFont(font)
        button1.setFixedSize(450, 70)
        button1.start_animation()
        button1.move(45, 600)
        button1.clicked.connect(self.open_newFilm)

        button2.setText("Додати серіал")
        button2.setFont(font)
        button2.setFixedSize(450, 70)
        button2.start_animation()
        button2.move(510, 600)
        button2.clicked.connect(self.open_newFilm)

    def open_newFilm(self):
        from ProgramPack.src.Add_new_Series import new_Series
        self.newSeries = new_Series()
        self.newSeries.show()
        self.close()