from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QFont
from ProgramPack.src.MyButton import _MyButton
from ProgramPack.src.MyWindowFormat import MyWindowFormat


class new_Film(MyWindowFormat):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Додати новий фільм")
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
        self.setStyleSheet("background-image: url(:/images/popcorn4.png);")

        # Створення кнопок і додавання їх до контейнера
        font = QFont()
        font.setPointSize(16)  # Встановлюємо розмір тексту кнопки

        button1 = _MyButton(self)
        button2 = _MyButton(self)
        button3 = _MyButton(self)

        button1.setText("Назад")
        button1.setFont(font)
        button1.setFixedSize(400, 70)
        #button1.start_animation()
        button1.move(300, 400)
        button1.clicked.connect(self.open_main_Window)

        button2.setText("Новий переглянутий фільм")
        button2.setFont(font)
        button2.setFixedSize(400, 70)
        #button2.start_animation()
        button2.move(45, 200)
        button2.clicked.connect(self.add_New_WatchedFilm)

        button3.setText("'Переглянути потім...'")
        button3.setFont(font)
        button3.setFixedSize(450, 70)
        #button3.start_animation()
        button3.move(510, 200)
        button3.clicked.connect(self.add_Film_later)

    # назад на головне вікно
    def open_main_Window(self):
        from ProgramPack.src.MainWindow import _MainWindow
        self.main_Window = _MainWindow()
        self.main_Window.show()
        self.close()

    # додати новий переглянутий фільм
    def add_New_WatchedFilm(self):
        from ProgramPack.Movies_module.New_Watched_Film import _new_Watched_Film
        self.watched_film = _new_Watched_Film()
        self.watched_film.show()
        self.close()

    # додати фільм переглянути потім
    def add_Film_later(self):
        from ProgramPack.Movies_module.watch_Film_later import _new_Film_later
        self._new_Film_later = _new_Film_later()
        self._new_Film_later.show()
        self.close()