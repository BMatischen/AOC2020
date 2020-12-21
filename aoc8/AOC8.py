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
    global acc
    acc = 0
    executed = []
    i = 0
    while i < len(instr_list):
        if i in executed:
            print("ACC before repeat: ", acc)
            return False
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
    return True


def fix_program():
    changed_lines = set({})
    index = 0
    while True:
        instr_list = get_instructions()
        fixed = False
        if index in changed_lines:
            index += 1
        elif index >= len(instr_list):
            print(acc)

        else:
            if "jmp" in instr_list[index]:
                instr_list[index] = re.sub("jmp","nop",instr_list[index])
                changed_lines.add(index)
                fixed = run_program(instr_list)
            elif "nop" in instr_list[index]:
                instr_list[index] = re.sub("nop","jmp",instr_list[index])
                changed_lines.add(index)
                fixed = run_program(instr_list)
            else:
                index += 1
        if fixed:
            break
            

def part_one():
    instructs = get_instructions()
    print(instructs)
    run_program(instructs)


def part_two():
    fix_program()


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
