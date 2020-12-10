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
    for j in numbers:
        sub_target = target - j
        if target_found:
            break
        elif sub_target < 0:
            continue
        else:
            for k in numbers:
                if k == sub_target:
                    target_found = True
                    print(i * j * k)
                    break


