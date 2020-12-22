# Starts with jolt rating of 0
# Ends with jolt rating of highest_rating + 3

def get_adapters():
    adapters = []
    with open("input.txt", "rt") as ratings:
        for line in ratings:
            adapters.append(int(line.strip()))
    return adapters


def count_diffs(chain):
    one_diffs = 1
    three_diffs = 1
    for i in range(0, len(chain)-1):
        diff = chain[i+1] - chain[i]
        if diff == 1:
            one_diffs += 1
        else:
            three_diffs += 1
    print(one_diffs, three_diffs)
    print(one_diffs * three_diffs)

    

def part_one():
    ratings = get_adapters()
    ratings.sort()
    print(ratings)
    count_diffs(ratings)
    

part_one()
