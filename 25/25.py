from collections import defaultdict


def stateA():
    global tape, cursor
    if tape[cursor] == 0:
        tape[cursor] = 1
        cursor += 1
        return stateB
    elif tape[cursor] == 1:
        tape[cursor] = 0
        cursor += -1
        return stateF


def stateB():
    global tape, cursor
    if tape[cursor] == 0:
        tape[cursor] = 0
        cursor += 1
        return stateC
    elif tape[cursor] == 1:
        tape[cursor] = 0
        cursor += 1
        return stateD


def stateC():
    global tape, cursor
    if tape[cursor] == 0:
        tape[cursor] = 1
        cursor += -1
        return stateD
    elif tape[cursor] == 1:
        tape[cursor] = 1
        cursor += 1
        return stateE


def stateD():
    global tape, cursor
    if tape[cursor] == 0:
        tape[cursor] = 0
        cursor += -1
        return stateE
    elif tape[cursor] == 1:
        tape[cursor] = 0
        cursor += -1
        return stateD


def stateE():
    global tape, cursor
    if tape[cursor] == 0:
        tape[cursor] = 0
        cursor += 1
        return stateA
    elif tape[cursor] == 1:
        tape[cursor] = 1
        cursor += 1
        return stateC


def stateF():
    global tape, cursor
    if tape[cursor] == 0:
        tape[cursor] = 1
        cursor += -1
        return stateA
    elif tape[cursor] == 1:
        tape[cursor] = 1
        cursor += 1
        return stateA


with open("input.txt", "r") as f:
    data = f.read()[:-1].split('\n')

tape = defaultdict(int)
cursor = 0
current_state = stateA

for _ in range(12994925):
    current_state = current_state()

print(tape)
print(sum(tape.values()))
