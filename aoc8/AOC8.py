import re
import time


def get_instructions():
    lines = []
    with open("input.txt", "rt") as instructs:
        for l in instructs:
            lines.append(l.strip())
    return lines


def update_acc(instr):
    op = re.findall("[+-]", instr)[0]
    num = int(re.findall("\d{1,}", instr)[0])
    global acc
    if op == "+":
        acc += num
    else:
        acc -= num


def get_jump_offset(instr):
    op = re.findall("[+-]", instr)[0]
    num = int(re.findall("\d{1,}", instr)[0])
    if op == "+":
        return num
    else:
        return -num


def run_program(instr_list):
    executed = []
    i = 0
    while i < len(instr_list):
        print(i, instr_list[i])
        print("ACC: ", acc, "\n")
        if i in executed:
            print("REPEATED!")
            print("ACC before repeat: ", acc)
            break
        else:
            executed.append(i)

        if re.search("nop", instr_list[i]):
            i += 1
        elif re.search("acc", instr_list[i]):
            update_acc(instr_list[i])
            i += 1
        else:
            i += get_jump_offset(instr_list[i])
    print("Final ACC:", acc)


def part_one():
    instructs = get_instructions()
    print(instructs)
    run_program(instructs)


def main():
    part_one()


if __name__ == "__main__":
    global acc
    acc = 0
    main()
