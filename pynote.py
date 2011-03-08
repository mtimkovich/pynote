#!/usr/bin/env python
import subprocess
import sys
import os

PATH = os.environ["HOME"] + "/.config/pynote/"
NOTES_PATH = os.environ["HOME"] + "/.config/pynote/notes/"
NOTE_DAT = os.environ["HOME"] + "/.config/pynote/names.dat"

OPTIONS = ["New", "Open", "List", "Delete", "Quit"]
EDITOR = os.environ["EDITOR"] or "vi"

GREEN = "\033[22;32m"
BOLD = "\033[01;37m"
RESET = "\033[00;37m"

def title():
    print("[", end="")
    for i in range(0, len(OPTIONS)):
        print(BOLD + OPTIONS[i][0], end="")
        print(RESET + "-" + OPTIONS[i], end="")
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

    try:
        file = open(NOTES_PATH + note_name)
        text = file.read()
        file.close()
    except IOError:
        print(note_name + " not saved: ignoring", file=sys.stderr)
        return

    if text:
        store_note_name(note_name)
    else:
        print(note_name + " is empty, not saving", file=sys.stderr)
        os.unlink(NOTES_PATH + note_name)
        

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

    note_list = notes.splitlines()
    if c > len(note_list):
        print("Invalid input")
        return

    try:
        subprocess.call([EDITOR, NOTES_PATH + note_list[c]])
    except OSError:
        print("Error running `" + EDITOR + " " + NOTES_PATH + note_list[c] + "'", file=sys.stderr)
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
        print(GREEN + str(i) + RESET + " " + note_list[i])

def delete_note():
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

    note_list = notes.splitlines()
    if c > len(note_list):
        print("Invalid input")
        return

    os.unlink(NOTES_PATH + note_list[c])

    del note_list[c]
    try:
        file = open(NOTE_DAT, "w")
        for i in note_list:
            file.write(i)
            file.write("\n")
        file.close()
    except IOError:
        print("Error writing `" + NOTE_DAT + "'", file=sys.stderr)
        exit(1)

############ Main ##############

if not os.path.isdir(PATH):
    try:
        os.mkdir(PATH)
    except OSError:
        print("Error creating '" + PATH + "' directory", file=sys.stderr)
        exit(1)

if not os.path.isdir(NOTES_PATH):
    try:
        os.mkdir(NOTES_PATH)
    except OSError:
        print("Error creating '" + NOTES_PATH + "' directory", file=sys.stderr)
        exit(1)

try:
    c = ""
    while c != "q":
        title()
        c = input("> ").lower()[0]

        if c == "n":
            new_note()
        elif c == "o":
            open_note()
        elif c == "l":
            list_notes()
        elif c == "d":
            delete_note()
        elif c == "q":
            exit(0)
        else:
            print("Unknown command")

        print()
except KeyboardInterrupt:
    exit(0)

