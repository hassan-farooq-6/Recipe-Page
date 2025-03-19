# bad_code.py
def divide_numbers(a, b):
    return a / b  # Potential division by zero error

result = divide_numbers(10, 0)  # This will cause a runtime error
print(result)