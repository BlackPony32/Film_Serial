from PyQt5.QtWidgets import QVBoxLayout, QWidget, QDesktopWidget, QLabel, QApplication, QHBoxLayout, QLineEdit, \
    QFormLayout
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

        #
        widget = QWidget()
        layout = QFormLayout()

        label1 = CustomLabelLineEdit("Ім'я:", "Введіть ім'я")
        label1.setFont(QFont("Arial", 12, QFont.Bold))
        label1.setStyleSheet("color: blue")

        label2 = CustomLabelLineEdit("Прізвище:", "Введіть прізвище")
        label2.setFont(QFont("Arial", 12, QFont.Bold))
        label2.setStyleSheet("color: blue")

        label3 = CustomLabelLineEdit("Вік:", "Введіть вік")
        label3.setFont(QFont("Arial", 12, QFont.Bold))
        label3.setStyleSheet("color: blue")

        layout.addRow(label1.label, label1.line_edit)
        layout.addRow(label2.label, label2.line_edit)
        layout.addRow(label3.label, label3.line_edit)
        layout.addWidget(widget)
        self.setLayout(layout)



    def open_newFilm(self):
        from ProgramPack.src.Add_new_Film import new_Film
        self.newFilm = new_Film()
        self.newFilm.show()
        self.close()