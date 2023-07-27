from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QFont
from ProgramPack.src.MyButton import _MyButton
from ProgramPack.src.MyWindowFormat import MyWindowFormat
#from ProgramPack.my_data.MainWindow import _MainWindow


class _FilmList(MyWindowFormat):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Список фільмів")
        self.setGeometry(0, 0, 1000, 700)

        self.center()
        self.initialize()

    def paintEvent(self, event):
        for button in self.findChildren(_MyButton):  # Отримати всі кнопки MyButton
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
        #font = QFont()
        #font.setPointSize(14)  # Встановлюємо розмір тексту кнопки

        self.button1 = _MyButton(self)
        self.button2 = _MyButton(self)
        self.button3 = _MyButton(self)

        self.button1.setText("Назад")
        self.button1.setFont(QFont("Arial", 14))
        self.button1.setFixedSize(400, 70)
        #self.button1.start_animation()
        self.button1.move(300, 400)
        self.button1.clicked.connect(self.open_main_Window)

        self.button2.setText("Список переглянутих фільмів")
        self.button2.setFont(QFont("Arial", 14))
        self.button2.setFixedSize(400, 70)
        #button2.start_animation()
        self.button2.move(45, 200)
        self.button2.clicked.connect(self.open_New_WatchedFilm)

        self.button3.setText("Список фільмів 'Переглянути потім...'")
        self.button3.setFont(QFont("Arial", 14))
        self.button3.setFixedSize(450, 70)
        #self.button3.start_animation()
        self.button3.move(510, 200)
        self.button3.clicked.connect(self.open_main_Window)

    def open_main_Window(self):
        from ProgramPack.src.MainWindow import _MainWindow
        self.main_Window = _MainWindow()
        self.main_Window.show()
        self.close()

    def open_New_WatchedFilm(self):
        from ProgramPack.Movies_module.New_Watched_Film import _new_Watched_Film
        self.watched_film = _new_Watched_Film()
        self.watched_film.show()
        self.close()