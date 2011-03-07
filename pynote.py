#!/usr/bin/env python
import subprocess
import sys

BLUE = "\033[22;34m"
GREEN = "\033[22;32m"
BOLD = "\033[01;37m"
EC = "\033[00;37m"

OPTIONS = ["New", "Open", "List", "Delete", "Quit"]
NOTES_PATH = "/home/max/Python/note/notes/"
NOTE_DAT = "names.dat"
EDITOR = "vim"

def title():
    print("[", end="")
    for i in range(0, len(OPTIONS)):
        print(BOLD + OPTIONS[i][0], end="")
        print(EC + "-" + OPTIONS[i], end="")
        if i != len(OPTIONS)-1:
            print(" ", end="")
        else:
            print("]")

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
        return

    store_note_name(note_name)

def open_note():
    print("Enter note's number")

    c = 0
    try:
        c = int(input("> "))
    except ValueError:
        print("Invalid input")
        return

    try:
        file = open(NOTE_DAT, "r")
        notes = file.read()
        file.close()
    except IOError:
        print("Error writing `" + NOTE_DAT + "'", file=sys.stderr)
        exit(1)

    notes_list = notes.splitlines()
    if c > len(notes_list):
        print("Invalid input")
        return

    try:
        subprocess.call([EDITOR, NOTES_PATH + notes_list[c]])
    except OSError:
        print("Error running `" + EDITOR + " " + NOTES_PATH + notes_list[c] + "'", file=sys.stderr)
        return

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
        print(GREEN + str(i) + EC + " " + note_list[i])

try:
    c = ""
    while c != "q":
        title()
        c = input("> ").lower()

        if c == "n":
            new_note()
        elif c == "o":
            open_note()
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
