import os

from PyQt5.QtCore import QFileSystemWatcher, QDate, Qt, QFile, QTextStream
from PyQt5.QtWidgets import QDesktopWidget, QLineEdit, QLabel, QPlainTextEdit, QCalendarWidget, QWidget, QVBoxLayout, \
    QMessageBox
from PyQt5.QtGui import QFont
from ProgramPack.src.MyButton import _MyButton
from ProgramPack.src.MyWindowFormat import MyWindowFormat

class _new_Series_later(MyWindowFormat):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Переглянути серіал пізніше")
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
        self.setStyleSheet("background-image: url(../img/light_cinema.png);")
        font = QFont()
        font.setPointSize(16)  # Встановлюємо розмір тексту кнопки
        #______________Тим часовий лейбл)__________________________________________________________
        TempLable = QLabel(self)
        TempLable.setFont(QFont("Arial", 41))
        TempLable.setStyleSheet("color: red")
        TempLable.setText("Не затягуйте з переглядом")
        TempLable.setFixedSize(855, 105)
        TempLable.move(80, 25)

        # _____________Основні кнопки для переходу по сторінках і збереження даних в базу___________
        button1 = _MyButton(self)
        button2 = _MyButton(self)

        button1.setText("Назад")
        button1.setFont(font)
        button1.setFixedSize(450, 70)
        #button1.start_animation()
        button1.move(45, 600)
        button1.clicked.connect(self.open_newSeries)

        button2.setText("Додати серіал")
        button2.setFont(font)
        button2.setFixedSize(450, 70)
        #button2.start_animation()
        button2.move(510, 600)
        #button2.clicked.connect(self.open_newSeries)

        # на 200 пікселів вниз змістив
        # ______________Назва серіала і поле для вводу назви_________________
        line_edit1 = QLineEdit(self)
        label1 = QLabel(self)
        label2 = QLabel(self)
        label22 = QLabel(self)
        # line_edit3 = QPlainTextEdit(self)
        # label3 = QLabel(self)

        label1.setFont(QFont("Arial", 15))
        label1.setStyleSheet("color: blue")
        label1.setText("Назва серіала")
        label1.setFixedSize(200, 30)
        label1.move(45, 215)

        line_edit1.setPlaceholderText("Введіть назву серіала")
        line_edit1.setFont(QFont("Arial", 13))
        line_edit1.setStyleSheet("background-color: #F0F0F0")
        line_edit1.setFixedSize(685, 30)
        line_edit1.move(290, 215)

        # ___________________Блок додавання дати_____________________________________________
        label2.setFont(QFont("Arial", 15))
        label2.setStyleSheet("color: blue")
        label2.setText("Оберіть дату додавання серіала")
        label2.setFixedSize(570, 30)
        label2.move(45, 255)

        self.labelDate = QLabel(self)
        self.labelDate.setFont(QFont("Arial", 15))
        self.labelDate.setStyleSheet("background-color: transparent")  # Set transparent background
        self.current_date = QDate.currentDate()
        # self.labelDate.setText(self.current_date.toString("dd.MM.yyyy")) #баг про накладання дат
        self.labelDate.setFixedSize(200, 45)
        self.labelDate.move(370, 305)

        self.buttonDate = _MyButton(self)
        self.buttonDate.setText("Дата додавання серіала")
        self.buttonDate.setFont(QFont("Arial", 14))
        self.buttonDate.setFixedSize(300, 45)
        # self.buttonDate.start_animation()
        self.buttonDate.move(45, 305)
        self.buttonDate.clicked.connect(self.buttonDateClicked)
        # ___________________Блок кількості сезонів_____________________________________________
        label22.setFont(QFont("Arial", 15))
        label22.setStyleSheet("color: blue")
        label22.setText("Оберіть скільки сезонів в серіалі")
        label22.setFixedSize(570, 30)
        label22.move(555, 255)

        self.labelCount = QLabel(self)
        self.labelCount.setFont(QFont("Arial", 15))
        self.labelCount.setStyleSheet("background-color: transparent")  # Set transparent background
        self.current_date = QDate.currentDate()
        # self.labelDate.setText(self.current_date.toString("dd.MM.yyyy")) #баг про накладання дат
        self.labelCount.setFixedSize(200, 45)
        self.labelCount.move(610, 305)

        self.buttonCount = _MyButton(self)
        self.buttonCount.setText("Кількість сезонів: ")
        self.buttonCount.setFont(QFont("Arial", 14))
        self.buttonCount.setFixedSize(300, 45)
        # self.buttonCount.start_animation()
        self.buttonCount.move(550, 305)
        # self.buttonCount.clicked.connect(self.buttonCountClicked)
        '''
        # _______________________________Блок жанрів серіала________________________________
        label4 = QLabel(self)

        label4.setFont(QFont("Arial", 15))
        label4.setStyleSheet("color: blue")
        label4.setText("Оберіть жанр серіала")
        label4.setFixedSize(280, 30)
        label4.move(45, 175)

        self.line_edit4 = QPlainTextEdit(self)
        self.line_edit4.setPlaceholderText("Запишіть жанр серіала самостійно або оберіть з доступних")
        self.file_name = "data.txt"
        self.file_path = os.path.join(os.getcwd(), self.file_name)

        self.file_watcher = QFileSystemWatcher()
        self.file_watcher.addPath(self.file_path)
        self.file_watcher.fileChanged.connect(self.update_line_edit4)

        self.update_line_edit4()
        self.line_edit4.setFont(QFont("Arial", 9))  # 13 норм розмір
        self.line_edit4.setStyleSheet("background-color: #F0F0F0")
        self.line_edit4.setFixedSize(280, 85)
        self.line_edit4.move(45, 225)

        self.buttonGanre = _MyButton(self)
        self.buttonGanre.setText("Доступні жанри")
        self.buttonGanre.setFont(QFont("Arial", 13))
        self.buttonGanre.setFixedSize(280, 55)
        # self.buttonGanre.start_animation()
        self.buttonGanre.move(45, 320)
        self.buttonGanre.clicked.connect(self.Genres_open)

        # ________________________________________series rating(оцінка серіала)_______________________
        label5 = QLabel(self)
        label5.setFont(QFont("Arial", 15))
        label5.setStyleSheet("color: blue")
        label5.setText("Оберіть оцінку серіала")
        label5.setFixedSize(280, 30)
        label5.move(370, 175)

        self.line_edit5 = QPlainTextEdit(self)
        self.line_edit5.setPlaceholderText(
            "Запишіть оцінку серіала самостійно або скористайтесь запропонованою системою")
        self.file_name1 = "movie_rating_result.txt"
        self.file_path1 = os.path.join(os.getcwd(), self.file_name1)

        self.file_watcher1 = QFileSystemWatcher()
        self.file_watcher1.addPath(self.file_path1)
        self.file_watcher1.fileChanged.connect(self.update_line_edit5)

        self.line_edit5.setFont(QFont("Arial", 9))  # 13 норм розмір
        self.line_edit5.setStyleSheet("background-color: #F0F0F0")
        self.line_edit5.setFixedSize(280, 85)
        self.line_edit5.move(370, 225)

        self.buttonRating = _MyButton(self)
        self.buttonRating.setText("Доступна система оцінювання")
        self.buttonRating.setFont(QFont("Arial", 9))
        self.buttonRating.setFixedSize(280, 55)
        # self.buttonRating.start_animation()
        self.buttonRating.move(370, 320)
        self.buttonRating.clicked.connect(self.Rating_open)

        self.update_line_edit5()
        '''
        # _______________________Блок опису серіала____________________________________________
        line_edit3 = QPlainTextEdit(self)
        label3 = QLabel(self)
        label3.setFont(QFont("Arial", 15))
        label3.setStyleSheet("color: blue")
        label3.setText("Короткий опис")
        label3.setFixedSize(250, 30)
        label3.move(45, 415)

        line_edit3.setPlaceholderText("Додайте короткий опис чи замітки по серіалу")
        line_edit3.setFont(QFont("Arial", 9))  # 13 норм розмір
        line_edit3.setStyleSheet("background-color: #F0F0F0")
        line_edit3.setFixedSize(700, 80)
        line_edit3.move(270, 415)
        # ___________________________________________Кінець коду елементів__________________________

    def open_newSeries(self):
        from ProgramPack.Series_module.Add_new_Series import new_Series
        self.newSeries = new_Series()
        self.newSeries.show()
        self.close()
    def buttonDateClicked(self):
        self.labelDate.setText("")
        if self.buttonDate.isEnabled():
            self.show_calendar()
            self.update_label()
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
    def Genres_open(self):
        from ProgramPack.src.GenresWindow import GenreSelectionApp
        import Image_resource_rc
        resource_path = ":/jsons/Genres.json"

        # Open and read the resource using QFile and QTextStream
        file = QFile(resource_path)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            stream.setCodec("UTF-8")  # Set the encoding to UTF-8
            import json
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
