#!/usr/bin/pypy3
from download import getInput

def check(a,b,c):
    return a+b>c and (a+c>b and b+c>a)

def part1(inpt):
    count = 0
    for a, b, c in [filter(lambda a:a, each.split()) for each in inpt.split("\n")]:
        count += check(int(a),int(b),int(c))
        print(a,b,c)
    print("Answer: ", count)

def part2(inpt):
    count = 0
    i = 0
    tmp = [[0,0,0],[0,0,0],[0,0,0]]
    for a, b, c in [filter(lambda a:a, each.split()) for each in inpt.split("\n")]:
        if not i%3:
            #print(tmp)
            count += sum([check(x,y,z) for x,y,z in tmp])

        tmp[0][i%3], tmp[1][i%3], tmp[2][i%3] = int(a), int(b), int(c)
        i += 1
    if not i%3:
        print(tmp)
        count += sum([check(x,y,z) for x,y,z in tmp])
    print("Answer: ", count)




part1(getInput(2016,3))
part2(getInput(2016,3))
