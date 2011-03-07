#!/usr/bin/env python
import subprocess
import sys

BLUE = "\033[22;34m"
GREEN = "\033[22;32m"
BOLD = "\033[01;37m"
EC = "\033[00;37m"

NAMES = ["New", "Open", "List", "Delete", "Quit"]
NOTES_PATH = "/home/max/Python/note/notes/"
NOTE_DAT = ".names.dat"
EDITOR = "vim"

def title():
    print("[", end="")
    for i in range(0, len(NAMES)):
        print(BOLD + NAMES[i][0], end="")
        print(EC + "-" + NAMES[i], end="")
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
        exit(1)

def new_note():
    print("Enter note's name")
    note_name = input("> ")

    try:
        subprocess.call([EDITOR, NOTES_PATH + note_name])
    except OSError:
        print("Error running `" + EDITOR + " " + NOTES_PATH + note_name + "'", file=sys.stderr)

    store_note_name(note_name)

def list_notes():
    try:
        file = open(NOTE_DAT, "r")
        notes = file.read()
        file.close()
    except IOError:
        print("Error writing `" + NOTE_DAT + "'", file=sys.stderr)
        exit(1)

    note_list = notes.splitlines()
    for i in range(0, len(note_list)):
        print(GREEN + str(i+1) + EC + " " + note_list[i])

try:
    c = ""
    while c != "q":
        c = menu().lower()
        if c == "n":
            new_note()
        elif c == "o":
            print("open file")
        elif c == "l":
            list_notes()
        elif c == "d":
            print("delete note")
        elif c == "q":
            exit(0)
        else:
            print("Unknown command")

        print()
except KeyboardInterrupt:
    exit(0)
