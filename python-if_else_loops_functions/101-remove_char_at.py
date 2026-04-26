#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    if n >= 0 and n < len(str):
        for i in range(len(str)):
            if i != n:
                result += str[i]
        return result
    else:
        return str
