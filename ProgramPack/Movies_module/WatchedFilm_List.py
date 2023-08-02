import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QDesktopWidget, QTableWidgetItem, \
    QHeaderView, QHBoxLayout, QTableWidget, QScrollArea, QVBoxLayout, QWidget
import psycopg2
from ProgramPack.src.MyButton import _MyButton
from ProgramPack.src.MyWindowFormat import MyWindowFormat

class _WatchedFilmList(MyWindowFormat):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Список переглянутих фільмів")
        self.setGeometry(0, 0, 1000, 750)

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
        label1 = QLabel(self)
        label1.setFont(QFont("Arial", 15))
        label1.setStyleSheet("color: black")
        label1.setText("Пошуковий фільтр")
        label1.setFixedSize(300, 30)
        label1.move(45, 20)
        # Додайте рядок пошуку
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Введіть ключові слова для пошуку")
        self.search_input.setStyleSheet(
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
        self.search_input.move(350,20)
        self.search_input.setFixedSize(600,45)

        # Додайте прокрутний віджет
        scroll_area = QScrollArea(self)
        scroll_area.move(0,70)
        scroll_area.setFixedSize(1000, 500)

        # Додайте таблицю в прокрутний віджет
        self.table_widget = QTableWidget(self)
        self.table_widget.move(0,70)
        self.table_widget.setFixedSize(1000, 500)
        scroll_area.setWidget(self.table_widget)

        # Підключення сигналу текстового поля до слоту для динамічного пошуку
        self.search_input.textChanged.connect(self.filter_table)

        self.connect_to_postgresql()

        # Додайте кнопки
        button_layout = QHBoxLayout()
        self.button1 = QPushButton("Видалити фільм", self)
        self.button1.setStyleSheet(
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
        self.button1.setFixedSize(315, 60)
        self.button1.move(45, 580)

        self.button2 = QPushButton("Назад", self)
        self.button2.setStyleSheet(
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
        self.button2.setFixedSize(275, 60)
        self.button2.move(365, 650)
        self.button2.clicked.connect(self.back)

        self.button3 = QPushButton("Оновити дані таблиці", self)
        self.button3.setStyleSheet(
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
        self.button3.setFixedSize(315, 60)
        self.button3.move(645, 580)
        self.button3.clicked.connect(self.update_database)

    def connect_to_postgresql(self):
        try:
            # Підключення до бази даних PostgreSQL
            conn = psycopg2.connect(
                host="localhost",
                port="5432",
                database="Film_Series",
                user="postgres",
                password="postgresql"
            )

            # Виконання SQL-запиту та виведення даних у таблиці
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Watched_Film_List")
            rows = cursor.fetchall()
            # Приховання стовпця з нумерацією
            self.table_widget.verticalHeader().setVisible(False)
            self.table_widget.setRowCount(len(rows))
            desired_column_count = 6
            self.table_widget.setColumnCount(desired_column_count)

            # Налаштування стилю та вигляду таблиці
            self.table_widget.setStyleSheet("""
                QTableWidget {
                    background-color: white;
                    alternate-background-color: #f2f2f2;
                    color: #333;
                }

                QTableWidget::item:selected {
                    background-color: #0078d4;
                    color: white;
                }
            """)

            # Налаштування заголовків стовпців
            header_labels = ["Назва фільма", "Дата додавання", "Жанр", "Оцінка фільма", "Вікові обмеження","Опис фільма"]
            self.table_widget.setHorizontalHeaderLabels(header_labels)

            header = self.table_widget.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)  # Розтягнути всі стовпці

            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    if len(str(value)) > 15:
                        item.setToolTip(str(value))  # Додано підказки для довгих значень
                    self.table_widget.setItem(i, j, item)

            # Закриття курсора та з'єднання
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            self.setWindowTitle("Помилка підключення до PostgreSQL")
            self.table_widget.setRowCount(0)
            self.table_widget.setColumnCount(0)
            self.table_widget.setHorizontalHeaderLabels(["Error"])
            item = QTableWidgetItem(f"{e}")
            self.table_widget.setItem(0, 0, item)
    def update_database(self):
        try:
            conn = psycopg2.connect(
                host="localhost",
                port="5432",
                database="Film_Series",
                user="postgres",
                password="postgresql"
            )
            cursor = conn.cursor()

            for row in range(self.table_widget.rowCount()):
                movie_name = self.table_widget.item(row, 0).text()
                date_added = self.table_widget.item(row, 1).text()
                genre = self.table_widget.item(row, 2).text()
                movie_rating = self.table_widget.item(row, 3).text()
                age_restrictions = self.table_widget.item(row, 4).text()
                movie_description = self.table_widget.item(row, 5).text()

                # Update the corresponding row in the database based on movie_name and date_added
                cursor.execute(
                    "UPDATE Watched_Film_List SET genre = %s, movie_rating = %s, age_restrictions = %s, movie_description = %s WHERE movie_name = %s AND date_added = %s",
                    (genre, movie_rating, age_restrictions, movie_description, movie_name, date_added)
                )

            conn.commit()
            cursor.close()
            conn.close()
            self.setWindowTitle("Зміни збережено")
        except psycopg2.Error as e:
            self.setWindowTitle("Помилка при збереженні змін")
            print("Помилка бази даних:", e)
            import traceback
            traceback.print_exc()
    def filter_table(self, search_text):
        for row in range(self.table_widget.rowCount()):
            row_hidden = True
            for col in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, col)
                if item is not None:
                    cell_text = item.text().strip().lower()
                    if search_text.lower() in cell_text:
                        row_hidden = False
                        break
            self.table_widget.setRowHidden(row, row_hidden)
    def back(self):
        from ProgramPack.Movies_module.FilmList import _FilmList
        self.newFilm = _FilmList()
        self.newFilm.show()
        self.close()