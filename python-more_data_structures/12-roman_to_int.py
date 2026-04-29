#!/usr/bin/python3

def roman_to_int(roman_string):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total_value = 0

    if roman_string == None:
        return total_value
    else:
    for i in range(len(roman_string)):
        if i +1 <len(roman_string):
            next_value = values[roman_string[i + 1]]
            if current_value > next_value:
                total_value += current_value
            else:
                total_value -= current_value
    return total_value
