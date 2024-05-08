#!/usr/bin/python3
def to_uppercase(str):
    result = ''
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))


if __name__ == '__main__':
    to_uppercase = __import__('8-uppercase').to_uppercase
    to_uppercase('holberton')
    to_uppercase('Best School 98 Battery street')
