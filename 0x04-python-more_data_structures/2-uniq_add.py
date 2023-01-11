#!/usr/bin/python3
def uniq_add(my_list=[]):
    answer = 0
    for i in set(my_list):
        answer = answer + i
    return (answer)
