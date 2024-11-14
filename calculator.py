def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
        "+" : add,
        "-" : subtract,
        "*" : multiply,
        "/" : divide
    }
def calculator():
    print("Welcome to my firstCalculatorApp")
    num1= float(input("Type your first number: "))
    x = True
    while x:
        for value in operations:
            print(value)
        operation_symbol = input("Choose your mathematical operator: ")
        num2 = float(input("Type your second number?: "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ").lower()

        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            x = False
            print("\n" * 20)
            calculator()

calculator()

