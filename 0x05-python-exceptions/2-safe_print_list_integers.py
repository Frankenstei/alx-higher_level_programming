#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    no_of_elements = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            no_of_elements = no_of_elements + 1
        except (ValueError, IndexError, TypeError):
            pass
    print("")
    return (no_of_elements)
