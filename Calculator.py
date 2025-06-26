from colorama import Fore, Style, init

init()

def calc(expression):
    expression = expression.lower()
    expression = expression.replace("plus", "+")
    expression = expression.replace("minus", "-")
    expression = expression.replace("multiply", "*")
    expression = expression.replace("divide", "/")

    tokens = expression.split()
    if len(tokens) != 3:
        print(Fore.RED + "Invalid format. Use: number operation number." + Style.RESET_ALL)
        return None

    try:
        a = float(tokens[0])
        b = float(tokens[2])

    except Exception:
        print(Fore.RED + "Invalid numbers." + Style.RESET_ALL)

    op = tokens[1]

    match op:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                print(Fore.RED + "Cannot be divided by zero." + Style.RESET_ALL)
                return None
            return a / b
        case _:
            print(Fore.RED + "Invalid operation." + Style.RESET_ALL)
            return None