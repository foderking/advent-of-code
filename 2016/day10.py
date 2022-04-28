#!/usr/bin/pypy3
from download import getInput
from pprint import pprint
import sys

#sys.setrecursionlimit(100)
day = 10

def parse(inpt):
    data = {}
    for each in inpt.strip().split("\n"):
        if "value"==each[:5]:
            bot = each.split(" goes to bot ")[1]
            val = each.split(" goes to bot ")[0][6:]

            c_bot = data.get(bot, [[], [],[]])
            c_bot[0].append(int(val))
            data[bot] = c_bot

        else:
            bot = each.split(" gives low to ")[0][4:]

            if "low to output" in each:
                print(each)
                low = int(each.split(" gives low to ")[1].split(" and ")[0][7:])
                print("low output", low)
            else:
                low = each.split(" gives low to ")[1].split(" and ")[0][4:]

            if "high to output" in each:
                print(each)
                high = int(each.split(" gives low to ")[1].split(" and ")[1].split("output ")[1])
                print("high output", high)
            else:
                high = each.split(" gives low to ")[1].split(" and ")[1].split("bot ")[1]

            c_bot = data.get(bot, [[],[],[]])
            c_bot[1].append(low)
            c_bot[1].append(high)
            
            if isinstance(low, str):
                l_bot = data.get(low, [[],[],[]])
                l_bot[0].append(bot)
                data[low] = l_bot
            if isinstance(high, str):
                h_bot = data.get(high, [[],[],[]])
                h_bot[0].append(bot)
                data[high] = h_bot

            data[bot] = c_bot
    return data

def solve(givers, bot, data):
    ans = []
    print("parents: ", givers, "child: ", bot)
    for each in givers:
        if isinstance(each, int): ans.append(each)

        elif not data[each][2]:
            data[each][2] = solve(data[each][0], each, data)

            val = min(data[each][2]) if data[each][1][0]==bot else max(data[each][2])
            ans.append(val)
        else:
            val = min(data[each][2]) if data[each][1][0]==bot else max(data[each][2])
            ans.append(val)
    print("finally", bot, "is", ans)
    return ans

def traverse(data):
    for key, value in data.items():
        if not value[2]:
            data[key][2] = solve(value[0], key, data)
            print(data[key][2])

def part1(inpt):

    bots = parse(inpt)
    traverse(bots)
    print("Part 1")
    for key, [a,b,c] in bots.items():
        if sorted(c)==[17,61]:
            print("Answer: ", key)
    print("Part 2")
    count = 1

    for key, [a,b,c] in bots.items():
        if 0 in b:
            count *= min(c)
            print(b, c, key)
        if 1 in b:
            count *= min(c)
            print(b, c, key)
        if 2 in b:
            count *= min(c)
            print(b, c, key)

    print("Answer: ", count)   

part1(getInput(2016,day))
