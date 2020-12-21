def get_numbers():
    numbers = []
    with open("input.txt", "rt") as number_file:
        for line in number_file:
            numbers.append(int(line.strip()))
    return numbers


""" Check current number is sum of previous n numbers """

def validate_num(number, last_nums):
    for i in range(0, len(last_nums)):
        valid = False
        for j in range(i+1, len(last_nums)):
            if (last_nums[i] + last_nums[j]) == number:
                valid = True
                break
        if valid:
            return False
    print(number, "is NOT VALID!")
    return True


def get_prev_nums(numbers, preamble, start):
    last_index = start - preamble
    prev_nums = numbers[last_index : start]
    return prev_nums


def get_contiguous_set(target, numbers):
    for i in range(0, len(numbers)):
        total = numbers[i]
        for j in range(i+1, len(numbers)):
            total += numbers[j]
            if total == target:
                return numbers[i : j+1]
            if total > target:
                break


def part_one():
    numbers = get_numbers()
    preamble = 25
    curr_pos = preamble
    found = False
    for n in range(curr_pos, len(numbers)):
        prev_nums = get_prev_nums(numbers, preamble, curr_pos)
        found = validate_num(numbers[n], prev_nums)
        if found:
            break
        curr_pos += 1


""" Tests that contiguous set adds to target """

def test_set(test_set, target):
    count = 0
    for num in test_set:
        count += num
    print(target - count)


def part_two():
    numbers = get_numbers()
    preamble = 25
    curr_pos = preamble
    target = 27911108 # From part 1
    target_set = get_contiguous_set(target, numbers)
    target_set.sort() # Sort in ascending order
    print(target_set)
    #test_set(target_set, target)
    print(target_set[0] + target_set[len(target_set)-1])


part_one()
part_two()
