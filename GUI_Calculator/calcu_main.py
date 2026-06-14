# Imports
import tkinter
import customtkinter

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("400x500")
app.title("Simple Calculator")

# Run app
app.mainloop()