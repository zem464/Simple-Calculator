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
print("==========================================================================")
print("|\033[37;40m                          " + "\033[35;40m\033[1mSIMPLE CALCULATOR\033[0m" + "\033[37;40m                             \033[37m|")
print("==========================================================================" + "\n")

# Ask how many numbers are to be calculated
print("\033[33m**Note that this calculator can only except at least 3 inputs.\n")
num = input("\033[34m\033[1mHow many numbers will you input?: \033[37m\033[0m")

# For 2 inputs
if num == '2':
    # Show operations
    print("\n\033[33;40m\033[1mIn selecting operations, pick a number.\033[0m")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
        
    # Use while loop
    while True:
        # Take the operations to be used by the users
        operations = input("\n\033[34m\033[1mOperation: \033[37m\033[0m")
        
        # Check the input 
        if operations in ('1', '2', '3', '4'):
            # Use try-except handling
            try:
                inp_num1 = float(input("\033[34m\033[1mEnter number: \033[37m\033[0m"))
                inp_num2 = float(input("\033[34m\033[1mEnter another number: \033[37m\033[0m"))
            except ValueError:
                print("\033[31m\033[1mInvalid input. Please enter numbers.")
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
                try:
                    print(inp_num1, "/", inp_num2, "=", divide(inp_num1, inp_num2))
                except ZeroDivisionError:
                    print("\033[31m\033[1mCannot divide by zero")
            
            # Then ask for more calculations
            again = input("\n\033[32m\033[1mMore calculations? Put 'n' if none: \033[37m\033[0m")
            # Continue if there are more calculations
            if again == 'n':
                print("\n\033[35m\033[1mThank you!")
                break

        # If input is invalid
        else:
            print("Invalid input.")

# For 3 inputs
elif num == '3':
    # Show operations
    print("\n\033[33;40m\033[1mIn selecting operations, pick a number.\033[0m")
    print("5. +, +")
    print("6. +, -")
    print("7. +, *")
    print("8. +, /")
    print("9. -, +")
    print("10. -, -")
    print("11. -, *")
    print("12. -, /")
    print("13. *, +")
    print("14. *, -")
    print("15. *, *")
    print("16. *, /")
    print("17. /, +")
    print("18. /, -")
    print("19. /, *")
    print("20. /, /")

    # Use while loop
    while True:
        # Take the operations to be used by the users
        operations = input("\n\033[34m\033[1mOperation: \033[37m\033[0m")

        # Check the input
        if operations in ('5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'):
            # use try-except handling
            try:
                inp_num1 = float(input("\033[34m\033[1mEnter number: \033[37m\033[0m"))
                inp_num2 = float(input("\033[34m\033[1mEnter another number: \033[37m\033[0m"))
                inp_num3 = float(input("\033[34m\033[1mEnter another number: \033[37m\033[0m"))
            except ValueError:
                print("\033[31m\033[1mInvalid input. Please enter numbers.")
                continue

            # If both addition
            if operations == '5':
                print(inp_num1, "+", inp_num2, "+", inp_num3, "=", add(inp_num1, inp_num2) + inp_num3)
            
            # If addition and subtraction
            elif operations == '6':
                print(inp_num1, "+", inp_num2, "-", inp_num3, "=", add(inp_num1, inp_num2) - inp_num3)

            # If addition and multiplication
            elif operations == '7':
                print(inp_num1, "+", inp_num2, "*", inp_num3, "=", add(inp_num1, inp_num2) * inp_num3)

            # If addition and division
            elif operations == '8':
                try:
                    print(inp_num1, "+", inp_num2, "/", inp_num3, "=", add(inp_num1, inp_num2) / inp_num3)
                except ZeroDivisionError:
                    print("\033[31m\033[1mCannot divide by zero")
            
            # If subtraction and addition
            elif operations == '9':
                print(inp_num1, "-", inp_num2, "+", inp_num3, "=", subtract(inp_num1, inp_num2) + inp_num3)
            
            # If both subtraction
            elif operations == '10':
                print(inp_num1, "-", inp_num2, "-", inp_num3, "=", subtract(inp_num1, inp_num2) - inp_num3)

            # If subtraction and multiplication
            elif operations == '11':
                print(inp_num1, "-", inp_num2, "*", inp_num3, "=", subtract(inp_num1, inp_num2) * inp_num3)

            # If subtraction and division
            elif operations == '12':
                try:
                    print(inp_num1, "-", inp_num2, "/", inp_num3, "=", subtract(inp_num1, inp_num2) / inp_num3)
                except ZeroDivisionError:
                    print("\033[31m\033[1mCannot divide by zero")
            
            # If multiplication and addition
            elif operations == '13':
                print(inp_num1, "*", inp_num2, "+", inp_num3, "=", multiply(inp_num1, inp_num2) + inp_num3)
            
            # If multiplication and subtraction
            elif operations == '14':
                print(inp_num1, "*", inp_num2, "-", inp_num3, "=", multiply(inp_num1, inp_num2) - inp_num3)

            # If both multiplication
            elif operations == '15':
                print(inp_num1, "*", inp_num2, "*", inp_num3, "=", multiply(inp_num1, inp_num2) * inp_num3)

            # If multiplication and division
            elif operations == '16':
                try:
                    print(inp_num1, "*", inp_num2, "/", inp_num3, "=", multiply(inp_num1, inp_num2) / inp_num3)
                except ZeroDivisionError:
                    print("\033[31m\033[1mCannot divide by zero")
            
            # If division and addition
            elif operations == '17':
                try:
                    print(inp_num1, "/", inp_num2, "+", inp_num3, "=", divide(inp_num1, inp_num2) + inp_num3)
                except ZeroDivisionError:
                    print("\033[31m\033[1mCannot divide by zero")
            
            # If division and subtraction
            elif operations == '18':
                try:
                    print(inp_num1, "/", inp_num2, "-", inp_num3, "=", divide(inp_num1, inp_num2) - inp_num3)
                except ZeroDivisionError:
                    print("\033[31m\033[1mCannot divide by zero")

            # If division and multiplication
            elif operations == '19':
                try:
                    print(inp_num1, "/", inp_num2, "*", inp_num3, "=", divide(inp_num1, inp_num2) * inp_num3)
                except ZeroDivisionError:
                    print("\033[31m\033[1mCannot divide by zero")

            # If both division
            elif operations == '20':
                try:
                    print(inp_num1, "/", inp_num2, "/", inp_num3, "=", divide(inp_num1, inp_num2) / inp_num3)
                except ZeroDivisionError:
                    print("\033[31m\033[1mCannot divide by zero")

            # Then ask for more calculations
            again = input("\n\033[32m\033[1mMore calculations? Put 'n' if none: \033[37m\033[0m")
            # Break if no other calculations
            if again == 'n':
                print("\n\033[35m\033[1mThank you!")
                break

        # If input is invalid
        else:
            print("\033[31m\033[1mInvalid input.")

# Give choices, if input is not in the choices
else:
    print("\033[31m\033[1mPlease enter 2 or 3 only.")