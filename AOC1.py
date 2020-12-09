numbers = []
with open("input.txt", "rt") as input_handler:
    for n in input_handler.readlines():
        numbers.append(int(n.strip()))
#print(numbers)

goal = 2020
target_found = False
for i in numbers:
    if target_found:
        break
    target = goal - i
    print("Current_num: ", i, "Target: ", target, "\n")
    for j in range(len(numbers)):
        if numbers[j] == target:
            target_found = True
            print(i * numbers[j])
            break


