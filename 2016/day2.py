#!/usr/bin/pypy3
from download import getInput

def part1(inpt):
    keypad = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    pos = [0,0]
    tmp = ""

    for char in inpt:
        last = pos
        print(pos, char)
        if char=="R":
            if pos[1]+1<2: pos[1] += 1
        elif char=="L":
            if pos[1]-1>-2: pos[1] -= 1
        elif char=="U":
            if pos[0]+1<2: pos[0] += 1
        elif char=="D":
            if pos[0]-1>-2: pos[0] -= 1
        elif char=="\n":
            ans = str( keypad[ -pos[0]+1 ][ pos[1]+1 ] )
            tmp += ans
            print(ans)
        else:
            raise "ValueError"

    ans = str( keypad[ -pos[0]+1 ][ pos[1]+1 ] )
    tmp += ans
    print(ans)

    print("Answer: ", tmp)
        

def part2(inpt):
    keypad = {
        (2,2): "1", (1,1): "2",
        (1,2): "3", (1,3): "4",
        (0,0): "5", (0,1): "6",
        (0,2): "7", (0,3): "8",
        (0,4): "9", (-1,1):"A",
        (-1,2):"B", (-1,3):"C",
        (-2,2):"D"
    }
    pos = [0,0]
    tmp = ""

    for char in inpt:
        last = pos
        print(keypad[tuple(pos)], char)
        if char=="R":
            if (pos[0], pos[1]+1) in keypad: pos[1] += 1
        elif char=="L":
            if (pos[0], pos[1]-1) in keypad: pos[1] -= 1
        elif char=="U":
            if (pos[0]+1, pos[1]) in keypad: pos[0] += 1
        elif char=="D":
            if (pos[0]-1, pos[1]) in keypad: pos[0] -= 1
        elif char=="\n":
            tmp += keypad[tuple(pos)]
        else:
            raise "ValueError"

    ans = keypad[tuple(pos)]
    tmp += ans
    print(ans)

    print("Answer: ", tmp)


part1(getInput(2016,2).rstrip())
part2(getInput(2016,2).rstrip())
