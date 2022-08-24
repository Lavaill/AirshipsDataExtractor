import string

import json5

import modules


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def load_modules(jsonStr):
    print("Loading module")
    objectSet = json5.loads(jsonStr)
    match objectSet:
        case dict():
            print("It's a dictionary")
        case list():
            print("It's a list")


load_modules(modules.imp_cannon)

