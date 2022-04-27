#!/usr/bin/pypy3
from download import getInput
from collections import Counter
day = 6

def part1(inpt):
    n = len(inpt.split("\n")[0])
    tmp = [Counter() for _ in range(n)]
    for each in inpt.split("\n"):
        for i, char in enumerate(each):
            tmp[i].update(char)

    print(tmp, n)
    print("Answer: ", "".join([each.most_common()[0][0] for each in tmp ]))

def part2(inpt):
    n = len(inpt.split("\n")[0])
    tmp = [Counter() for _ in range(n)]
    for each in inpt.split("\n"):
        for i, char in enumerate(each):
            tmp[i].update(char)

    print(tmp, n)
    print("Answer: ", "".join([sorted(each.items(), key=lambda a: a[1])[0][0] for each in tmp ]))




part1(getInput(2016,day))
part2(getInput(2016,day))
