import re

def closeDatabase(file):
    file.close()
    print 'database closed'

def createDatabase(filename):
    file = open(filename, 'w')
    print "Database created"
    closeDatabase(file)

def getPhonebook(filename):
    file = open(filename, 'r')

    phonebook = {}
    for line in file:
        line = line.split(';')
        phonebook[line[0].strip()] = line[1].strip()

    closeDatabase(file)
    return phonebook

def create(argsList):
    # because I didn't like the idea to loop through the list and check if 2 is in the list
    if not 2 in range(len(argsList)):
        print 'A database filename must be specified'
    else:
        createDatabase(argsList[2])

def lookup(argsList):
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

def add(argsList):
    if not 2 in range(len(argsList)):
        print 'A name must be specified'
    if not 3 in range(len(argsList)):
        print 'A phone must be specified'
    if not 4 in range(len(argsList)):
        print 'A database filename must be specified'

    if ";" in str(argsList[2]):
        print 'Your user\'s name can not contain the character ";"'
        return

    filename = argsList[4]
    phonebook = getPhonebook(filename)

    # is user already existing
    if str(argsList[2]) in phonebook:
        print 'This user already exist, you must specify another name'
    else:
        file = open(filename, 'a')
        file.write(str(argsList[2]) + ';' + str(argsList[3]) + '\n')
        closeDatabase(file)
        print 'User added'

def change(argsList):
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
            userEdited = True
            file.write(key + ';' + str(argsList[3]) + '\n')
        else:
            file.write(key + ';' + value + '\n')
    closeDatabase(file)

    if userEdited:
        print 'User edited'
    else:
        print 'User not found'

def remove(argsList):
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
    closeDatabase(file)

    if userDeleted:
        print 'User deleted'
    else:
        print 'User not found'

def reverseLookup(argsList):
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
