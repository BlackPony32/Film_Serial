from PyQt5.QtWidgets import QVBoxLayout, QWidget, QDesktopWidget, QLabel, QApplication, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from MyButton import MyButton
from MyWindowFormat import MyWindowFormat
#from ProgramPack.src.MainWindow import _MainWindow


class _FilmWatcgeOrlaterList(MyWindowFormat):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Списки фільмів")
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

        # Створення кнопок і додавання їх до контейнера
        font = QFont()
        font.setPointSize(16)  # Встановлюємо розмір тексту кнопки

        button1 = MyButton(self)
        button2 = MyButton(self)
        button3 = MyButton(self)

        button1.setText("Назад")
        button1.setFont(font)
        button1.setFixedSize(400, 70)
        button1.start_animation()
        button1.move(300, 400)
        button1.clicked.connect(self.open_main_Window)

        button2.setText("Список переглянутих фільмів")
        button2.setFont(font)
        button2.setFixedSize(400, 70)
        button2.start_animation()
        button2.move(45, 200)
        button2.clicked.connect(self.open_New_WatchedFilm)

        button3.setText("Список фільмів 'Переглянути потім...'")
        button3.setFont(font)
        button3.setFixedSize(450, 70)
        button3.start_animation()
        button3.move(510, 200)
        button3.clicked.connect(self.open_main_Window)

    def open_main_Window(self):
        from ProgramPack.src.MainWindow import _MainWindow
        self.main_Window = _MainWindow()
        self.main_Window.show()
        self.close()

    def open_New_WatchedFilm(self):
        from ProgramPack.src.New_Watched_Film import _new_Watched_Film
        self.watched_film = _new_Watched_Film()
        self.watched_film.show()
        self.close()