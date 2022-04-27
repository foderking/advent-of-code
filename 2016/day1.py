#!/usr/bin/pypy3
from download import getInput

def scale(axis, value):
    return [each*value for each in axis]

def add(axis, position):
    return [sum(each) for each in zip(axis, position)]

def shiftr(axis):
    if axis[0]: return axis[::-1]
    else: return scale(axis[::-1], -1)

def shiftl(axis):
    if axis[-1]: return axis[::-1]
    else: return scale(axis[::-1], -1)

def addLocations(prevPos, nextPos, tmp):
    if prevPos[0]==nextPos[0]:
        for each in range(min(prevPos[1],nextPos[1]), max(prevPos[1],nextPos[1])+1):
            if each==prevPos[1]: continue
            current = (prevPos[0],each)
            if current not in tmp: tmp.append(current)
            else: return (True, current)
    elif prevPos[1]==nextPos[1]:
        for each in range(min(prevPos[0],nextPos[0]), max(prevPos[0],nextPos[0])+1):
            if each==prevPos[0]: continue
            current = (each, prevPos[1])
            if current not in tmp: tmp.append(current)
            else: return (True, current)
    else:
        raise "LocationError"
    return (False, nextPos)

def main(inpt):
    pos = [0, 0]
    axis = [0, 1]

    for dirc in inpt.split(", "):
        val = int(dirc[1:])
        print(axis, dirc,val)

        if dirc[0]=="R":
            pos = add(pos, scale(axis,val))
            axis = shiftr(axis)
        elif dirc[0]=="L":
            laxis = scale(axis,-1)
            pos = add(pos, scale(laxis,val))
            axis = scale(shiftl(laxis), -1)
            pass
        else:
            raise "InputError"
        print(pos)
    print("Answer: ", sum(map(abs, pos)))

def main2(inpt):
    tmp = []
    pos = [0, 0]
    axis = [0, 1]

    for dirc in inpt.split(", "):
        val = int(dirc[1:])
        #print(tmp)
        print(axis, dirc,val)

        if dirc[0]=="R":
            next_pos = add(pos, scale(axis,val))
            axis = shiftr(axis)

            found, pos = addLocations(pos, next_pos, tmp)
            print(found, pos)
            if found: break


        elif dirc[0]=="L":
            laxis = scale(axis,-1)
            next_pos = add(pos, scale(laxis,val))
            axis = scale(shiftl(laxis), -1)

            found, pos = addLocations(pos, next_pos, tmp)
            print(found, pos)
            if found: break
        else:
            raise "InputError"
    print("Answer: ", sum(map(abs, pos)))


main(getInput(2016, 1))
main2(getInput(2016, 1))
