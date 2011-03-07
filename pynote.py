#!/usr/bin/env python
import subprocess
import sys

NAMES = ["New", "Open", "List", "Delete", "Quit"]
NOTES_PATH = "/home/max/Python/note/notes/"
NOTE_DAT = ".names.dat"
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

def store_note_name(note_name):
    try:
        file = open(NOTE_DAT, "a")
        file.write(note_name)
        file.write("\n")
        file.close()
    except IOError:
        print("Could not write to `" + NOTE_DAT + "'", file=sys.stderr)

def new_note():
    print("Enter note's name")
    note_name = input("> ")

    try:
        subprocess.call([EDITOR, NOTES_PATH + note_name])
    except OSError:
        print("Error running `" + EDITOR + " " + NOTES_PATH + note_name + "'", file=sys.stderr)

    store_note_name(note_name)

try:
    c = ""
    while c != "q":
        c = menu().lower()
        if c == "n":
            new_note()
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
except KeyboardInterrupt:
    exit(0)
