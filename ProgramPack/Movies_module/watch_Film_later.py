from PyQt5.QtWidgets import QVBoxLayout, QWidget, QDesktopWidget, QLabel, QLineEdit, QPlainTextEdit, QCalendarWidget, QMessageBox
from PyQt5.QtGui import QFont
from ProgramPack.src.MyButton import _MyButton
from ProgramPack.src.MyWindowFormat import MyWindowFormat
from PyQt5.QtCore import QDate, Qt


class _new_Film_later(MyWindowFormat):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Переглянути фільм пізніше")
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
        #self.setStyleSheet("background-image: url(../img/cinema1.png);")
        font = QFont()
        font.setPointSize(16)  # Встановлюємо розмір тексту кнопки

        button1 = _MyButton(self)
        button2 = _MyButton(self)

        button1.setText("Назад")
        button1.setFont(font)
        button1.setFixedSize(450, 70)
        button1.start_animation()
        button1.move(45, 600)
        button1.clicked.connect(self.open_newSeries)

        button2.setText("Додати фільм")
        button2.setFont(font)
        button2.setFixedSize(450, 70)
        button2.start_animation()
        button2.move(510, 600)
        button2.clicked.connect(self.open_newSeries)
        #
        label0 = QLabel(self)
        labelAnec = QPlainTextEdit(self)

        label0.setFont(QFont("Arial", 17))
        label0.setStyleSheet("color: blue")
        label0.setText("Невеликий анегдот на тематику фільмів (згенеровано АІ)")
        label0.setFixedSize(800, 30)
        label0.move(10, 15)

        self.generate_random_anecdote()
        random_joke = self.generate_random_anecdote()


        labelAnec.setFont(QFont("Arial", 17))
        labelAnec.setStyleSheet("color: blue")
        labelAnec.setPlainText(random_joke)
        labelAnec.setFixedSize(800, 140)
        labelAnec.move(10, 45)

        #layout = QFormLayout()
        line_edit1 = QLineEdit(self)
        label1 = QLabel(self)
        #line_edit2 = QLineEdit(self)
        label2 = QLabel(self)
        line_edit3 = QLineEdit(self)
        label3 = QLabel(self)

        label1.setFont(QFont("Arial", 17))
        label1.setStyleSheet("color: blue")
        label1.setText("Назва фільма")
        label1.setFixedSize(250, 30)
        label1.move(45, 200)

        line_edit1.setPlaceholderText("Введіть назву фільма")
        line_edit1.setFont(QFont("Arial", 13))
        line_edit1.setStyleSheet("background-color: #F0F0F0")
        line_edit1.setFixedSize(350, 30)
        line_edit1.move(270, 200)

        label2.setFont(QFont("Arial", 17))
        label2.setStyleSheet("color: blue")
        label2.setText("Оберіть дату додавання фільма")
        label2.setFixedSize(570, 30)
        label2.move(45, 255)
        #____________________________________________________________________________

        self.labelDate = QLabel(self)
        self.labelDate.setFont(QFont("Arial", 17))
        self.labelDate.setStyleSheet("background-color: transparent")  # Set transparent background
        self.current_date = QDate.currentDate()
        self.labelDate.setFixedSize(200, 50)
        self.labelDate.move(300, 310)

        self.buttonDate = _MyButton(self)
        self.buttonDate.setText("Дата додавання")
        self.buttonDate.setFont(font)
        self.buttonDate.setFixedSize(250, 55)
        self.buttonDate.start_animation()
        self.buttonDate.move(45, 310)
        self.buttonDate.clicked.connect(self.buttonDateClicked)
        #___________________________________________________________________
        label3.setFont(QFont("Arial", 17))
        label3.setStyleSheet("color: blue")
        label3.setText("Короткий опис")
        label3.setFixedSize(250, 30)
        label3.move(45, 370)

        line_edit3.setPlaceholderText("Додайте короткий опис чи замітки по фільму")
        line_edit3.setFont(QFont("Arial", 9)) #13 норм розмір
        line_edit3.setStyleSheet("background-color: #F0F0F0")
        line_edit3.setFixedSize(350, 30)
        line_edit3.move(270, 370)

    def open_newSeries(self):
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
        with open('../data/Filmanecdotes.json', 'r', encoding='utf-8') as file:
            anecdotes = json.load(file)

        # Вибір випадкового анекдота
        random_anecdote = random.choice(anecdotes)

        return random_anecdote['text']