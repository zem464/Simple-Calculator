# Class file for the calculator backend

# Define the operations to be used
class Calculator:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2
    
    def process_calculation(self, num1, num2, operator):
        """Routes the inputs to the correct mathematical function."""
        if operator == '+':
            return self.add(num1, num2)
        elif operator == '-':
            return self.subtract(num1, num2)
        elif operator == '*':
            return self.multiply(num1, num2)
        elif operator == '/':
            return self.divide(num1, num2)
        else:
            return "Error"