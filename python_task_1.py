def add(x, y):
    """Adds two numbers"""
    return x + y

def subtract(x, y):
    """Subtracts two numbers"""
    return x - y

def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def divide(x, y):
    """Divides two numbers, handling division by zero"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def calculator():
    print("--- Simple Python Calculator ---")
    print("Select an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    # Prompt the user for the operation
    choice = input("\nEnter choice (1/2/3/4): ")

    # Check if the user's choice is one of the valid options
    if choice in ('1', '2', '3', '4'):
        try:
            # Prompt the user for two numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values only.")
            return

        # Perform the calculation and display the result
        if choice == '1':
            print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"\nResult: {num1} / {num2} = {divide(num1, num2)}")
            
    else:
        print("Invalid Input! Please select a valid operation (1-4).")

# Run the calculator
if __name__ == "__main__":
    calculator()