import random
import time


def bubble_sort(input_list):
    stages = []
    for i in range(len(input_list) - 1):
        for x in range(len(input_list) - 1):
            y = x + 1
            if input_list[x] > input_list[y]:
                old_y = input_list[y]
                input_list[y] = input_list[x]
                input_list[x] = old_y
                stages.append(input_list.copy())
    return stages


def selection_sort(input_list):
    stages = []
    for i in range(len(input_list)):
        max_val = 0
        for x in range(len(input_list) - i):
            if input_list[max_val] < input_list[x]:
                max_val = x
        old_last = input_list[-(i + 1)]
        input_list[-(i + 1)] = input_list[max_val]
        input_list[max_val] = old_last
        stages.append(input_list.copy())
    return stages


def insertion_sort(input_list):
    stages = []
    for i in range(1, len(input_list)):
        key = input_list[i]
        j = i - 1
        while j >= 0 and key < input_list[j]:
            input_list[j + 1] = input_list[j]
            j -= 1
            stages.append(input_list.copy())
        input_list[j + 1] = key

    return stages+[input_list.copy()]


