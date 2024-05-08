#!/usr/bin/python3
def upper(str):
    result = ''
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))


if __name__ == '__main__':
    upper = __import__('8-uppercase').upper
    upper('best')
    upper('Best School 98 Battery street')
