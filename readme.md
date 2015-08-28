# Command line tool that manages phone books

# Interface

Create the phone book hsphonebook.pb in the current directory.

```shell
$ phonebook create hsphonebook.pb
```
or

```shell
$ python phonebook.py create hsphonebook.pb
```

Look for a person in a phone book.

```shell
$ phonebook lookup Sarah hsphonebook.pb # error message on no such phonebook
Sarah Ahmed 432 123 4321
Sarah Apple 509 123 4567
Sarah Orange 123 456 7890
```

Add a person in a phone book.

```shell
$ phonebook add 'John Michael' '123 456 4323' hsphonebook.pb # error message on duplicate name
```

Edit a person in a phone book.

```shell
$ phonebook change 'John Michael' '234 521 2332' hsphonebook.pb # error message on not exist
```

Remove a person from a phone book.

```shell
$ phonebook remove 'John Michael' hsphonebook.pb # error message on not exist
```

Look for a phone number in a phone book.

```shell
$ phonebook reverse-lookup '312 432 5432' hsphonebook.pb
```
