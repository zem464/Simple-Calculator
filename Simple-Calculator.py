# Define the operations to be used
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

# Print intro or greetings
print("SIMPLE CALCULATOR")

# Ask how many numbers are to be calculated
print("**Note that this calculator can only except at least 3 inputs.\n")
num = input("How many numbers will you input?: ")

# For 2 inputs
if num == '2':
    # Show operations
    print("\nIn selecting operations, pick a number.")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
        
    # Use while loop
    while True:
        # Take the operations to be used by the users
        operations = input("\nOperation: ")
        
        # Check the input 
        if operations in ('1', '2', '3', '4'):
            # Use try-except handling
            try:
                inp_num1 = float(input("Enter number: "))
                inp_num2 = float(input("Enter another number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            # If addition
            if operations == '1':
                print(inp_num1, "+", inp_num2, "=", add(inp_num1, inp_num2))
            
            # If subtraction
            elif operations == '2':
                print(inp_num1, "-", inp_num2, "=", subtract(inp_num1, inp_num2))

            # If multiplication
            elif operations == '3':
                print(inp_num1, "*", inp_num2, "=", multiply(inp_num1, inp_num2))

            # If division
            elif operations == '4':
                print(inp_num1, "/", inp_num2, "=", divide(inp_num1, inp_num2))
            
            # Then ask for more calculations

            # Continue if there are more calculations

        # If input is invalid

# For 3 inputs

# Show operations

# Use while loop

# Take the operations to be used by the users

# Check the input

# use try-except handling

# If both addition

# If addition and subtraction

# If addition and multiplication

# If addition and division

# If subtraction and addition
            
# If both subtraction

# If subtraction and multiplication
            
# If multiplication and addition
            
# If multiplication and subtraction

# If both multiplication

# If multiplication and division
            
# If division and addition
            
# If division and subtraction

# If division and multiplication
            
# If both division

# Then ask for more calculations

# Break if no other calculations

# If input is invalid

# Give choices, if input is not in the choices