# 1-3 a: password policy; two numbers for two positions; letter must appear at precisely one of these indexes
import re

indices_regex = "^\d{1,2}-\d{1,2}" # Limits digits separated by -
char_regex = "[a-zA-Z]:" # Letter for validation ends with colon
pw_regex = "[a-zA-Z]{2,}" # Passwords are sequences of at least two alphabet letters

valid = 0

with open("input_2.txt", "rt") as passwords:
    for line in passwords.readlines():
        indices = re.findall(indices_regex, line)
        char = re.findall(char_regex, line)[0].strip(":")
        pw = re.findall(pw_regex, line)[0]
        indices = indices[0].split("-")
        first_pos = int(indices[0])-1
        last_pos = int(indices[1])-1

        if pw[first_pos] == char and pw[last_pos] != char:
            valid += 1
        elif pw[first_pos] != char and pw[last_pos] == char:
            valid += 1
        else:
            pass

print("Valid: ", valid)
