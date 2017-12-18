import threading
import time
from collections import defaultdict
from queue import Queue


class Program(threading.Thread):
    def __init__(self, data, prog_i, send_q, rcv_q, result):
        threading.Thread.__init__(self)
        self.data = data
        self.prog_i = prog_i
        self.registers = defaultdict(int)
        self.registers['p'] = prog_i
        self.send_q = send_q
        self.rcv_q = rcv_q
        self.result = result
        self.result[self.prog_i] = 0

    def run(self):
        data = self.data
        registers = self.registers
        i = 0
        while i >= 0 and i < len(data):
            instr = data[i].split()
            if len(instr) > 2:
                try:
                    val = int(instr[2])
                except:
                    val = registers[instr[2]]

            if instr[0] == 'set':
                registers[instr[1]] = val
            elif instr[0] == 'snd':
                try:
                    val = int(instr[1])
                except:
                    val = registers[instr[1]]
                self.send_q.put(val)
                self.result[self.prog_i] += 1

            elif instr[0] == 'add':
                registers[instr[1]] += val
            elif instr[0] == 'mul':
                registers[instr[1]] *= val
            elif instr[0] == 'mod':
                registers[instr[1]] = registers[instr[1]] % val
            elif instr[0] == 'rcv':
                try:
                    registers[instr[1]] = self.rcv_q.get(timeout=5)
                except:
                    print('timeout from thread: ' + str(self.prog_i))
                    break
            elif instr[0] == 'jgz':
                try:
                    val1 = int(instr[1])
                except:
                    val1 = registers[instr[1]]

                if val1 > 0:
                    i += val
                    continue

            i += 1

with open("input.txt", "r") as f:
    data = f.read()[:-1].split('\n')

queue0 = Queue()
queue1 = Queue()
result = {}

prog0 = Program(data, 0, queue0, queue1, result)
prog1 = Program(data, 1, queue1, queue0, result)

prog0.start()
prog1.start()
print('all program started')
prog0.join()
print('prog0 joined!')
prog1.join()
print('prog1 joined!')

print(result)
print(prog0.registers)
print(prog1.registers)
