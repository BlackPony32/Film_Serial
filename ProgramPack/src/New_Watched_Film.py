import json
import os

from PyQt5.QtCore import Qt, QDate, QFileSystemWatcher
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
        font.setPointSize(15)  # Встановлюємо розмір тексту кнопки

        button1 = MyButton(self)
        button2 = MyButton(self)

        button1.setText("Назад")
        button1.setFont(font)
        button1.setFixedSize(350, 60)
        button1.start_animation()
        button1.move(45, 600)
        button1.clicked.connect(self.open_newFilm)

        button2.setText("Додати фільм")
        button2.setFont(font)
        button2.setFixedSize(350, 60)
        button2.start_animation()
        button2.move(610, 600)
        button2.clicked.connect(self.open_newFilm)


        #______________________________________________________
        label0 = QLabel(self)
        labelAnec = QPlainTextEdit(self)

        label0.setFont(QFont("Arial", 15))
        label0.setStyleSheet("color: blue")
        label0.setText("Невеликий анегдот на тематику фільмів (згенеровано АІ)")
        label0.setFixedSize(795, 30)
        label0.move(45, 15)

        self.generate_random_anecdote()
        random_joke = self.generate_random_anecdote()

        labelAnec.setFont(QFont("Arial", 15))
        labelAnec.setStyleSheet("color: blue")
        labelAnec.setPlainText(random_joke)
        labelAnec.setFixedSize(930, 70)
        labelAnec.move(45, 45)

        line_edit1 = QLineEdit(self)
        label1 = QLabel(self)
        label2 = QLabel(self)
        line_edit3 = QPlainTextEdit(self)
        label3 = QLabel(self)

        label1.setFont(QFont("Arial", 15))
        label1.setStyleSheet("color: blue")
        label1.setText("Назва фільма")
        label1.setFixedSize(200, 30)
        label1.move(45, 120)

        line_edit1.setPlaceholderText("Введіть назву фільма")
        line_edit1.setFont(QFont("Arial", 13))
        line_edit1.setStyleSheet("background-color: #F0F0F0")
        line_edit1.setFixedSize(685, 30)
        line_edit1.move(290, 120)

        label2.setFont(QFont("Arial", 15))
        label2.setStyleSheet("color: blue")
        label2.setText("Оберіть дату додавання фільма")
        label2.setFixedSize(570, 30)
        label2.move(45, 175)
        # ____________________________________________________________________________

        self.labelDate = QLabel(self)
        self.labelDate.setFont(QFont("Arial", 15))
        self.labelDate.setStyleSheet("background-color: transparent")  # Set transparent background
        self.current_date = QDate.currentDate()
        #self.labelDate.setText(self.current_date.toString("dd.MM.yyyy")) #баг про накладання дат
        self.labelDate.setFixedSize(200, 45)
        self.labelDate.move(300, 205)

        self.buttonDate = MyButton(self)
        self.buttonDate.setText("Дата додавання")
        self.buttonDate.setFont(QFont("Arial", 14))
        self.buttonDate.setFixedSize(250, 45)
        self.buttonDate.start_animation()
        self.buttonDate.move(45, 205)
        self.buttonDate.clicked.connect(self.buttonDateClicked)
        # ___________________________________________________________________
        label3.setFont(QFont("Arial", 15))
        label3.setStyleSheet("color: blue")
        label3.setText("Короткий опис")
        label3.setFixedSize(250, 30)
        label3.move(45, 265)

        line_edit3.setPlaceholderText("Додайте короткий опис чи замітки по фільму")
        line_edit3.setFont(QFont("Arial", 9))  # 13 норм розмір
        line_edit3.setStyleSheet("background-color: #F0F0F0")
        line_edit3.setFixedSize(700, 80)
        line_edit3.move(270, 265)

        label4 = QLabel(self)

        label4.setFont(QFont("Arial", 15))
        label4.setStyleSheet("color: blue")
        label4.setText("Оберіть жанр фільма")
        label4.setFixedSize(280, 30)
        label4.move(45, 345)

        self.line_edit4 = QPlainTextEdit(self)
        self.line_edit4.setPlaceholderText("Запишіть жанр фільма самостійно або оберіть з доступних")
        self.file_name = "data.txt"
        self.file_path = os.path.join(os.getcwd(), self.file_name)

        self.file_watcher = QFileSystemWatcher()
        self.file_watcher.addPath(self.file_path)
        self.file_watcher.fileChanged.connect(self.update_line_edit4)

        self.update_line_edit4()


        self.line_edit4.setFont(QFont("Arial", 9))  # 13 норм розмір
        self.line_edit4.setStyleSheet("background-color: #F0F0F0")
        self.line_edit4.setFixedSize(280, 85)
        self.line_edit4.move(45, 385)

        self.buttonGanre = MyButton(self)
        self.buttonGanre.setText("Доступні жанри")
        self.buttonGanre.setFont(QFont("Arial", 13))
        self.buttonGanre.setFixedSize(280, 55)
        self.buttonGanre.start_animation()
        self.buttonGanre.move(45, 480)
        self.buttonGanre.clicked.connect(self.Genres_open)

        #________________________________________film rating
        label5 = QLabel(self)
        label5.setFont(QFont("Arial", 15))
        label5.setStyleSheet("color: blue")
        label5.setText("Оберіть оцінку фільма")
        label5.setFixedSize(280, 30)
        label5.move(370, 345)

        self.line_edit5 = QPlainTextEdit(self)
        self.line_edit5.setPlaceholderText("Запишіть оцінку фільма самостійно або скористайтесь запропонованою системою")
        self.file_name1 = "movie_rating_result.txt"
        self.file_path1 = os.path.join(os.getcwd(), self.file_name1)

        self.file_watcher1 = QFileSystemWatcher()
        self.file_watcher1.addPath(self.file_path1)
        self.file_watcher1.fileChanged.connect(self.update_line_edit5)

        self.line_edit5.setFont(QFont("Arial", 9))  # 13 норм розмір
        self.line_edit5.setStyleSheet("background-color: #F0F0F0")
        self.line_edit5.setFixedSize(280, 85)
        self.line_edit5.move(370, 385)

        self.buttonRating = MyButton(self)
        self.buttonRating.setText("Доступна система оцінювання")
        self.buttonRating.setFont(QFont("Arial", 9))
        self.buttonRating.setFixedSize(280, 55)
        self.buttonRating.start_animation()
        self.buttonRating.move(370, 480)
        self.buttonRating.clicked.connect(self.Rating_open)

        self.update_line_edit5()
        #_______________________________________________ age rating
        label6 = QLabel(self)
        label6.setFont(QFont("Arial", 15))
        label6.setStyleSheet("color: blue")
        label6.setText("Віковий рейтинг фільма")
        label6.setFixedSize(280, 30)
        label6.move(690, 345)

        self.line_edit6 = QPlainTextEdit(self)
        self.line_edit6.setPlaceholderText(
            "Введіть доповнення до вікового рейтингу або оберіть доступну")
        self.file_name2 = "movie_age_rating.txt"
        self.file_path2 = os.path.join(os.getcwd(), self.file_name2)

        self.file_watcher2 = QFileSystemWatcher()
        self.file_watcher2.addPath(self.file_path2)
        self.file_watcher2.fileChanged.connect(self.update_line_edit6)

        self.line_edit6.setFont(QFont("Arial", 9))  # 13 норм розмір
        self.line_edit6.setStyleSheet("background-color: #F0F0F0")
        self.line_edit6.setFixedSize(280, 85)
        self.line_edit6.move(690, 385)

        self.buttonAge = MyButton(self)
        self.buttonAge.setText("Доступна система рейтингу")
        self.buttonAge.setFont(QFont("Arial", 9))
        self.buttonAge.setFixedSize(280, 55)
        self.buttonAge.start_animation()
        self.buttonAge.move(690, 480)
        self.buttonAge.clicked.connect(self.Age_Rating_open)

        self.update_line_edit6()


    def open_newSeries(self):                               # ШО ЦЕЙ КОД РОБИТЬ?
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
        #self.labelDate.setText("")
        try:
            self.labelDate.setText(self.current_date.toString("dd.MM.yyyy"))
        except Exception as e:
            print("Exception in update_label:", e)
            QMessageBox.critical(self, "Error", "An error occurred while updating the label.")

    def buttonDateClicked(self):
        self.labelDate.setText("")
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
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                file.write('')
        except Exception as e:
            print("Exception in clear_file:", e)
            QMessageBox.critical(self, 'Помилка', f'Виникла помилка при очищенні файлу:\n{str(e)}')
        try:
            with open(self.file_path1, 'w', encoding='utf-8') as file:
                file.write('')
        except Exception as e:
            print("Exception in clear_file:", e)
            QMessageBox.critical(self, 'Помилка', f'Виникла помилка при очищенні файлу:\n{str(e)}')
        try:
            with open(self.file_path2, 'w', encoding='utf-8') as file:
                file.write('')
        except Exception as e:
            print("Exception in clear_file:", e)
            QMessageBox.critical(self, 'Помилка', f'Виникла помилка при очищенні файлу:\n{str(e)}')

        self.newFilm = new_Film()
        self.newFilm.show()
        self.close()

    def Genres_open(self):
        from GenresWindow import GenreSelectionApp
        with open("Genres.json", "r", encoding='utf-8') as file:
            genres_data = json.load(file)
            genres = genres_data["genres"]

        self.wind = GenreSelectionApp(genres)
        self.wind.setWindowModality(Qt.ApplicationModal)
        self.wind.show()

    def update_line_edit4(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                self.line_edit4.setPlainText(text)
        except FileNotFoundError:
            self.line_edit4.setPlainText("Файл не знайдено")
        except Exception as e:
            print("Exception in update_line_edit4:", e)
            QMessageBox.critical(self, 'Помилка', f'Виникла помилка при оновленні вмісту:\n{str(e)}')

    def update_line_edit5(self):
        try:
            with open(self.file_path1, 'r', encoding='utf-8') as file:
                text = file.read()
                self.line_edit5.setPlainText(text)
        except FileNotFoundError:
            self.line_edit5.setPlainText("Файл не знайдено")
        except Exception as e:
            print("Exception in update_line_edit4:", e)
            QMessageBox.critical(self, 'Помилка', f'Виникла помилка при оновленні вмісту:\n{str(e)}')

    def update_line_edit6(self):
        try:
            with open(self.file_path2   , 'r', encoding='utf-8') as file:
                text = file.read()
                self.line_edit6.setPlainText(text)
        except FileNotFoundError:
            self.line_edit6.setPlainText("Файл не знайдено")
        except Exception as e:
            print("Exception in update_line_edit4:", e)
            QMessageBox.critical(self, 'Помилка', f'Виникла помилка при оновленні вмісту:\n{str(e)}')
    def Rating_open(self):
        from series_movie_rating import MovieRatingApp

        self.wind = MovieRatingApp()
        self.wind.setWindowModality(Qt.ApplicationModal)
        self.wind.show()

    def Age_Rating_open(self):
        from Age_rating import Age_MovieRatingApp

        self.wind = Age_MovieRatingApp()
        self.wind.setWindowModality(Qt.ApplicationModal)
        self.wind.show()