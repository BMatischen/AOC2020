""" 26 questions on form
letters represent a yes to a question
groups separated by blank line
persons answers on one line
abc

a
b
c

ab
ac

a
a
a
a

b

first group(line): 1 per 3 ans
second: 3 per with 1 ans each
third: 2 per with 2 ans each
fourth: 4 per with 1 ans each
fifth: 1 per 1 ans

P1: total sum of yesses to unique questions across groups
P2: total sum of questions that everyone in each group answered yes to
"""
import re


def get_answers():
    answers = []
    with open("forminput.txt", "r") as ans:
        group = []
        lines = ans.readlines()
        for i in range(len(lines)+1):
            if i == len(lines) or lines[i].strip() == '':
                answers.append(group)
                group = []
            else:
                group.append(lines[i].strip())
    return answers


""" Count questions with at least 1 yes """
""" group: Array of strings, letters are yesses to a question """


def count_yesses(group):
    questions = set({})  # Stores question letters with at least one yes
    for person_qs in group:
        for char in person_qs:
            questions.add(char)
    return len(questions)


def count_unanimous(group):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, len(group)):
        for char in alphabet:
            found = re.search(char, group[i])
            if not found:
                alphabet = re.sub(char, "", alphabet)
    return len(alphabet)
    

def part_one():
    count = 0
    answers = get_answers()
    for group in answers:
        count += count_yesses(group)
    print(count)


def part_two():
    count = 0
    answers = get_answers()
    for group in answers:
        count += count_unanimous(group)
    print(count)


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()
