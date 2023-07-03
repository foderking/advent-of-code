#!/usr/bin/pypy3
from download import getInput
from pprint import pprint
from copy import deepcopy
import sys
sys.setrecursionlimit(100000)
day = 11

states = {}

def getStr(elev):
    return "\n".join(["|".join([i.ljust(2) for i in each]) for each in elev])

def getMoves(pos, elev, mem, n):
    global states
    INF = float("inf")
    curr_state = getStr(elev)
    print("\n"+curr_state)
    # base case
    if not list(filter(lambda x: x==".", elev[0][2:])):
        print("Got to top of elevator")
        print(curr_state)
        return 0
    # memoization
    if curr_state in mem:
        print("state memoized with val", mem[curr_state])
        return mem[curr_state]
    # pruning
    for each in elev[pos][2:]:
        if each==".": continue
        if each[1]=="M":
            gens = list(filter(lambda x:x!="." and x[1]=="G", elev[pos][2:]))
            if gens and each[0]+"G" not in gens:
                print("no generator for", each, "with", "at",elev[pos][2:], gens)
                mem[curr_state] = INF
                return mem[curr_state]
            elif gens:
                print("generator found for", each, "in", gens)
    # get all moves
    movable = list(filter(lambda x: x[1]!=".", enumerate(elev[pos][2:])))
    min_moves = INF

    
    for i in range(len(movable)):
        ind_i = movable[i][0]
        first = movable[i][1]
 
        # go up
        print()
        print()
        if pos-1>=0:
            tmp_elev = deepcopy(elev)
            tmp_elev[pos][1]="."
            tmp_elev[pos-1][1]="E"

            tmp_elev[pos][2+ind_i]="."
            tmp_elev[pos-1][2+ind_i]=first

           # two at a time
            for j in range(i+1, len(movable)):
                ind_j  = movable[j][0]
                second = movable[j][1]

                tmp_elev[pos][2+ind_j]="."
                tmp_elev[pos-1][2+ind_j]=second

                tmp_state = getStr(tmp_elev)
                print("move", first, "and", second, "up from pos", -pos+n)

                
                if tmp_state in states:
                    print("duplicate move", first, "up at and",second, -pos+n)
                    print(tmp_state)
                    print("min moves: ", min_moves)
                else:
                    states[tmp_state] = 1
                    ans = getMoves(pos-1, tmp_elev, mem, n)+1
                    states.pop(tmp_state)
                    min_moves = min(min_moves, ans)
                    print("got", ans, "up from pos", -pos+n,"with", first, "and", second)
                    print("min moves", min_moves)
                # undo last move
                tmp_elev[pos][2+ind_j]=second
                tmp_elev[pos-1][2+ind_j]="."

            # one at a time
            tmp_state = getStr(tmp_elev)
            print("move", first, "up from pos", -pos+n)

            if tmp_state in states:
                print("duplicate move", first, "up at", -pos+n)
                print(tmp_state)
                print("min moves: ", min_moves)
            else:
                states[tmp_state] = 1
                ans = getMoves(pos-1, tmp_elev, mem, n)+1
                states.pop(tmp_state)
                min_moves = min(min_moves, ans)
                print("got", ans, "up from pos", -pos+n, "with", first)
                print("min moves", min_moves)

 
    for i in range(len(movable)):
        ind_i = movable[i][0]
        first = movable[i][1]

        # go down
        if pos+1<n:
            tmp_elev = deepcopy(elev)
            tmp_elev[pos][1]="."
            tmp_elev[pos+1][1]="E"

            tmp_elev[pos][2+ind_i]="."
            tmp_elev[pos+1][2+ind_i]=first

            # one at a time
            tmp_state = getStr(tmp_elev)
            print("move", first, "down from pos", -pos+n)

            if tmp_state in states:
                print("duplicate move", first, "down at", -pos+n)
                print(tmp_state)
                print("min moves: ", min_moves)
            else:
                states[tmp_state] = 1
                ans = getMoves(pos+1, tmp_elev, mem, n)+1
                states.pop(tmp_state)
                min_moves = min(min_moves, ans)
                print("got", ans, "down from pos", -pos+n, "with", first)
                print("min moves", min_moves)

            # two at a time
            for j in range(i+1, len(movable)):
                ind_j  = movable[j][0]
                second = movable[j][1]

                tmp_elev[pos][2+ind_j]="."
                tmp_elev[pos+1][2+ind_j]=second

                tmp_state = getStr(tmp_elev)
                print("move", first, "and", second, "down from pos", -pos+n)

                if tmp_state in states:
                    print("duplicate move", first, "down at and",second, -pos+n)
                    print(tmp_state)
                    print("min moves: ", min_moves)
                else:
                    states[tmp_state] = 1
                    ans = getMoves(pos+1, tmp_elev, mem, n)+1
                    states.pop(tmp_state)
                    min_moves = min(min_moves, ans)
                    print("got", ans, "down from pos", -pos+n,"with", first, "and", second)
                    print("min moves", min_moves)
                # undo last move
                tmp_elev[pos][2+ind_j]=second
                tmp_elev[pos+1][2+ind_j]="."


    mem[curr_state] = min_moves
    print("minimum moves", mem[curr_state])
    return mem[curr_state]

def part1(inpt):
    elev = [list(filter(lambda x: x, each.split(" "))) for each in inpt.strip().split("\n")]
    mem = {}
    n = len(elev)
    #solve(n-1, elev, 0, mem, n)
    print("Answer: ", getMoves(n-1,elev,mem, n))

    print("All", len(mem.values()), "moves")
    for key, value in mem.items():
        print(key)
        print("moves", value)

def part2(inpt):
    pass


part1(getInput(2016,day))
part2(getInput(2016,day))
