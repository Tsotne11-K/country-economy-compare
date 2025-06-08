
from PyQt5 import QtWidgets, QtGui, QtCore
from economy_ui import Ui_MainWindow
from logic import CountryEconomy
import sys

class EconomyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.logic = CountryEconomy()
        self.language_index = 0
        self.languages = ["English", "ქართული", "Français", "Italiano", "Español"]
        self.country_translations = {
            "English": ["Georgia", "France", "Italy", "Spain"],
            "ქართული": ["საქართველო", "საფრანგეთი", "იტალია", "ესპანეთი"],
            "Français": ["Géorgie", "France", "Italie", "Espagne"],
            "Italiano": ["Georgia", "Francia", "Italia", "Spagna"],
            "Español": ["Georgia", "Francia", "Italia", "España"]
        }

        self.current_lang = "English"
        self.update_country_comboboxes()
        self.setup_styles()
        self.connect_signals()

        self.seconds_inside = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer_label)
        self.timer.start(1000) 

    def setup_styles(self):
        self.setStyleSheet("background-color: #f0f0f0;")
        self.ui.label_title.setStyleSheet("font-size: 20px; font-weight: bold; color: #333;")
        self.ui.label_title.setAlignment(QtCore.Qt.AlignCenter)

        combo_style = """
            QComboBox {
                background-color: white;
                border: 1px solid gray;
                padding: 5px;
                font-size: 14px;
            }
        """
        self.ui.comboBox_country1.setStyleSheet(combo_style)
        self.ui.comboBox_country2.setStyleSheet(combo_style)

        self.ui.pushButton_compare.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.ui.pushButton_compare.setFixedSize(160, 40)

        self.ui.pushButton_language.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                font-size: 14px;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        self.ui.pushButton_language.setFixedSize(160, 40)

        self.ui.textEdit_result.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                border: 1px solid #ccc;
                font-size: 14px;
                padding: 10px;
            }
        """)

        if not hasattr(self.ui, "label_timer"):
            self.ui.label_timer = QtWidgets.QLabel(self)
            self.ui.label_timer.setGeometry(220, 360, 160, 30)
            self.ui.label_timer.setStyleSheet("font-size: 14px; color: #555;")
            self.ui.label_timer.setAlignment(QtCore.Qt.AlignCenter)

    def connect_signals(self):
        self.ui.pushButton_compare.clicked.connect(self.compare_countries)
        self.ui.pushButton_language.clicked.connect(self.change_language)

    def update_country_comboboxes(self):
        self.ui.comboBox_country1.clear()
        self.ui.comboBox_country2.clear()
        countries = self.country_translations[self.current_lang]
        self.ui.comboBox_country1.addItems(countries)
        self.ui.comboBox_country2.addItems(countries)

    def get_english_name(self, name):
        for lang in self.country_translations.values():
            for i, val in enumerate(lang):
                if val == name:
                    return self.country_translations["English"][i]
        return name

    def compare_countries(self):
        c1 = self.get_english_name(self.ui.comboBox_country1.currentText())
        c2 = self.get_english_name(self.ui.comboBox_country2.currentText())
        result = self.logic.compare(c1, c2)
        self.ui.textEdit_result.setText(result)

    def change_language(self):
        self.language_index = (self.language_index + 1) % len(self.languages)
        self.current_lang = self.languages[self.language_index]
        self.update_country_comboboxes()

    def update_timer_label(self):
        self.seconds_inside += 1
        self.ui.label_timer.setText(f"აპლიკაციაში დრო: {self.seconds_inside} წთ")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = EconomyApp()
    window.setWindowTitle("Country Economy Compare")
    window.setFixedSize(600, 400)
    window.show()
    sys.exit(app.exec_())
