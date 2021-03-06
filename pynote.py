#!/usr/bin/python
import subprocess
import sys
import os

PATH = os.environ["XDG_CONFIG_HOME"] + "/pynote/"
NOTES_PATH = os.environ["XDG_CONFIG_HOME"] + "/pynote/notes/"
NOTE_DAT = os.environ["XDG_CONFIG_HOME"] + "/pynote/notes.dat"

OPTIONS = ["New", "List", "Delete", "Quit"]
EDITOR = os.environ["EDITOR"] or "vi"

GREEN = "\033[22;32m"
BOLD = "\033[01;37m"
RESET = "\033[00;37m"

def prompt():
    user = input("> ")

    if user == "" or user == "\n":
        raise IOError
    else:
        return user

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
    try:
        note_name = prompt()
    except IOError:
        return

    if len(note_name) > 255:
        print("Note name is too long", file=sys.stderr)
        return

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

def open_note(c):
    try:
        file = open(NOTE_DAT, "r")
        notes = file.read()
        file.close()
    except IOError:
        print("Error writing `" + NOTE_DAT + "'", file=sys.stderr)
        exit(1)

    note_list = notes.splitlines()
    if c >= len(note_list) or c < 0:
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
        print("You do not have any notes!")
        return

    note_list = notes.splitlines()
    for i in range(0, len(note_list)):
        print(GREEN + str(i) + RESET + " " + note_list[i])

def delete_note():
    print("Enter note's number")

    c = 0
    try:
        c = int(prompt())
    except ValueError:
        print("Invalid input")
        return
    except IOError:
        return

    try:
        file = open(NOTE_DAT, "r")
        notes = file.read()
        file.close()
    except IOError:
        print("Error writing `" + NOTE_DAT + "'", file=sys.stderr)
        exit(1)

    note_list = notes.splitlines()
    if c > len(note_list) or c < 0:
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
    first = 0
    while 1:
        title()
        if first == 0:
            list_notes()
        c = ""
        try:
            c = prompt().lower()
        except IOError:
            print()
            continue

        if c.isdigit():
            open_note(int(c))
        elif c == "n":
            new_note()
        elif c == "l":
            list_notes()
        elif c == "d":
            delete_note()
        elif c == "q":
            exit(0)
        else:
            print("Unknown command")

        print()
        first = 1
except KeyboardInterrupt:
    exit(0)

