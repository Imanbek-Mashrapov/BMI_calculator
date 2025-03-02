from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QRadioButton
import os
from PyQt6 import uic

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(os.path.dirname(__file__), "bmi_style.ui")
        uic.loadUi(ui_path, self)
        self.initUI()

    def initUI(self):
        """Find all widgets after loading the UI."""
        self.title_label: QLabel = self.findChild(QLabel, "title_label")
        self.standard_radio_button: QRadioButton = self.findChild(QRadioButton, "standard_radio_button")
        self.metric_radio_button: QRadioButton = self.findChild(QRadioButton, "metric_radio_button")
        self.height_input: QLineEdit = self.findChild(QLineEdit, "height_input")
        self.weight_input: QLineEdit = self.findChild(QLineEdit, "weight_input")
        self.height_label: QLabel = self.findChild(QLabel, "height_label")
        self.weight_label: QLabel = self.findChild(QLabel, "weight_label")
        self.calculate_button: QPushButton = self.findChild(QPushButton, "calculate_button")
        self.bmi_result_title: QLabel = self.findChild(QLabel, "bmi_result_title")
        self.bmi_result_label: QLabel = self.findChild(QLabel, "bmi_result_label")
        self.underweight_label: QLabel = self.findChild(QLabel, "underweight_label")
        self.normal_label: QLabel = self.findChild(QLabel, "normal_label")
        self.overweight_label: QLabel = self.findChild(QLabel, "overweight_label")
        self.obese_label: QLabel = self.findChild(QLabel, "obese_label")

        print("Height Label:", self.height_label)
        print("Weight Label:", self.weight_label)
        print("Title Label: ", self.title_label)

        if self.metric_radio_button:
            self.metric_radio_button.setChecked(True)

        if self.height_label:
            self.height_label.setText('Your height (cm)')
        if self.weight_label:
            self.weight_label.setText('Your weight (kg)')

        if self.standard_radio_button:
            self.standard_radio_button.toggled.connect(self.update_labels)
        if self.metric_radio_button:
            self.metric_radio_button.toggled.connect(self.update_labels)

        self.calculate_button.clicked.connect(self.on_click)

        self.action_exit.triggered.connect(self.close)
        self.action_clear.triggered.connect(self.clear_inputs)
        self.action_help.triggered.connect(self.show_help)

        self.update_labels()

    def update_labels(self):
        if self.metric_radio_button.isChecked():
            if self.height_label:
                self.height_label.setText("Height (cm):")
            if self.weight_label:
                self.weight_label.setText("Weight (kg):")

        else:
            if self.height_label:
                self.height_label.setText("Height (ft):")
            if self.weight_label:
                self.weight_label.setText("Weight (lbs):")

    def on_click(self):
        try:
            height = float(self.height_input.text())
            weight = float(self.weight_input.text())

            if height == 0:
                self.bmi_result_label.setText("Height cannot be zero.")
                return

            if self.metric_radio_button.isChecked():
                height_meters = height / 100
                bmi = weight / (height_meters ** 2)
            elif self.standard_radio_button.isChecked():
                bmi = (weight * 703) / (height ** 2)
            else:
                self.bmi_result_label.setText("Please select a unit system.")
                return

            self.bmi_result_label.setText(f"{bmi:.1f}")
            self.on_bmi_color()

        except ValueError:
            self.bmi_result_label.setText("Invalid input. Please enter numbers.")

    def on_bmi_color(self):
        bmi = float(self.bmi_result_label.text())

        if bmi <= 18.5:
            background_color = '#FFD700'
        elif 18.5 < bmi <= 25:
            background_color = '#008000'
        elif 25 < bmi <= 30:
            background_color = '#FFA500'
        elif bmi > 30:
            background_color = '#FF0000'

        self.bmi_result_label.setStyleSheet(f'''background-color: {background_color};
    color: black;
    font-size: 18px;
    font-weight: bold;
    padding: 10px;
    border-radius: 5px;''')


