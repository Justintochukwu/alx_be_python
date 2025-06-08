def perform_operation(num1, num2, operation):
    if operation == "add" or operation == "+":
        return num1 + num2
    elif operation == "subtract" or operation == "-":
        return num1 - num2
    elif operation == "multiply" or operation == "*":
        return num1 * num2
    elif operation == "divide" or operation == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2 
    else:
        return "Error: Invalid operation"
