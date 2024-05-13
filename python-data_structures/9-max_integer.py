#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return None
    max_value = my_list[0]
    for num in my_list[1:]:  # Start from the second element
        if num > max_value:
            max_value = num
    return max_value


if __name__ == "__main__":
    # Test code
    my_list = [1, 90, 2, 13, 34, 5, -13, 3]
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
