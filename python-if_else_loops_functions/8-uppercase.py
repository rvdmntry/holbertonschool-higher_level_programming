#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))


if __name__ == '__main__':
    uppercase = __import__('8-uppercase').uppercase
    uppercase('holberton')
    uppercase('Best School 98 Battery street')
