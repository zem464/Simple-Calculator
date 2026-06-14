# Imports
from calc_ui import CalculatorGUI

if __name__ == "__main__":
    # Initialize and run the application
    app = CalculatorGUI()
    
    # System appearance and theme settings
    import customtkinter as ctk
    ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    # Run app
    app.mainloop() 