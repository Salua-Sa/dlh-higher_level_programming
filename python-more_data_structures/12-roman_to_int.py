#!/usr/bin/python3

def roman_to_int(roman_string):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total_value = 0

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    for i in range(len(roman_string)):
        current_value = values[roman_string[i]]
        if i + 1 < len(roman_string):
            next_value = values[roman_string[i + 1]]
            if current_value < next_value:
                total_value -= current_value
            else:
                total_value += current_value
        else:
            total_value += current_value
    return total_value
