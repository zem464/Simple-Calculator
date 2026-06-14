# Class file for the calculator backend

import customtkinter as ctk
from calc_backend import Calculator

# The main GUI window, handling all visual elements and user input.
class CalculatorGUI(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("Simple Calculator")
        self.geometry("320x450")
        self.resizable(False, False)
        
        # Instantiate the backend engine
        self.engine = Calculator()
        
        # State variables to track inputs
        self.current_input = ""
        self.first_number = None
        self.operator = None
        
        self.setup_ui()
    
    def setup_ui(self):
        # Display Screen
        self.display = ctk.CTkEntry(self, font=("Arial", 28), justify="right", height=50)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")

        # Button Grid Layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Generate buttons using a loop
        for (text, row, col) in buttons:
            btn = ctk.CTkButton(
                self, text=text, font=("Arial", 20), width=70, height=80,
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

    # Button Click Handlers
    def on_button_click(self, char):

        if char in '0123456789':    # Valid numbers only
            self.current_input += char
            self.update_display(self.current_input)

        elif char in '+-*/':        # Valid characters for operators
            # Save the first number and the operator
            if self.current_input:
                self.first_number = float(self.current_input)
                self.operator = char
                self.current_input = ""
        
        elif char == '=':           # Calculate the result
            if self.first_number is not None and self.operator and self.current_input:
                second_number = float(self.current_input)
                try:
                    result = self.engine.process_calculation(
                        self.first_number, second_number, self.operator
                    )
                    self.update_display(str(result))
                except ZeroDivisionError:
                    self.update_display("Error: Div by 0")
                finally:
                    # Reset state after calculation
                    self.first_number = None
                    self.operator = None
                    self.current_input = ""

        elif char == 'C':           # Clear the display and reset state
            self.current_input = ""
            self.first_number = None
            self.operator = None
            self.update_display("")

    # Display update method
    def update_display(self, text):
        self.display.delete(0, ctk.END)
        self.display.insert(0, text)