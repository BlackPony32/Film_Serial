from PyQt5.QtWidgets import QVBoxLayout, QWidget, QDesktopWidget, QLabel, QApplication, QHBoxLayout
from PyQt5.QtGui import QFont, QPixmap
from MyButton import MyButton
from MyWindowFormat import MyWindowFormat
#from ProgramPack.src.MainWindow import _MainWindow


class new_Film(MyWindowFormat):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Додати новий фільм")
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
        # self.setStyleSheet("background-image: url(../img/popcorn4.png);")

        # Створення кнопок і додавання їх до контейнера
        central_widget = QWidget()
        #layout = QHBoxLayout(central_widget)
        #layout.setSpacing(10)
        self.setCentralWidget(central_widget)

        # Створення кнопок і додавання їх до контейнера
        font = QFont()
        font.setPointSize(16)  # Встановлюємо розмір тексту кнопки

        button1 = MyButton()
        button2 = MyButton()
        button3 = MyButton()

        button1.setText("Назад")
        button1.setFont(font)
        #button1.setGeometry(100, 10, 20, 70)
        button1.setFixedSize(450, 70)
        #button1.start_animation()
        #button1.move(100, 100)
        button1.clicked.connect(self.open_main_Window)

        button2.setText("Новий переглянутий фільм")
        button2.setFont(font)
        button2.setFixedSize(450, 70)
        #button2.start_animation()
        #button2.move(300, 100)
        button2.clicked.connect(self.open_main_Window)

        button3.setText("'Переглянути потім...'")
        button3.setFont(font)
        button3.setFixedSize(450, 70)
        #button3.start_animation()
        #button3.move(200, 200)
        button3.clicked.connect(self.open_main_Window)

        central_widget.add
        #layout.addWidget(button1)
        #layout.addWidget(button2)
        #layout.addWidget(button3)
    def open_main_Window(self):
        from ProgramPack.src.MainWindow import _MainWindow
        self.main_Window = _MainWindow()
        self.main_Window.show()
        self.close()