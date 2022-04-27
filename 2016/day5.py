#!/usr/bin/python3
from download import getInput
from hashlib import md5

import hasher
assert hasher.greet("world") == "Hello, world!"
assert hasher.greet(name="world") == "Hello, world!"

day = 5

def part1(inpt):
    print("Answer: ", hasher.partOne(inpt))

def part2(inpt):
    print("Answer: ", hasher.partTwo(inpt))



part1(getInput(2016,day).strip())
part2(getInput(2016,day).strip())
