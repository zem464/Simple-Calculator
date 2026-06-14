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