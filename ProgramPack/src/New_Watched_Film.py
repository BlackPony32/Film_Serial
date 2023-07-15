import json

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QDesktopWidget, QLabel, QApplication, QHBoxLayout, QLineEdit, \
    QFormLayout, QMessageBox, QCalendarWidget, QPlainTextEdit
from PyQt5.QtGui import QFont, QPixmap
from sqlalchemy.dialects.postgresql import psycopg2
from ProgramPack.src.CustomLabelLine import CustomLabelLineEdit
from MyButton import MyButton
from MyWindowFormat import MyWindowFormat

class _new_Watched_Film(MyWindowFormat):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Новий переглянутий фільм")
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
        #self.setStyleSheet("background-image: url(../img/light_cinema.png);")
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

        button2.setText("Додати фільм")
        button2.setFont(font)
        button2.setFixedSize(450, 70)
        button2.start_animation()
        button2.move(510, 600)
        button2.clicked.connect(self.open_newFilm)


        #______________________________________________________
        label0 = QLabel(self)
        labelAnec = QPlainTextEdit(self)

        label0.setFont(QFont("Arial", 15))
        label0.setStyleSheet("color: blue")
        label0.setText("Невеликий анегдот на тематику фільмів (згенеровано АІ)")
        label0.setFixedSize(800, 30)
        label0.move(10, 15)

        self.generate_random_anecdote()
        random_joke = self.generate_random_anecdote()

        labelAnec.setFont(QFont("Arial", 15))
        labelAnec.setStyleSheet("color: blue")
        labelAnec.setPlainText(random_joke)
        labelAnec.setFixedSize(800, 90)
        labelAnec.move(10, 45)

        line_edit1 = QLineEdit(self)
        label1 = QLabel(self)
        label2 = QLabel(self)
        line_edit3 = QPlainTextEdit(self)
        label3 = QLabel(self)

        label1.setFont(QFont("Arial", 17))
        label1.setStyleSheet("color: blue")
        label1.setText("Назва фільма")
        label1.setFixedSize(250, 30)
        label1.move(45, 150)

        line_edit1.setPlaceholderText("Введіть назву фільма")
        line_edit1.setFont(QFont("Arial", 13))
        line_edit1.setStyleSheet("background-color: #F0F0F0")
        line_edit1.setFixedSize(350, 30)
        line_edit1.move(270, 150)

        label2.setFont(QFont("Arial", 17))
        label2.setStyleSheet("color: blue")
        label2.setText("Оберіть дату додавання фільма")
        label2.setFixedSize(570, 30)
        label2.move(45, 195)
        # ____________________________________________________________________________

        self.labelDate = QLabel(self)
        self.labelDate.setFont(QFont("Arial", 17))
        self.labelDate.setStyleSheet("background-color: transparent")  # Set transparent background
        self.current_date = QDate.currentDate()
        self.labelDate.setFixedSize(200, 50)
        self.labelDate.move(300, 245)

        self.buttonDate = MyButton(self)
        self.buttonDate.setText("Дата додавання")
        self.buttonDate.setFont(font)
        self.buttonDate.setFixedSize(250, 55)
        self.buttonDate.start_animation()
        self.buttonDate.move(45, 245)
        self.buttonDate.clicked.connect(self.buttonDateClicked)
        # ___________________________________________________________________
        label3.setFont(QFont("Arial", 17))
        label3.setStyleSheet("color: blue")
        label3.setText("Короткий опис")
        label3.setFixedSize(250, 30)
        label3.move(45, 305)

        line_edit3.setPlaceholderText("Додайте короткий опис чи замітки по фільму")
        line_edit3.setFont(QFont("Arial", 9))  # 13 норм розмір
        line_edit3.setStyleSheet("background-color: #F0F0F0")
        line_edit3.setFixedSize(350, 100)
        line_edit3.move(270, 305)

        line_edit4 = QPlainTextEdit(self)
        label4 = QLabel(self)

        label4.setFont(QFont("Arial", 17))
        label4.setStyleSheet("color: blue")
        label4.setText("Оберіть жанр фільма")
        label4.setFixedSize(280, 30)
        label4.move(45, 415)

        line_edit4.setPlaceholderText("Запишіть жанр фільма самостійно або оберіть з доступних")
        line_edit4.setFont(QFont("Arial", 9))  # 13 норм розмір
        line_edit4.setStyleSheet("background-color: #F0F0F0")
        line_edit4.setFixedSize(250, 85)
        line_edit4.move(370, 415)

        self.buttonGanre = MyButton(self)
        self.buttonGanre.setText("Доступні жанри")
        self.buttonGanre.setFont(font)
        self.buttonGanre.setFixedSize(250, 55)
        self.buttonGanre.start_animation()
        self.buttonGanre.move(45, 455)
        self.buttonGanre.clicked.connect(self.Genres_open)

        self.line_edit4 = line_edit4
    def open_newSeries(self):
        from ProgramPack.src.Add_new_Film import new_Film
        self.newFilm = new_Film()
        self.newFilm.show()
        self.close()

    def show_calendar(self):
        try:
            self.calendar = QCalendarWidget()
            self.calendar.setWindowModality(Qt.ApplicationModal)
            self.calendar.clicked.connect(self.select_date)

            self.widget = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(self.calendar)
            self.widget.setLayout(layout)
            self.widget.setGeometry(200, 200, 300, 200)
            self.widget.show()
        except Exception as e:
            print("Exception in show_calendar:", e)
            QMessageBox.critical(self, "Error", "An error occurred while opening the calendar.")

    def select_date(self, date):
        try:
            self.current_date = date
            self.update_label()
            self.widget.close()
        except Exception as e:
            print("Exception in select_date:", e)
            QMessageBox.critical(self, "Error", "An error occurred while selecting the date.")

    def update_label(self):
        try:
            self.labelDate.setText(self.current_date.toString("dd.MM.yyyy"))
        except Exception as e:
            print("Exception in update_label:", e)
            QMessageBox.critical(self, "Error", "An error occurred while updating the label.")

    def buttonDateClicked(self):
        if self.buttonDate.isEnabled():
            self.show_calendar()
            self.update_label()

    def generate_random_anecdote(self):
        import json
        import random
        # Відкриття JSON-файлу та завантаження анекдотів
        with open('Filmanecdotes.json', 'r', encoding='utf-8') as file:
            anecdotes = json.load(file)

        # Вибір випадкового анекдота
        random_anecdote = random.choice(anecdotes)

        return random_anecdote['text']

    def open_newFilm(self):
        from ProgramPack.src.Add_new_Film import new_Film
        self.newFilm = new_Film()
        self.newFilm.show()
        self.close()

    def Genres_open(self):
        from test import GenreSelectionApp
        with open("Genres.json", "r", encoding='utf-8') as file:
            genres_data = json.load(file)
            genres = genres_data["genres"]

        self.wind = GenreSelectionApp(genres)
        self.wind.setWindowModality(Qt.ApplicationModal)
        self.wind.show()
