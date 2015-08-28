#! /usr/bin/python

import sys
import re

def closedatabase(file):
    file.close()
    print 'database closed'

def create(filename):
    file = open(filename, 'a')
    closedatabase(file)
    print "Database created and opened succesfully"

def openDatabase(filename):
    file = open(filename, 'r')
    print 'database opened'
    return file

def getPhonebook(filename):
    file = open(filename, 'r')

    phonebook = {}
    for line in file:
        line = line.split(';')
        phonebook[line[0].strip()] = line[1].strip()

    closedatabase(file)
    return phonebook

# Get the arguments list
argsList = sys.argv
cmd = argsList[1]

def main():
    if cmd == 'create':
        # because i didn't like the idea to loop through the list and check if 2 is in the list
        if not 2 in range(len(argsList)):
            print 'A database filename must be specified'
        else:
            create(argsList[2])

    elif cmd == 'lookup':
        if not 2 in range(len(argsList)):
            print 'A name must be specified'
        if not 3 in range(len(argsList)):
            print 'A database filename must be specified'

        filename = argsList[3]
        phonebook = getPhonebook(filename)

        entries = []
        for key, value in phonebook.iteritems():
            if argsList[2] in key:
                entries.append(key + ' ' + str(value))

        if len(entries):
            for entry in entries:
                print entry
        else:
            print 'No entry found'

    elif cmd in 'add':
        if not 2 in range(len(argsList)):
            print 'A name must be specified'
        if not 3 in range(len(argsList)):
            print 'A phone must be specified'
        if not 4 in range(len(argsList)):
            print 'A database filename must be specified'

        filename = argsList[4]
        phonebook = getPhonebook(filename)

        # is user already existing
        if str(argsList[2]) in phonebook:
            print 'This user already exist, you must specify another name'
        else:
            file = open(filename, 'a')
            file.write(str(argsList[2]) + ';' + str(argsList[3]) + '\n')
            closedatabase(file)
            print 'User added'

    elif cmd in 'change':
        if not 2 in range(len(argsList)):
            print 'A name must be specified'
        if not 3 in range(len(argsList)):
            print 'A phone must be specified'
        if not 4 in range(len(argsList)):
            print 'A database filename must be specified'

        filename = argsList[4]
        phonebook = getPhonebook(filename)

        file = open(filename, 'w')
        userEdited = False
        for key, value in phonebook.iteritems():
            if argsList[2] == key:
                userDeleted = True
                file.write(key + ';' + str(argsList[3]) + '\n')
            else:
                file.write(key + ';' + value + '\n')
        closedatabase(file)

        if userDeleted:
            print 'User edited'
        else:
            print 'User not found'

    elif cmd in 'remove':
        if not 2 in range(len(argsList)):
            print 'A name must be specified'
        if not 3 in range(len(argsList)):
            print 'A database filename must be specified'

        filename = argsList[3]
        phonebook = getPhonebook(filename)

        file = open(filename, 'w')
        userDeleted = False
        for key, value in phonebook.iteritems():
            if argsList[2] == key:
                userDeleted = True
            else:
                file.write(key + ';' + value + '\n')
        closedatabase(file)

        if userDeleted:
            print 'User deleted'
        else:
            print 'User not found'

    elif cmd in 'reverse-lookup':
        if not 2 in range(len(argsList)):
            print 'A phone must be specified'
        if not 3 in range(len(argsList)):
            print 'A database filename must be specified'

        filename = argsList[3]
        phonebook = getPhonebook(filename)

        entries = []
        for key, value in phonebook.iteritems():
            if argsList[2] in value:
                entries.append(key + ' ' + str(value))

        if len(entries):
            for entry in entries:
                print entry
        else:
            print 'No entry found'
    else:
        print 'The command you type doesn\'t been exit'

main();
# Questions
# is there any good practice like making a main method or so?
# python doesnt have a swith method, true?
