#!/usr/bin/pypy3
from download import getInput
from collections import deque
day = 13

def bitCount(x):
    tmp = x
    n = 0
    while tmp != 0:
        tmp = tmp & (tmp-1)
        n += 1
    return n

def isWall(x,y, favNum):
    func = x*x + 3*x + 2*x*y + y + y*y + favNum
    noBits = bitCount(func)

    return noBits % 2

def neighbours(loc):
    x, y = loc
    arr = [(x+1,y), (x,y+1)]
    if x > 0:
        arr.append((x-1,y))
    if y > 0:
        arr.append((x,y-1))
    return arr

def bfs(fav):
    q = deque([(1,1)])
    n = 0
    while q:
        n += 1
        for _ in range(len(q)):
            each = q.popleft()
            for (x,y) in neighbours(each):
                if (x, y) == (31,39): 
                #if (x, y) == (7,4): 
                    return n
                if not isWall(x,y,fav):
                    q.append((x,y))
        print(n)
    return n

def part1(inpt):
    fav = int(inpt)
    #print(bitCount(7))
    #print("\n".join(["".join(["#" if isWall(x,y, fav) else "." for x in range(50)]) for y in range(25)]))
    print(bfs(fav))
    pass

def part2(inpt):
    pass


part1(getInput(2016,day))
part2(getInput(2016,day))
