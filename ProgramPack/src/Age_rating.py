import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout, QWidget


class Age_MovieRatingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Віковий рейтинг фільмів")
        self.setGeometry(200, 200, 400, 150)

        self.ratings = {
            "G": "Для всіх",
            "PG": "Батькам рекомендовано",
            "PG-13": "Для дітей від 13 років",
            "R": "Для дорослих",
            "NC-17": "Тільки для дорослих"
        }

        layout = QVBoxLayout()

        self.rating_combo = QComboBox()
        self.rating_combo.addItems(self.ratings.keys())
        layout.addWidget(QLabel("Виберіть віковий рейтинг фільму:"))
        layout.addWidget(self.rating_combo)

        self.rating_combo.currentIndexChanged.connect(self.update_description)

        self.description_label = QLabel()
        layout.addWidget(self.description_label)

        hbox = QHBoxLayout()
        self.submit_button = QPushButton("Зберегти результат")
        self.submit_button.clicked.connect(self.save_to_file)
        hbox.addWidget(self.submit_button)




        layout.addLayout(hbox)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def update_description(self):
        selected_rating = self.rating_combo.currentText()
        description = self.ratings[selected_rating]
        self.description_label.setText(description)

    def save_to_file(self):
        try:
            selected_rating = self.rating_combo.currentText()
            description = self.ratings[selected_rating]

            result = f"Ви обрали віковий рейтинг: {selected_rating}\nОпис: {description}"

            with open("movie_age_rating.txt", "w", encoding="utf-8") as file:
                file.write(result)
        except Exception as e:
            self.result_label.setText("Помилка збереження у файл!")
        self.close()


