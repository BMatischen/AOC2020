numbers = []
with open("input.txt", "rt") as input_handler:
    for n in input_handler.readlines():
        numbers.append(int(n.strip()))
print(numbers)


