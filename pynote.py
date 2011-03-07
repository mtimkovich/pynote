#!/usr/bin/env python
import subprocess
import sys

NAMES = ["New", "Open", "List", "Delete", "Quit"]
NOTES_PATH = "/home/max/Python/note/notes/"
EDITOR = "vim"

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

def newfile():
    print("Enter note's name")
    filename = input("> ")

    try:
        subprocess.call([EDITOR, NOTES_PATH + filename])
    except OSError:
        print("Error running `" + EDITOR + " " + NOTES_PATH + filename + "'", file=sys.stderr)

c = ""
filename = ""
while c != "q":
    c = menu().lower()
    if c == "n":
        newfile()
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

