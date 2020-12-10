# 1-3 a: password policy; letter a must appear at least 1, at most 3 times
import re

count_regex = "^\d{1,2}-\d{1,2}" # Limits digits separated by -
char_regex = "[a-zA-Z]:" # Letter for validation ends with colon
pw_regex = "[a-zA-Z]{2,}" # Passwords are sequences of at least two alphabet letters

valid = 0

with open("input_2.txt", "rt") as passwords:
    for line in passwords.readlines():
        limits = re.findall(count_regex, line)
        char = re.findall(char_regex, line)[0].strip(":")
        pw = re.findall(pw_regex, line)[0]
        limits = limits[0].split("-")
        minimum = int(limits[0])
        maximum = int(limits[1])
        count = 0
        for c in pw:
            if c == char:
                count += 1
        if count >= minimum and count <= maximum:
            valid += 1

print("Valid: ", valid)
        
        
