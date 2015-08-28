#! /usr/bin/python

import sys
from actions import create, lookup, add, change, remove, reverseLookup

# Get the arguments list
argsList = sys.argv
cmd = argsList[1]

def main(argsList):
    if cmd == 'create':
        create(argsList)

    elif cmd == 'lookup':
        lookup(argsList)

    elif cmd in 'add':
        add(argsList)

    elif cmd in 'change':
        change(argsList)

    elif cmd in 'remove':
        remove(argsList)

    elif cmd in 'reverse-lookup':
        reverseLookup(argsList)

    else:
        print 'The command you type doesn\'t been exit'

main(argsList);

# Questions
# is there any good practice like making a main method or so?
# python doesn't have a switch method, true?
