class Calculator:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def operate(self, operation):
        if operation == 'add':
            return self.a + self.b
        elif operation == 'subtract':
            return self.a - self.b
        elif operation == 'multiply':
            return self.a * self.b
        elif operation == 'divide':
            return self.a / self.b if self.b != 0 else "Division by zero error"
        else:
            return "Invalid operation"

# Example usage:
calc = Calculator(10, 5)
print(calc.operate('multiply'))  # Output: 50.0
