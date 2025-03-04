# BMI Calculator

## Overview
#### This is a PyQt6-based BMI Calculator that allows users to calculate their Body Mass Index (BMI) using either the Metric or Standard measurement system

## Features

#### - Select between Metric (kg, cm) or Standard (lbs, ft) units.
#### - Input fields for height and weight.
#### - Calculates BMI based on the provided inputs.
#### - Displays BMI result with color-coded interpretation.
#### - Provides a help section for users.
#### - Options to clear inputs and exit the application.

## How to Run

#### - Clone or download the repository.
#### - Ensure all required dependencies are installed.
#### - Run the following command in your terminal:
```python
python main.py
```

## Class and Method Documentation

### MyWindow Class

#### This class represents the main application window and handles the logic for BMI calculation.

### Methods:
#### - __init__(): Initializes the main window and loads the UI.
#### - initUI(): Connects UI elements and sets default values.
#### - update_labels(): Updates labels based on the selected unit system.
#### - show_help(): Displays a help message with instructions on how to use the application.
#### - on_click(): Handles BMI calculation based on user input.
#### - on_bmi_color(): Updates the background color of the BMI result label based on the BMI range.
#### - clear_inputs(): Clears all input fields and resets the result label.


## Sample Input/Output
### Example 1 (Metric System)

#### Input:
#### - Height: 177 cm
#### - Weight: 72 kg

#### Output:
#### - BMI: 23.0 (Normal Weight, displayed with a green background)

![example1.png](images%2Fexample1.png)

### Example 2 (Standard System)
#### Input:

#### - Height: 6.1 ft
#### - Weight: 171 lbs

#### Output:
#### - BMI: 22.4 (Normal Weight, displayed with a green background)
![example2.png](images%2Fexample2.png)