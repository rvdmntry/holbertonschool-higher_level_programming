#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        my_list[:] = my_list[:idx] + my_list[idx+1:]
    return my_list


if __name__ == "__main__":
    # Test code
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_list = delete_at(my_list, idx)
    print(new_list)
    print(my_list)
