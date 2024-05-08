#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        # Check if the character is lowercase (a-z)
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)  # Convert to uppercase by subtracting 32
        else:
            result += char  # Add the character as it is if it's not a lowercase letter
    print(result)

if __name__ == "__main__":
    uppercase = __import__('8-uppercase').uppercase

    uppercase("best")
    uppercase("Best School 98 Battery street")
