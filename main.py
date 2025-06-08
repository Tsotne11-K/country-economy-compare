
import sys
from PyQt5 import QtWidgets, QtCore
from economy_ui import Ui_MainWindow
from logic import CountryEconomy

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

        self.ui.pushButton_compare.clicked.connect(self.compare_countries)
        self.ui.pushButton_language.clicked.connect(self.change_language)

        self.seconds_inside = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer_label)
        self.timer.start(1000)

        self.update_country_comboboxes()

    def update_country_comboboxes(self):
        self.ui.comboBox_country1.clear()
        self.ui.comboBox_country2.clear()
        countries = self.country_translations[self.current_lang]
        self.ui.comboBox_country1.addItems(countries)
        self.ui.comboBox_country2.addItems(countries)

    def get_english_name(self, name):
        for lang_list in self.country_translations.values():
            for i, val in enumerate(lang_list):
                if val == name:
                    return self.country_translations["English"][i]
        return name

    def compare_countries(self):
        c1 = self.get_english_name(self.ui.comboBox_country1.currentText())
        c2 = self.get_english_name(self.ui.comboBox_country2.currentText())

        # User amount from QLineEdit
        amount_text = self.ui.lineEdit_amount.text()
        try:
            amount = float(amount_text)
        except ValueError:
            self.ui.textEdit_result.setText("გთხოვთ შეიყვანოთ სავალდებულო თანხა სწორ ფორმატში.")
            return

        # კონვერტაცია და შედარება
        converted_amount, currency = self.logic.convert_amount(amount, c1, c2)
        comparison = self.logic.compare(c1, c2)

        result_text = (
            f"{amount} {self.logic.currency_names[c1]} ტოლია ≈ {converted_amount} {currency} \n\n"
            f"{comparison}"
        )
        self.ui.textEdit_result.setText(result_text)

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
