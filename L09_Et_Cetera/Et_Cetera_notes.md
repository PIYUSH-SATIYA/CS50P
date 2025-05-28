# Sets

set is another datatype, which does not allow repeatation of items in it.

`setName.add()` method is used to add something to the set

# Global Variable

A variable just written outside all the functions is indeed a global variable but it is read only, it just can't modified unless explicitely mentioned.

To change that variable inside some function, we have to include the line `global variableName` to the function and then it can be changed.

If a variable with the same name as the global one, the local gets preceedence.

# Constants

It's value can't be changed once defined,

unfortunately the python as a language does not defies the change in it but it is the honour system of python.

There is no syntax in python to declare a constant, we just write it in all caps just conventionally and it will be treated as constant, by other collaborators.

# Type hints

Python is a dynamically typed language which means that it dynamically detects the type of the variable and not needing the coder to explicitely specify it.

However we can use some tools that help us ensuring type safety,

We can give hints about the type of data to be assigned to the variable by annotating it like `variable: typeOfData`

However the language itself does not enforce it but, some programs do.  
one of such is `mypy`, we just have to run it like `mypy filename.py` and it will warn us about the violation of type hints.

We can annotate the return value also by using the arrow syntax.

# docstrings

These are specially written comments whose purpose is to generate documentation for the code we have written, and we avoid inline comments for that purpose.

There are third party tools which than identify the docstring and generate separate pdf and md files as documentatoins.


# Argparse

It is great to provide switches and flags in the cli when the user is going to interact with the programe in the cli.  

The argparse library comes with great way of providing switches.  

Conventionally, the name of the switches with only one letter are preceeded by one dash like `-n`, and those with more letter required to be preceeded with two dashes, like `--help`.  

