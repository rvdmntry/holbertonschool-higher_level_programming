#!/usr/bin/python3

def no_c(my_string):
    # Use list comprehension to filter out 'c' and 'C'
    filtered_string = [char for char in my_string if char not in ['c', 'C']]
    # Join the list back into a string
    return ''.join(filtered_string)


if __name__ == "__main__":
    # Test code
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
