#!/usr/bin/python3

def roman_to_int(roman_string):
    int_num = 0
    if roman_string == None:
        return int_num
    else:
        for i in roman_string:
            if i >= i+1:
                if i == "I":
                    int_num += 1
                elif i == "V":
                    int_num += 5
                elif i == "X":
                    int_num += 10
                elif i == "L":
                    int_num += 50
                elif i == "C":
                    int_num += 100
                elif i == "D":
                    int_num += 500
                elif i == "D":
                    int_num += 1000
            else:
                if i == "I":
                    int_num -= 1
                elif i == "V":
                    int_num -= 5
                elif i == "X":
                    int_num -= 10
                elif i == "L":
                    int_num -= 50
                elif i == "C":
                    int_num -= 100
                elif i == "D":
                    int_num -= 500
                elif i == "D":
                    int_num -= 1000
    return int_num
