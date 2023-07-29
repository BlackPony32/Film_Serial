import os
import sys

from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox


class Age_MovieRatingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Віковий рейтинг фільмів")
        self.setGeometry(200, 200, 400, 150)

        self.ratings = {
            "Не обрано": "Не обрано",
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

        self.description_label = QLabel("Не обрано")
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
        self.description = self.ratings[selected_rating]
        self.description_label.setText(self.description)

    def save_to_file(self):
        project_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        file_path = os.path.join(project_dir, "movie_age_rating.txt")
        self.update_description()
        # Open the file for writing and save the text
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.description)
            self.close()
            # QMessageBox.information(self, 'Success', 'Text saved successfully!')

        except Exception as e:
            print(f"Error writing to the file: {e}")
            QMessageBox.critical(self, 'Error', f'Error saving text:\n{str(e)}')


