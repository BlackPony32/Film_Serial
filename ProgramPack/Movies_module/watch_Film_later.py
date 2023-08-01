from PyQt5.QtWidgets import QVBoxLayout, QWidget, QDesktopWidget, QLabel, QLineEdit, QPlainTextEdit, QCalendarWidget, QMessageBox
from PyQt5.QtGui import QFont
from ProgramPack.src.MyButton import _MyButton
from ProgramPack.src.MyWindowFormat import MyWindowFormat
from PyQt5.QtCore import QDate, Qt, QFile, QTextStream


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
        self.setStyleSheet(
            '''
            QMainWindow {
                background-image: url(":/images/cinema2.png");
            }
            '''
        )
        # Set the background image using a style sheet
        self.setStyleSheet(self.styleSheet())

        button1 = _MyButton(self)
        button2 = _MyButton(self)

        button1.setText("Назад")
        button1.setStyleSheet(
            '''
            QPushButton {
                background-color: #6C3483;  /* Пурпурно-червоний */
                color: #FFFFFF;
                border-style: outset;
                padding: 2px;
                font: bold 25px;
                border-width: 6px;
                border-radius: 15px;
                border-color: #512E5F;  /* Темний пурпурно-червоний */
            }
            QPushButton:hover {
                background-color: #F39C12;  /* Помаранчевий */
            }
            QPushButton:pressed {
                background-color: #117A65;  /* Темний зелений */
            }
            '''
        )
        button1.setFixedSize(350, 60)
        button1.move(45, 600)
        button1.clicked.connect(self.open_newSeries)

        button2.setText("Додати фільм")
        button2.setStyleSheet(
            '''
            QPushButton {
                background-color: #6C3483;  /* Пурпурно-червоний */
                color: #FFFFFF;
                border-style: outset;
                padding: 2px;
                font: bold 25px;
                border-width: 6px;
                border-radius: 15px;
                border-color: #512E5F;  /* Темний пурпурно-червоний */
            }
            QPushButton:hover {
                background-color: #F39C12;  /* Помаранчевий */
            }
            QPushButton:pressed {
                background-color: #117A65;  /* Темний зелений */
            }
            '''
        )
        button2.setFixedSize(350, 60)
        button2.move(620, 600)
        button2.clicked.connect(self.open_newSeries)

        # ___________________Лейбл про анегдот та поле для виводу випадкового анегдоту______________________________
        label0 = QLabel(self)
        labelAnec = QPlainTextEdit(self)

        label0.setFont(QFont("Arial", 15))
        label0.setStyleSheet("color: lightgray")
        label0.setText("Невеликий анегдот на тематику фільмів (згенеровано АІ)")
        label0.setFixedSize(795, 30)
        label0.move(45, 15)

        self.generate_random_anecdote()
        random_joke = self.generate_random_anecdote()

        labelAnec.setFont(QFont("Arial", 15))
        labelAnec.setStyleSheet(
            '''
            QPlainTextEdit {
                background-color: #FDFD96;  /* Світло-жовтий фон */
                border: 2px solid #FF5733;  /* Червона рамка */
                border-radius: 15px;
                padding: 10px;
                font-size: 15px;
            }
            QPlainTextEdit:focus {
                border-color: #0074D9;  /* Задаємо колір рамки при фокусі */
                background-color: #85C1E9;  /* Задаємо колір фону при фокусі */
            }
            '''
        )
        labelAnec.setPlainText(random_joke)
        labelAnec.setReadOnly(True)
        labelAnec.setFixedSize(930, 70)
        labelAnec.move(45, 45)

        # ______________Назва фільма і поле для вводу назви_________________
        line_edit1 = QLineEdit(self)
        label1 = QLabel(self)
        label2 = QLabel(self)
        line_edit3 = QPlainTextEdit(self)
        label3 = QLabel(self)

        label1.setFont(QFont("Arial", 15))
        label1.setStyleSheet("color: lightgray")
        label1.setText("Назва фільма")
        label1.setFixedSize(200, 30)
        label1.move(45, 120)

        line_edit1.setPlaceholderText("Введіть назву фільма")
        line_edit1.setFont(QFont("Arial", 13))
        line_edit1.setStyleSheet(
            '''
            QLineEdit {
                background-color: #FDFD96;  /* Світло-жовтий фон */
                border: 2px solid #FF5733;  /* Червона рамка */
                border-radius: 15px;
                padding: 10px;
                font-size: 18px;
            }
            QLineEdit:focus {
                border-color: #0074D9;  /* Задаємо колір рамки при фокусі */
                background-color: #85C1E9;  /* Задаємо колір фону при фокусі */
            }
            '''
        )
        line_edit1.setFixedSize(685, 50)
        line_edit1.move(290, 120)

        label2.setFont(QFont("Arial", 15))
        label2.setStyleSheet("color: lightgray")
        label2.setText("Оберіть дату додавання фільма")
        label2.setFixedSize(570, 30)
        label2.move(45, 175)
        # ___________________Блок дати додавання дати_____________________________________________
        self.labelDate = QLabel(self)
        self.labelDate.setFont(QFont("Arial", 15))
        self.labelDate.setStyleSheet("color: white")
        self.current_date = QDate.currentDate()
        # self.labelDate.setText(self.current_date.toString("dd.MM.yyyy")) #баг про накладання дат
        self.labelDate.setFixedSize(200, 45)
        self.labelDate.move(300, 205)

        self.buttonDate = _MyButton(self)
        self.buttonDate.setText("Дата додавання")
        self.buttonDate.setFont(QFont("Arial", 14))
        self.buttonDate.setFixedSize(250, 45)
        self.buttonDate.move(45, 205)
        self.buttonDate.clicked.connect(self.buttonDateClicked)
        # _______________________Блок опису фільма____________________________________________
        label3.setFont(QFont("Arial", 15))
        label3.setStyleSheet("color: lightgray")
        label3.setText("Короткий опис")
        label3.setFixedSize(250, 30)
        label3.move(45, 265)

        line_edit3.setPlaceholderText("Додайте короткий опис чи замітки по фільму")
        line_edit3.setFont(QFont("Arial", 9))  # 13 норм розмір
        line_edit3.setStyleSheet(
            '''
            QPlainTextEdit {
                background-color: #FDFD96;  /* Світло-жовтий фон */
                border: 2px solid #FF5733;  /* Червона рамка */
                border-radius: 15px;
                padding: 10px;
                font-size: 15px;
            }
            QPlainTextEdit:focus {
                border-color: #0074D9;  /* Задаємо колір рамки при фокусі */
                background-color: #85C1E9;  /* Задаємо колір фону при фокусі */
            }
            '''
        )
        line_edit3.setFixedSize(700, 80)
        line_edit3.move(270, 265)

    def open_newSeries(self):
        from ProgramPack.Movies_module.Add_new_Film import new_Film
        self.newFilm = new_Film()
        self.newFilm.show()
        self.close()

    def show_calendar(self):
        try:
            from PyQt5.QtGui import QIcon
            from IPython.external.qt_for_kernel import QtGui
            self.calendar = QCalendarWidget()
            icon = QIcon(":/images/MovieIcon.jpg")

            # Встановлюємо картинку як іконку вікна

            width = 32  # Desired width
            height = 32  # Desired height
            resized_icon = icon.pixmap(width, height).scaled(width, height)

            # Set the resized icon as the taskbar icon for the main window

            # self.calendar.setWindowModality(Qt.ApplicationModal)
            self.calendar = QCalendarWidget()
            self.calendar.setWindowModality(Qt.ApplicationModal)
            self.calendar.clicked.connect(self.select_date)

            self.widget = QWidget()
            layout = QVBoxLayout()
            layout.addWidget(self.calendar)
            self.widget.setWindowIcon(QtGui.QIcon(resized_icon))
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
        import Image_resource_rc
        resource_path = ":/jsons/Filmanecdotes.json"

        # Open and read the resource using QFile and QTextStream
        file = QFile(resource_path)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            stream.setCodec("UTF-8")  # Set the encoding to UTF-8
            anecdotes = json.loads(stream.readAll())
            file.close()
        random_anecdote = random.choice(anecdotes)

        return random_anecdote['text']