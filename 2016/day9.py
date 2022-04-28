#!/usr/bin/pypy3
from download import getInput
day = 9

def part1(inpt):
    for each in inpt.strip().split():
        n = len(each)
        i = 0
        tmp = ""
        while i<n:
            if each[i]!="(":
                tmp += each[i]
                i+=1
            else:
                i+=1
                length = mult = ""
                while each[i]!="x":
                    length += each[i] 
                    i+=1
                i+=1
                while each[i]!=")":
                    mult += each[i] 
                    i+=1
                i+=1
                length, mult = int(length), int(mult)
                tmp += each[i:i+length]*mult
                i+=length
        print("Answer: ", len(tmp), tmp)
                

def parse(each, i, n):
    temp  = 0

    while i<n:
        if each[i]!="(":
            temp += 1
            i+=1
        else:
            i+=1
            leng = mull = ""
            while each[i]!="x":
                leng += each[i] 
                i+=1
            i+=1
            while each[i]!=")":
                mull += each[i] 
                i+=1
            i+=1
            leng, mull = int(leng), int(mull)
            txt = each[i:i+leng]
            #print("text", txt)
            #print("recursing, ")
            temp += parse(txt, 0, len(txt))*mull
            i+=leng
    #print("temp" ,temp)
    return temp


def part2(inpt):
    for each in inpt.strip().split():
        n = len(each)
        i = 0
        tmp = 0
        while i<n:
            if each[i]!="(":
                tmp += 1
                i+=1
            else:
                i+=1
                length = mult = ""
                while each[i]!="x":
                    length += each[i] 
                    i+=1
                i+=1
                while each[i]!=")":
                    mult += each[i] 
                    i+=1
                i+=1
                length, mult = int(length), int(mult)
                txt = each[i:i+length]*mult
                #print("text", txt)
                #print("recursing, ")
                tmp += parse(txt, 0, len(txt))
                i+=length
        print("Answer: ", tmp)
 

part1(getInput(2016,day))
part2(getInput(2016,day))
