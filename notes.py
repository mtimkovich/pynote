#!/usr/bin/env python

NAMES = ["New", "Open", "List", "Delete", "Quit"]

def bold(bool):
    ESC = chr(27)
    if bool == 1:
        print(ESC + "[1m", end="")
    else:
        print(ESC + "[0m", end="")

def title():
    print("[", end="")
    for i in range(0, len(NAMES)):
        bold(1)
        print(NAMES[i][0], end="")
        bold(0)
        print("-" + NAMES[i], end="")
        if i != len(NAMES)-1:
            print(" ", end="")
        else:
            print("]")

def menu():
    title()
    answer = input("> ")
    return answer

c = ""
while c != "q":
    c = menu().lower()
    if c == "n":
        print("new file")
    elif c == "o":
        print("open file")
    elif c == "l":
        print("list notes")
    elif c == "d":
        print("delete note")
    elif c == "q":
        exit(0)
    else:
        print("Unknown command")

    print()

