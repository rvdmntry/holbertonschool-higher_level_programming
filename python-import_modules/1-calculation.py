#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def main(a, b):
    # Calculate all operations
    operations = [
        f"{a} + {b} = {add(a, b)}",
        f"{a} - {b} = {sub(a, b)}",
        f"{a} * {b} = {mul(a, b)}",
        f"{a} / {b} = {div(a, b)}" if b != 0 else f"{a} / {b} = Error"  # Handle division by zero
    ]
    # Use a single print function
    print("\n".join(operations))

if __name__ == "__main__":
    main(10, 5)
