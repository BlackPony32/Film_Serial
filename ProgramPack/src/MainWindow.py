from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtGui import QFont, QPixmap
from ProgramPack.src.MyButton import _MyButton
from ProgramPack.src.MyWindowFormat import MyWindowFormat
import Image_resource_rc
class _MainWindow(MyWindowFormat):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ваша фільмотека")
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
        self.setStyleSheet(
            '''
            QMainWindow {
                background-image: url(":/images/popcorn4.png");
            }
            '''
        )
        # Set the background image using a style sheet
        self.setStyleSheet(self.styleSheet())
        # Створення кнопок і додавання їх до контейнера
        font = QFont()
        font.setPointSize(16)  # Встановлюємо розмір тексту кнопки
        button1 = _MyButton(self)

        button1.setText("Додати новий фільм")
        button1.setFont(font)
        button1.setFixedSize(450, 70)
        #button1.start_animation()
        button1.move(20,100)
        button1.clicked.connect(self.add_new_Film)

        button2 = _MyButton(self)
        button2.setText("Додати новий серіал")
        button2.setFont(font)
        button2.setFixedSize(450, 70)
        #button2.start_animation()
        button2.move(20, 200)
        button2.clicked.connect(self.add_new_Series)

        button3 = _MyButton(self)
        button3.setText("Переглянути список фільмів")
        button3.setFont(font)
        button3.setFixedSize(450, 70)
        #button3.start_animation()
        button3.move(20, 300)
        button3.clicked.connect(self.FilmList)

        button4 = _MyButton(self)
        button4.setText("Переглянути список серіалів")
        button4.setFont(font)
        button4.setFixedSize(450, 70)
        button4.move(20, 400)
        button4.clicked.connect(self.SeriesList)

        button5 = _MyButton(self)
        button5.setText("Вихід з програми")
        button5.setFont(font)
        button5.setFixedSize(450, 70)
        button5.move(20, 500)

    def add_new_Film(self):
        from ProgramPack.Movies_module.Add_new_Film import new_Film
        self.new_film_window = new_Film()
        self.new_film_window.show()
        self.close()

    def add_new_Series(self):
        from ProgramPack.Series_module.Add_new_Series import new_Series
        self.new_series_window = new_Series()
        self.new_series_window.show()
        self.close()

    def FilmList(self):
        from ProgramPack.Movies_module.FilmList import _FilmList
        self.list = _FilmList()
        self.list.show()
        self.close()

    def SeriesList(self):
        from ProgramPack.Series_module.SeriesList import _SeriesList
        self.list = _SeriesList()
        self.list.show()
        self.close()