#!/usr/bin/pypy3
from download import getInput
day = 7

def isabba(string):
    for i in range(2, len(string)):
        if string[i-2:i]==string[i:i+2][::-1] and string[i]!=string[i+1]: return True
    return False

def isaba(string):
    tmp = []
    for i in range(2, len(string)):
        if string[i]==string[i-2] and string[i]!=string[i-1]:
            tmp.append(string[i-2:i+1])
    return tmp

def isValid(string):
    ans = False

    left = string.split("[")[0] 
    if isabba(left): ans = True

    for each in string.split("[")[1:]:
        square, right = each.split("]")

        if isabba(square): return False
        if isabba(right): ans = True

    return ans

def bab(aba):
    return aba[1] + aba[0] + aba[1]

def isSsl(string):
    #print(string)
    babs = []
    left = string.split("[")[0] 
    babs.extend(isaba(left))

    for each in string.split("[")[1:]:
        _, right = each.split("]")
        babs.extend(isaba(right))

    for each in string.split("[")[1:]:
        square, _ = each.split("]")

        #print(babs)
        for aba in babs:
            if bab(aba) in square:
                #print(bab(aba))
                return True

    return False

def part1(inpt):
    count = 0
    for each in inpt.split("\n"):
        count += isValid(each)
        
    print("Answer: ", count)

def part2(inpt):
    count = 0
    for each in inpt.split("\n"):
        an = isSsl(each)
        #print(an)
        count += an
        
    print("Answer: ", count)



part1(getInput(2016,day))
part2(getInput(2016,day))
