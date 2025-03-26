from calc_art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+":add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))
    should_accumulate = True

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operator = input("Choose a Mathematical Operator: ")
        num2 = float(input("Choose a second number: "))
        answer = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or Type 'n' to start a new calculation").lower()

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
calculator()