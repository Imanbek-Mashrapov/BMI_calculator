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

        C:\Users\User\Documents\Python\oop_learning\bmi_calculator_task


