#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Create a copy of the list
    list_copy = my_list[:]
    if 0 <= idx < len(list_copy):
        list_copy[idx] = element
    return list_copy


if __name__ == "__main__":
    # Test code
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9
    new_list = new_in_list(my_list, idx, new_element)

    print(new_list)
    print(my_list)
