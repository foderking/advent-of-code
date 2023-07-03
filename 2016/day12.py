#!/usr/bin/pypy3
from download import getInput
day = 12
registers = "abcd"

def getValue(x, mem):
    return mem[x] if x in registers else int(x)

def evaluate(memory, instr, index):
    if instr[0] == "cpy":
        memory[instr[2]] = getValue(instr[1], memory)
        return index + 1
    elif instr[0] == "inc":
        memory[instr[1]] += 1
        return index + 1
    elif instr[0] == "dec":
        memory[instr[1]] -= 1
        return index + 1
    elif instr[0] == "jnz":
        x = getValue(instr[1], memory)
        if x == 0:
            return index + 1
        else:
            return index + int(instr[2])
    else:
        raise "error"

def serializeInput(inp):
    return [each.split(" ") for each in inp.split("\n")]

def part1(inpt):
    mem = {k: 0 for k in registers}
    instructions = serializeInput(inpt)
    n = len(instructions)
    i = 0
    while i < n and i >= 0:
        i = evaluate(mem, instructions[i] , i)
    print(mem)

def part2(inpt):
    mem = {k: 0 for k in registers}
    mem["c"] = 1
    instructions = serializeInput(inpt)
    n = len(instructions)
    i = 0
    while i < n and i >= 0:
        i = evaluate(mem, instructions[i] , i)
    print(mem)


part1(getInput(2016,day))
part2(getInput(2016,day))
