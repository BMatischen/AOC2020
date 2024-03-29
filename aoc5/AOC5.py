"""FBFBBFF RLR - first 7 specify seat num (0-127), F or B
    - first: F means 0-63 
    - second B means 32-63
    - third F means 32-47

lb = 0, ub = 127
FOR 7 letters:
    diff = ub-lb
    if F, ub = diff/2 if diff even, (diff+1)/2 if diff odd
    if B, lb = diff/2 if diff even, lb = lb + (diff+1)/2 if diff odd

Last three either L or R for columns (0-7)
lb = 0, ub = 7
diff = ub-lb
if L, ub = ub - diff/2 if diff even, ub = ub - (diff+1)/2 if diff odd
if R, lb = lb + diff/2 if diff even, lb = lb + (diff+1)/2 if diff odd
"""


import re

def get_passes():
    pass_list = []
    with open("passes.txt", "r") as passes:
        for line in passes:
            pass_list.append(line.strip())
    return pass_list


"""Get row using first 7 chars (F or B)"""


def calc_seat_row(row_str):
    lb = 0  # Lower bound on seat row
    ub = 127  # Upper bound on seat row
    at_end = True
    for i in range(0, 6):
        char = row_str[i]

        if char == 'F':
            if (ub - lb) % 2 > 0:
                ub = ub - (ub - lb + 1)/2
            else:
                ub = ub - (ub - lb)/2
        else:
            at_end = True
            if (ub - lb) % 2 > 0:
                lb = lb + (ub - lb + 1)/2
            else:
                lb = lb + (ub - lb)/2

    i += 1
    row = lb if row_str[i] == 'F' else ub
    return row


"""Get col using last 3 chars (R or L)"""


def calc_seat_col(col_str):
    lb = 0  # Lower bound on seat col
    ub = 7  # Upper bound on seat col
    for i in range(0, 2):
        char = col_str[i]

        if char == 'L':
            if (ub - lb) % 2 > 0:
                ub = ub - (ub - lb + 1)/2
            else:
                ub = ub - (ub - lb)/2
        else:
            if (ub - lb) % 2 > 0:
                lb = lb + (ub - lb + 1)/2
            else:
                lb = lb + (ub - lb)/2

    i += 1
    col = lb if col_str[i] == 'L' else ub
    return col


def get_seat_id(curr_pass):
    row = calc_seat_row(curr_pass[0:7])
    col = calc_seat_col(curr_pass[7:len(curr_pass)])
    pass_id = (8 * row) + col
    return pass_id


def part_one():
    passes = get_passes()
    max_id = -1
    for p in passes:
        curr_id = get_seat_id(p)
        if max_id < curr_id:
            max_id = curr_id

    print("Max:", max_id)


def next_seat_missing(curr_id, next_id):
    expected_id = curr_id + 1
    if expected_id != next_id:
        return True
    return False
    
        

def part_two():
    passes = get_passes()
    seats = []
    at_front_regex = "F{7}"
    at_back_regex = "B{7}"
    very_front = []
    very_back = []
    for p in passes:
        seats.append(get_seat_id(p))
    seats.sort()
    missing_list = []
    for i in range(0, len(seats)-1):
        if next_seat_missing(seats[i], seats[i+1]):
            missing_list.append(seats[i]+1)
    print(missing_list)


def main():
    #part_one()
    part_two()


at_ends = []
if __name__ == '__main__':
    main()

