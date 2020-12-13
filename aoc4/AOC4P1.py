"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.

hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.

hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.

key:value pairs separated with spaces or newlines
"""

#P2: ans < 105

import re

def read_file():
    with open("input_4.bat", "rt") as file:
        contents = file.read().split("\n\n")
        contents = [line.replace("\n", " ") for line in contents]
    return contents


def validate_contents(contents):
    byr_regex = r'byr:19[2-9][0-9]|byr:200[0-2]'
    iyr_regex = r'iyr:201[0-9]|iyr:2020'
    eyr_regex = r'eyr:202[0-9]|eyr:2030'
    hgt_regex = r'hgt:1[5-8][0-9]cm|hgt:19[0-3]cm|hgt:59in|hgt:6[0-9]in|hgt:7[0-6]in'
    hcl_regex = r'hcl:#[\da-f]{6}'
    ecl_regex = r'ecl:amb|ecl:blu|ecl:brn|ecl:gry|ecl:grn|ecl:hzl|ecl:oth'
    pid_regex = r'pid:\d{9}( |$)'

    attributes = []
    valid = 0
    for line in contents:
        attributes.append(re.findall(byr_regex, line))
        attributes.append(re.findall(iyr_regex, line))
        attributes.append(re.findall(eyr_regex, line))
        attributes.append(re.findall(hgt_regex, line))
        attributes.append(re.findall(hcl_regex, line))
        attributes.append(re.findall(ecl_regex, line))
        attributes.append(re.findall(pid_regex, line))
        is_valid = True
        for att in attributes:
            if len(att) < 1:
                is_valid = False
                break
            if 'pid' in att[0] and len(att[0]) > 14:
                print("10 digits!")
        if is_valid:
            valid += 1
        attributes.clear()
    return valid


contents = read_file()
valid = validate_contents(contents)
print(valid)
