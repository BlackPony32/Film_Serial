import json
import os

from PyQt5.QtCore import Qt, QDate, QFileSystemWatcher, QFile, QTextStream
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QDesktopWidget, QLabel, QLineEdit, \
    QMessageBox, QCalendarWidget, QPlainTextEdit
from PyQt5.QtGui import QFont
from ProgramPack.src.MyButton import _MyButton
from ProgramPack.src.MyWindowFormat import MyWindowFormat
import Image_resource_rc
class _new_Watched_Film(MyWindowFormat):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Новий переглянутий фільм")
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
        background_image = ":/images/light_cinema4.png"
        # Set the background image using a style sheet
        #self.setStyleSheet(f"background-image: url({background_image});")
        font = QFont()
        font.setPointSize(15)  # Встановлюємо розмір тексту кнопки

        #_____________Основні кнопки для переходу по сторінках і збереження даних в базу___________
        button1 = _MyButton(self)
        button2 = _MyButton(self)

        button1.setText("Назад")
        button1.setFont(font)
        button1.setFixedSize(350, 60)
        #button1.start_animation()
        button1.move(45, 600)
        button1.clicked.connect(self.open_newFilm)

        button2.setText("Додати фільм")
        button2.setFont(font)
        button2.setFixedSize(350, 60)
        #button2.start_animation()
        button2.move(620, 600)
        button2.clicked.connect(self.open_newFilm)

        #___________________Лейбл про анегдот та поле для виводу випадкового анегдоту______________________________
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

        #______________Назва фільма і поле для вводу назви_________________
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

        # ___________________Блок дати додавання дати_____________________________________________
        label2.setFont(QFont("Arial", 15))
        label2.setStyleSheet("color: blue")
        label2.setText("Оберіть дату додавання фільма")
        label2.setFixedSize(570, 30)
        label2.move(45, 175)

        self.labelDate = QLabel(self)
        self.labelDate.setFont(QFont("Arial", 15))
        self.labelDate.setStyleSheet("background-color: transparent")  # Set transparent background
        self.current_date = QDate.currentDate()
        #self.labelDate.setText(self.current_date.toString("dd.MM.yyyy")) #баг про накладання дат
        self.labelDate.setFixedSize(200, 45)
        self.labelDate.move(300, 205)

        self.buttonDate = _MyButton(self)
        self.buttonDate.setText("Дата додавання")
        self.buttonDate.setFont(QFont("Arial", 14))
        self.buttonDate.setFixedSize(250, 45)
        #self.buttonDate.start_animation()
        self.buttonDate.move(45, 205)
        self.buttonDate.clicked.connect(self.buttonDateClicked)
        # _______________________Блок опису фільма____________________________________________
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

        #_________________Блок опису жанру фільма______________________
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

        #_______________________________Блок жанрів фільма________________________________
        self.line_edit4.setFont(QFont("Arial", 9))  # 13 норм розмір
        self.line_edit4.setStyleSheet("background-color: #F0F0F0")
        self.line_edit4.setFixedSize(280, 85)
        self.line_edit4.move(45, 385)

        self.buttonGanre = _MyButton(self)
        self.buttonGanre.setText("Доступні жанри")
        self.buttonGanre.setFont(QFont("Arial", 13))
        self.buttonGanre.setFixedSize(280, 55)
        #self.buttonGanre.start_animation()
        self.buttonGanre.move(45, 480)
        self.buttonGanre.clicked.connect(self.Genres_open)

        #________________________________________film rating(оцінка фільма)_______________________
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

        self.buttonRating = _MyButton(self)
        self.buttonRating.setText("Доступна система оцінювання")
        self.buttonRating.setFont(QFont("Arial", 9))
        self.buttonRating.setFixedSize(280, 55)
        #self.buttonRating.start_animation()
        self.buttonRating.move(370, 480)
        self.buttonRating.clicked.connect(self.Rating_open)

        self.update_line_edit5()
        #_______________________________________________ age rating______________________________
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

        self.buttonAge = _MyButton(self)
        self.buttonAge.setText("Доступна система рейтингу")
        self.buttonAge.setFont(QFont("Arial", 9))
        self.buttonAge.setFixedSize(280, 55)
        #self.buttonAge.start_animation()
        self.buttonAge.move(690, 480)
        self.buttonAge.clicked.connect(self.Age_Rating_open)

        self.update_line_edit6()
        #___________________________________________Кінець коду елементів__________________________

    def open_newSeries(self):                               # ШО ЦЕЙ КОД РОБИТЬ?
        from ProgramPack.Movies_module.Add_new_Film import new_Film

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
        import Image_resource_rc
        resource_path = ":/jsons/Filmanecdotes.json"

        # Open and read the resource using QFile and QTextStream
        file = QFile(resource_path)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            stream.setCodec("UTF-8")  # Set the encoding to UTF-8
            anecdotes = json.loads(stream.readAll())
            file.close()
            #print(json_data)
        """
        else:
            print("Error opening the resource file.")
        # Відкриття JSON-файлу та завантаження анекдотів
        try:
            file_path = ':/jsons/Filmanecdotes.json'
            with open(file_path, 'r', encoding='utf-8') as file:
                anecdotes = json.load(file)
        except FileNotFoundError:
            print("Файл не знайдено. Перевірте правильність шляху до файлу.")
        except json.JSONDecodeError as e:
            print(f"Помилка декодування JSON: {e}")
        except Exception as e:
            print(f"Сталася невідома помилка: {e}")

        # Вибір випадкового анекдота
        """
        random_anecdote = random.choice(anecdotes)

        return random_anecdote['text']
        #text = "ds"
        #return text
    def open_newFilm(self):
        from ProgramPack.Movies_module.Add_new_Film import new_Film
        #___________________Стерти поле жанрів_______________________________________________
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                pass  # Writing nothing truncates the file (clears its content)

        except Exception as e:
            print(f"Error clearing the file: {e}")
        #___________________Стерти поле оцінки_______________________________________________
        try:
            with open(self.file_path1, 'w', encoding='utf-8') as file:
                pass  # Writing nothing truncates the file (clears its content)

        except Exception as e:
            print(f"Error clearing the file: {e}")
        #___________________Стерти поле вікового рейтингу____________________________________
        try:
            with open(self.file_path2, 'w', encoding='utf-8') as file:
                pass  # Writing nothing truncates the file (clears its content)

        except Exception as e:
            print(f"Error clearing the file: {e}")

        self.newFilm = new_Film()
        self.newFilm.show()
        self.close()
    def Genres_open(self):
        from ProgramPack.src.GenresWindow import GenreSelectionApp
        import Image_resource_rc
        resource_path = ":/jsons/Genres.json"

        # Open and read the resource using QFile and QTextStream
        file = QFile(resource_path)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            stream.setCodec("UTF-8")  # Set the encoding to UTF-8
            genres_data = json.loads(stream.readAll())
            genres = genres_data["genres"]
            file.close()

        self.wind = GenreSelectionApp(genres)
        self.wind.setWindowModality(Qt.ApplicationModal)
        self.wind.show()
        '''Старий формат считування json file 
        with open(":/Genres.json", "r", encoding='utf-8') as file:
            genres_data = json.load(file)
            genres = genres_data["genres"]

        self.wind = GenreSelectionApp(genres)
        self.wind.setWindowModality(Qt.ApplicationModal)
        self.wind.show()
        '''
    def update_line_edit4(self):
        #file = QFile(self.file_path)
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                text_content = file.read()
            self.line_edit4.setPlainText(text_content)

        except Exception as e:
            print(f"Error reading the file: {e}")
    def update_line_edit5(self):
        #file1 = QFile(self.file_path1)
        try:
            with open(self.file_path1, 'r', encoding='utf-8') as file:
                text_content = file.read()
            self.line_edit5.setPlainText(text_content)

        except Exception as e:
            print(f"Error reading the file: {e}")
    def update_line_edit6(self):
        try:
            with open(self.file_path2, 'r', encoding='utf-8') as file:
                text_content = file.read()
            self.line_edit6.setPlainText(text_content)

        except Exception as e:
            print(f"Error reading the file: {e}")
        #__Формат для считування /qrc файлу
        '''try:
            with open(self.file_path2   , 'r', encoding='utf-8') as file:
                text = file.read()
                self.line_edit6.setPlainText(text)
        except FileNotFoundError:
            self.line_edit6.setPlainText("Файл не знайдено")
        except Exception as e:
            print("Exception in update_line_edit4:", e)
            QMessageBox.critical(self, 'Помилка', f'Виникла помилка при оновленні вмісту:\n{str(e)}')'''
    def Rating_open(self):
        from ProgramPack.src.series_movie_rating import MovieRatingApp

        self.wind = MovieRatingApp()
        self.wind.setWindowModality(Qt.ApplicationModal)
        self.wind.show()
    def Age_Rating_open(self):
        from ProgramPack.src.Age_rating import Age_MovieRatingApp

        self.wind = Age_MovieRatingApp()
        self.wind.setWindowModality(Qt.ApplicationModal)
        self.wind.show()