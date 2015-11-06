import re
from helpers import printEntries, checkParams, closeDatabase, getPhonebook

def create(argsList):
    params = checkParams('create', argsList)

    file = open(params['database'], 'w')
    print "Database created"
    closeDatabase(file)

def lookup(argsList):
    params = checkParams('lookup', argsList)

    phonebook = getPhonebook(params['database'])

    entries = []
    for key, value in phonebook.iteritems():
        if params['name'] in key:
            entries.append(key + ' ' + str(value))

    printEntries(entries)

def reverseLookup(argsList):
    params = checkParams('reverseLookup', argsList)

    phonebook = getPhonebook(params['database'])

    entries = []
    for key, value in phonebook.iteritems():
        if params['phone'] in value:
            entries.append(key + ' ' + str(value))

    printEntries(entries)

def add(argsList):
    params = checkParams('add', argsList)

    if ";" in str(argsList[2]):
        print 'Your user\'s name can not contain the character ";"'
        return

    phonebook = getPhonebook(params['database'])

    # is user already existing
    if str(params['name']) in phonebook:
        print 'This user already exist, you must specify another name'
    else:
        file = open(params['database'], 'a')
        file.write(str(params['name']) + ';' + str(params['phone']) + '\n')
        closeDatabase(file)
        print 'User added'

def change(argsList):
    params = checkParams('change', argsList)

    phonebook = getPhonebook(params['database'])

    file = open(params['database'], 'w')
    userEdited = False
    for key, value in phonebook.iteritems():
        if params['name'] == key:
            userEdited = True
            file.write(key + ';' + str(params['phone']) + '\n')
        else:
            file.write(key + ';' + value + '\n')
    closeDatabase(file)

    if userEdited:
        print 'User edited'
    else:
        print 'User not found'

def remove(argsList):
    params = checkParams('remove', argsList)

    phonebook = getPhonebook(params['database'])

    file = open(params['database'], 'w')
    userDeleted = False
    for key, value in phonebook.iteritems():
        if params['name'] == key:
            userDeleted = True
        else:
            file.write(key + ';' + value + '\n')
    closeDatabase(file)

    if userDeleted:
        print 'User deleted'
    else:
        print 'User not found'
