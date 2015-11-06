#! /usr/bin/python

import subprocess;
import os.path
import timeit

numberOftestsOk = 0
numberOftestsNok = 0

def main():
    start = timeit.default_timer()
    databaseName = 'test_hsphonebook.pb'

    # It should clean a previous database if found
    print '### Test - reset database'
    try:
        os.remove(databaseName)
    except OSError:
        pass

    # test for the database creation
    print '### Test - create command'
    subprocess.check_output(['./phonebook.py', 'create', databaseName])
    asertEqual(os.path.exists(databaseName), True)

    asertEqual(subprocess.check_output(['./phonebook.py', 'create']),
        'A database filename must be specified\n')

    # test for the add command
    print '### Test - add command (first entry)'
    asertEqual(subprocess.check_output(['./phonebook.py', 'add']),
        'A phone must be specified\n')

    asertEqual(subprocess.check_output(['./phonebook.py', 'add', 'Ben']),
        'A phone must be specified\n')

    asertEqual(subprocess.check_output(['./phonebook.py', 'add', 'Ben', '987 456 1230']),
        'A database filename must be specified\n')

    subprocess.check_output(['./phonebook.py', 'add', 'Ben', '123 456 7890', databaseName])

    databaseExpected = dict({'Ben': '123 456 7890'})
    asertEqual(readDatabase(databaseName), databaseExpected)

    print '### Test - add command (same entry)'
    message = subprocess.check_output(['./phonebook.py', 'add', 'Ben', '123 456 7890', databaseName])

    asertEqual(readDatabase(databaseName), databaseExpected)
    asertEqual(message, 'This user already exist, you must specify another name\n')

    print '### Test - add command (new entry)'
    subprocess.check_output(['./phonebook.py', 'add', 'Mary', '987 654 3210', databaseName])

    databaseExpected = dict({'Ben': '123 456 7890', 'Mary': '987 654 3210'})

    asertEqual(readDatabase(databaseName), databaseExpected)

    # Add other users
    subprocess.check_output(['./phonebook.py', 'add', 'Mary', '987 654 3210', databaseName])
    subprocess.check_output(['./phonebook.py', 'add', 'John', '654 789 3210', databaseName])
    subprocess.check_output(['./phonebook.py', 'add', 'Allie', '321 654 0987', databaseName])
    subprocess.check_output(['./phonebook.py', 'add', 'Tom', '123 654 7890', databaseName])

    print '### Test - lookup command'
    asertEqual(subprocess.check_output(['./phonebook.py', 'lookup']),
        'A database filename must be specified\n')

    asertEqual(subprocess.check_output(['./phonebook.py', 'lookup', 'Ben']),
        'A database filename must be specified\n')

    message = subprocess.check_output(['./phonebook.py', 'lookup', 'John', databaseName])
    asertEqual(message, 'John 654 789 3210\n')

    message = subprocess.check_output(['./phonebook.py', 'lookup', 'Ben', databaseName])
    asertEqual(message, 'Ben 123 456 7890\n')

    print '### Test - reverse lookup command'
    asertEqual(subprocess.check_output(['./phonebook.py', 'reverse-lookup']),
        'A database filename must be specified\n')

    asertEqual(subprocess.check_output(['./phonebook.py', 'reverse-lookup', '987 654 3210']),
        'A database filename must be specified\n')

    message = subprocess.check_output(['./phonebook.py', 'reverse-lookup', '987 654 3210', databaseName])
    asertEqual(message, 'Mary 987 654 3210\n')

    message = subprocess.check_output(['./phonebook.py', 'reverse-lookup', '123 654 7890', databaseName])
    asertEqual(message, 'Tom 123 654 7890\n')

    print '### Test - change command (existing user)'
    asertEqual(subprocess.check_output(['./phonebook.py', 'change']),
        'A phone must be specified\n')

    asertEqual(subprocess.check_output(['./phonebook.py', 'change', 'Mary']),
        'A phone must be specified\n')

    asertEqual(subprocess.check_output(['./phonebook.py', 'change', 'Mary', '231 654 3210']),
        'A database filename must be specified\n')

    message = subprocess.check_output(['./phonebook.py', 'change', 'Mary', '231 654 3210', databaseName])

    databaseExpected = dict({'John': '654 789 3210', 'Ben': '123 456 7890', 'Mary': '231 654 3210', 'Allie': '321 654 0987', 'Tom': '123 654 7890'})

    asertEqual(readDatabase(databaseName), databaseExpected)
    asertEqual(message, 'User edited\n')

    print '### Test - change command (not existing user)'
    message = subprocess.check_output(['./phonebook.py', 'change', 'George', '231 564 3210', databaseName])

    databaseExpected = dict({'John': '654 789 3210', 'Ben': '123 456 7890', 'Mary': '231 654 3210', 'Allie': '321 654 0987', 'Tom': '123 654 7890'})

    asertEqual(readDatabase(databaseName), databaseExpected)
    asertEqual(message, 'User not found\n')

    print '### Test - remove command (existing user)'
    asertEqual(subprocess.check_output(['./phonebook.py', 'remove']),
        'A database filename must be specified\n')

    asertEqual(subprocess.check_output(['./phonebook.py', 'remove', 'John']),
        'A database filename must be specified\n')

    message = subprocess.check_output(['./phonebook.py', 'remove', 'John', databaseName])

    databaseExpected = dict({'Ben': '123 456 7890', 'Mary': '231 654 3210', 'Allie': '321 654 0987', 'Tom': '123 654 7890'})

    asertEqual(readDatabase(databaseName), databaseExpected)
    asertEqual(message, 'User deleted\n')

    print '### Test - remove command (not existing user)'
    message = subprocess.check_output(['./phonebook.py', 'remove', 'George', databaseName])

    databaseExpected = dict({'Ben': '123 456 7890', 'Mary': '231 654 3210', 'Allie': '321 654 0987', 'Tom': '123 654 7890'})

    asertEqual(readDatabase(databaseName), databaseExpected)
    asertEqual(message, 'User not found\n')

    numberOftests = numberOftestsOk + numberOftestsNok
    print '\n### Summary'
    print '  - Passed ' + str(numberOftestsOk) + '/' + str(numberOftests)
    print '  - Failed ' + str(numberOftestsNok) + '/' + str(numberOftests) + '\n'

    stop = timeit.default_timer()
    runtime = '(run time: ' + str(round(stop - start, 3)) + 's)'

    if numberOftestsOk == numberOftests:
        print '\033[92m' + '\033[1m' + '  ' + u'\u2713' + '  ' + str(numberOftests) + ' tests passed' + '\033[0m ' + runtime
    else:
        print '\033[91m' + '\033[1m' + '  ' + u'\u2718' + '  ' + str(numberOftestsNok) + '/' + str(numberOftests) + ' test(s) failed' + '\033[0m ' + runtime

def asertEqual(actual, expected):
    global numberOftestsOk
    global numberOftestsNok

    if actual == expected:
        numberOftestsOk += 1
        print '\033[92m' + '\033[1m  ' + u'\u2713' + '\033[0m'
    else:
        numberOftestsNok += 1
        print '\033[91m' + '\033[1m  ' + u'\u2718' + '\033[0m'

def readDatabase(databaseName):
    file = open(databaseName, 'r')

    phonebook = {}
    for line in file:
        line = line.split(';')
        phonebook[line[0].strip()] = line[1].strip()

    file.close()
    return phonebook



main();
