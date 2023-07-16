import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget


class MovieRatingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Оцінка фільмів")
        self.setGeometry(200, 200, 500, 300)

        self.ratings = {
            1: "Дуже поганий фільм (не рекомендую)",
            2: "Поганий фільм",
            3: "Не дуже вдалий фільм",
            4: "Середній фільм",
            5: "Непоганий фільм",
            6: "Хороший фільм",
            7: "Дуже хороший фільм",
            8: "Чудовий фільм",
            9: "Відмінний фільм",
            10: "Шедевр!"
        }

        layout = QVBoxLayout()

        for rating, comment in self.ratings.items():
            hbox = QHBoxLayout()

            comment_label = QLabel(comment)
            hbox.addWidget(comment_label)

            rating_button = QPushButton(f"{rating}/10")
            rating_button.clicked.connect(self.show_result)
            hbox.addWidget(rating_button)

            layout.addLayout(hbox)

        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        save_button = QPushButton("Зберегти результат")
        save_button.clicked.connect(self.save_to_file)
        layout.addWidget(save_button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def show_result(self):
        button = self.sender()
        rating = int(button.text().split("/")[0])
        comment = self.ratings[rating]
        self.result_label.setText(f"Ви обрали оцінку: {button.text()}\n{comment}")

        self.current_result = f"Ви обрали оцінку: {button.text()}\n{comment}"

    def save_to_file(self):
        try:
            with open("movie_rating_result.txt", "w", encoding="utf-8") as file:
                file.write(self.current_result)
            #self.result_label.setText("Результат збережено у файл 'movie_rating_result.txt'")
        except Exception as e:
            self.result_label.setText("Помилка збереження у файл!")
        self.close()



