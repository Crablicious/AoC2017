import string
from enum import Enum
from math import floor


class Move:
    def do_move(self, l: list) -> list:
        raise NotImplementedError('do_move not implemented')

    def _swap(self, l, pos0, pos1):
        tmp = l[pos0]
        l[pos0] = l[pos1]
        l[pos1] = tmp


class SpinMove(Move):
    def __init__(self, num_spins: int):
        self.num_spins = num_spins

    def do_move(self, l: list) -> list:
        length = len(l)
        return l[length-self.num_spins:] + l[:length-self.num_spins]


class ExchMove(Move):
    def __init__(self, pos0: int, pos1: int):
        self.pos0 = pos0
        self.pos1 = pos1

    def do_move(self, l: list) -> list:
        self._swap(l, self.pos0, self.pos1)
        return l


class PartMove(Move):
    def __init__(self, part0: str, part1: str):
        self.part0 = part0
        self.part1 = part1

    def do_move(self, l: list) -> list:
        pos0 = l.index(self.part0)
        pos1 = l.index(self.part1)
        self._swap(l, pos0, pos1)
        return l


def part_one(line, moves):
    for move in moves:
        line = move.do_move(line)

    print('Part one: ' + ''.join(line))


def part_two(line, moves):
    og_line = line[:]
    loop_num = 0
    for i in range(0, 1000000000):
        for move in moves:
            line = move.do_move(line)
        if og_line == line:
            loop_num = i+1
            break

    start = floor(1000000000/loop_num)*loop_num
    for i in range(start, 1000000000):
        for move in moves:
            line = move.do_move(line)

    print('Part two: ' + ''.join(line))


def main():
    with open("input.txt", "r") as f:
        data = f.read()[:-1].split(',')

    moves = []
    for move in data:
        if move[0] == 's':
            moves.append(SpinMove(int(move[1:])))
        elif move[0] == 'x':
            poses = move[1:].split('/')
            moves.append(ExchMove(int(poses[0]), int(poses[1])))
        elif move[0] == 'p':
            moves.append(PartMove(move[1], move[3]))

    line = list(string.ascii_lowercase)[:16]
    part_one(line[:], moves)
    part_two(line[:], moves)

if __name__ == '__main__':
    main()
