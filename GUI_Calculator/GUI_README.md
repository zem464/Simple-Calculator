# Simple OOP Calculator

A modern, graphical calculator built with Python and `customtkinter`. This project demonstrates core software engineering principles by strictly separating the underlying mathematical logic from the visual user interface.

## Features

* **Modular Architecture:** Frontend UI and backend calculation logic are isolated in separate files for high maintainability and code reusability.
* **Continuous Evaluation:** Supports chaining multiple operations dynamically (e.g., computing `1 + 2 + 3` seamlessly).
* **Multi-line Display:** Features an intuitive screen that tracks the active equation history alongside the current user input.
* **Robust Error Handling:** Safely catches and manages edge cases, such as division by zero, preventing application crashes.
* **Modern GUI:** Utilizes CustomTkinter for a clean, responsive, and dark-mode compatible interface.

## Repository Structure

```text
Simple_Calculator/
├── calcu_main.py                # Application entry point
├── calcu_backend.py   # Pure backend logic (mathematical operations)
└── calcu_ui.py       # Frontend GUI and state management
```

## Installation and Setup

1. **Prerequisites:** Ensure you have a Python 3.x installed on your system.

2. **Clone the Repository:** Download or clone the project file into a local directory.

3. **Install Dependencies:** This project will require you to install `customtkinter` library. Install it via pip:

```pip install customtkinter```