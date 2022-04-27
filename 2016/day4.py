#!/usr/bin/pypy3
from download import getInput
from functools import reduce
from collections import Counter
import re

def part1(inpt):
    count = 0
    for each in inpt.split("\n"):
        tmp = each.split("-")
        valid = reduce(lambda x,y: x+y ,[a for a,_ in Counter(sorted(reduce(lambda a,b: a+b, tmp[:-1]))).most_common(5)])

        checksum_valid = re.match(f"(\d+)\[{valid}\]", tmp[-1])
        if checksum_valid: count+= int(checksum_valid.groups()[0])
        print(tmp, valid)

    print("Answer: ", count)

def shift(string, no):
    return "".join([chr( ord("a")+(ord(char)+no-ord("a"))%26 ) for char in string])

def part2(inpt):
    for each in inpt.split("\n"):
        tmp = each.split("-")
        s, section_id = tmp[:-1], int(tmp[-1].split("[")[0])
        message = [shift(each, section_id) for each in s]
        #print(message)
        print(" ".join(message), section_id)
        if "northpole" in message:
            print("Answer: ", section_id)
            break
        #print(s, section_id)
    pass


part1(getInput(2016,4))
part2(getInput(2016,4))
