#!/usr/bin/python3

# Program idea code
"""
Concept:
Divide number by 4 to see how many times the place list values can be incremented until recieving an error
Each iteration the current char will be removed from the string
Check if there are any remaining characters in the string, if so then add them to a new list value
"""


def split_password(password: str):
    count = len(password)
    amount_of_iterations = count // 4
    split_result = []
    string_to_append = ""

    for i in range(0, amount_of_iterations):
        limit_counter = 0
        for char in password:
            if limit_counter != 4:
                string_to_append += char
                password = password.replace(char, "")
                limit_counter += 1
                if len(string_to_append) == 4:
                    split_result.append(string_to_append)
            else:
                string_to_append = ""
                continue

    if password != "":
        string_to_append = ""
        for remaining_char in password:
            string_to_append += remaining_char
        split_result.append(string_to_append)
    return split_result
