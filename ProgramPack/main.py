import os
import sys

#from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from ProgramPack.src.MainWindow import _MainWindow

if __name__ == '__main__':
    try:
        file_path = os.path.join(os.getcwd(), "data.txt")
        with open(file_path, 'w', encoding='utf-8') as file:
            pass  # Writing nothing truncates the file (clears its content)

    except Exception as e:
        print(f"Error clearing the file: {e}")
    # ___________________Стерти поле оцінки_______________________________________________
    try:
        file_path1 = os.path.join(os.getcwd(), "movie_rating_result.txt")
        with open(file_path1, 'w', encoding='utf-8') as file:
            pass  # Writing nothing truncates the file (clears its content)

    except Exception as e:
        print(f"Error clearing the file: {e}")
    # ___________________Стерти поле вікового рейтингу____________________________________
    try:
        file_path2 = os.path.join(os.getcwd(), "movie_age_rating.txt")
        with open(file_path2, 'w', encoding='utf-8') as file:
            pass  # Writing nothing truncates the file (clears its content)

    except Exception as e:
        print(f"Error clearing the file: {e}")

    # ___________________Стерти лейбл сезонів____________________________________
    try:
        file_path40 = os.path.join(os.getcwd(), "Series_QuantitySeason.txt")
        with open(file_path40, 'w', encoding='utf-8') as file:
            pass  # Writing nothing truncates the file (clears its content)

    except Exception as e:
        print(f"Error clearing the file: {e}")
    # ___________________Стерти поле режисерів____________________________________
    file_path4 = os.path.join(os.getcwd(), "dataDirectors.txt")
    try:
        with open(file_path4, 'w', encoding='utf-8') as file:
            pass  # Writing nothing truncates the file (clears its content)

    except Exception as e:
        print(f"Error clearing the file: {e}")
    # ___________________Стерти поле режисерів____________________________________
    file_path5 = os.path.join(os.getcwd(), "dataActors.txt")
    try:
        with open(file_path5, 'w', encoding='utf-8') as file:
            pass  # Writing nothing truncates the file (clears its content)

    except Exception as e:
        print(f"Error clearing the file: {e}")
    # ___________________Стерти поле статусу серіала______________________________
    file_path3 = os.path.join(os.getcwd(), "Series_status.txt")
    try:
        with open(file_path3, 'w', encoding='utf-8') as file:
            pass  # Writing nothing truncates the file (clears its content)

    except Exception as e:
        print(f"Error clearing the file: {e}")
    app = QApplication(sys.argv)

    window = _MainWindow()

    window.show()
    sys.exit(app.exec_())
