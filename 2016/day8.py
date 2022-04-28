#!/usr/bin/pypy3
from download import getInput
from pprint import pprint
day = 8

def rect(col, row, arr):
    for i in range(int(row)):
        for j in range(int(col)):
            arr[i][j] = "1"

def rotateRow(row, pixel, arr):
    pixel = int(pixel)
    row   = int(row)
    arr[row] = arr[row][-pixel:] + arr[row][:-pixel]

def rotateCol(col, pixel, arr):
    N  = 6
    col = int(col)
    pixel = int(pixel)
    col_arr = [each[col] for each in arr]
    col_arr = col_arr[-pixel:] + col_arr[:-pixel]

    for i, each in enumerate(col_arr):
        arr[i][col] = each

def part1(inpt):
    screen = [["0"]*50 for _ in range(6)]
    for each in inpt.split("\n"):
        pprint(["".join(each) for each in screen])
        if "rect" in each:
            col, row = each.split(" ")[1].split("x")
            rect(col, row, screen)
        elif "rotate row" in each:
            row, pixel = each.split("=")[1].split(" by ")
            rotateRow(row, pixel, screen)
        elif "rotate column" in each:
            col, pixel = each.split("=")[1].split(" by ")
            rotateCol(col, pixel, screen)
        else:
            print(each)
            raise ValueError
    print("Answer: ", sum([sum([int(i) for i in x]) for x in screen]))

def part2(inpt):
    screen = [["0"]*50 for _ in range(6)]
    for each in inpt.split("\n"):
        if "rect" in each:
            col, row = each.split(" ")[1].split("x")
            rect(col, row, screen)
        elif "rotate row" in each:
            row, pixel = each.split("=")[1].split(" by ")
            rotateRow(row, pixel, screen)
        elif "rotate column" in each:
            col, pixel = each.split("=")[1].split(" by ")
            rotateCol(col, pixel, screen)
        else:
            print(each)
            raise ValueError
    for each in screen:
        for char in each:
            print("#" if char=="1" else " ", end="")
        print()

part1(getInput(2016,day).strip())
part2(getInput(2016,day).strip())
