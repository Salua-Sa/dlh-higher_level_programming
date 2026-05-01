#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list == []:
        return 0
    total_score_weight = 0
    total_weight = 0

    for i in my_list:
        total_score_weight += i[0] * i[1]
        total_weight += i[1]

    return total_score_weight / total_weight
