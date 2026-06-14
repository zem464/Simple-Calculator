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
        self.full_equation = "" 
        
        self.setup_ui()
    
    def setup_ui(self):
        # Display Screen - CHANGED to CTkTextbox
        self.display = ctk.CTkTextbox(self, font=("Arial", 28), height=85, wrap="word")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")
        self.display.configure(state="disabled")  # Make display read-only

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
                self, text=text, font=("Arial", 20), width=70, height=70,
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, padx=5, pady=5)

    # Button Click Handlers
    def on_button_click(self, char):

        if char in '0123456789':    # Valid numbers 
            if "\n=" in self.display.get("1.0", "end-1c"):  
                # If the last operation was a calculation, reset for new input
                self.current_input = char
                self.full_equation = char
            else:
                self.current_input += char
                self.full_equation += char
            
            # FIXED: Display the full equation, not just the current input
            self.update_display(self.full_equation)

        elif char in '+-*/':        # Valid characters for operators
            if self.current_input:
                
                # Check if we are chaining operations (a first number and operator already exist)
                if self.first_number is not None and self.operator:
                    # Calculate the intermediate result behind the scenes
                    second_number = float(self.current_input)
                    intermediate_result = self.engine.process_calculation(
                        self.first_number, second_number, self.operator
                    )
                    # The intermediate result becomes the new first number
                    self.first_number = intermediate_result
                else:
                    # This is the first operator pressed in the equation
                    self.first_number = float(self.current_input)
                
                # Save the new operator and update the display
                self.operator = char
                self.full_equation += f" {char} "
                self.current_input = ""
                self.update_display(self.full_equation)
        
        elif char == '=':           # Calculate the result
            if self.first_number is not None and self.operator and self.current_input:
                second_number = float(self.current_input)
                
                # Fetch result from engine
                result = self.engine.process_calculation(
                    self.first_number, second_number, self.operator
                )
                
                # FIXED: Append result to the next line of the equation
                self.full_equation += f"\n= {result}"
                self.update_display(self.full_equation)
                
                # Reset state after calculation
                self.first_number = None
                self.operator = None
                self.current_input = str(result) if "Error" not in str(result) else ""
                # Do NOT reset full_equation here, let the user see it until they type again

        elif char == 'C':           # Clear the display and reset state
            self.current_input = ""
            self.first_number = None
            self.operator = None
            self.full_equation = ""
            self.update_display("")

    # Display update method
    def update_display(self, text):
        self.display.configure(state="normal")  # Enable editing to update display
        self.display.delete("1.0", "end")
        self.display.insert("1.0", text)

        # Align text to the right
        self.display.tag_config("right", justify="right")
        self.display.tag_add("right", "1.0", "end")
        
        self.display.configure(state="disabled") # Lock it back up