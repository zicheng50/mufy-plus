# TODO:
# Create a function called calculate that takes three arguments:
# - A number
# - An operator ("+", "-", "*", or "/")
# - Another number
# The function should return the result of the calculation
def calculate(num1, n, num2):
    if n == "+":
        return num1 + num2
    elif n == "-":
        return num1 - num2
    elif n == "*":
        return num1 * num2
    elif n == "/":
        if num2 == 0:
            return 'error: zero error'
        else:
             return num1/num2
    else:
        return ("Invalid operator")

# Test the function with different operations
print(calculate(10, "+", 10))  # should return 20
print(calculate(10, "-", 10))  # should return 0
print(calculate(10, "*", 10))  # should return 100
print(calculate(10, "/", 10))  # should return 1.0
print(calculate(10, "^", 10))  # should return "Invalid operator"
print(calculate(10, "/", 0))   # should return 'error: zero error'