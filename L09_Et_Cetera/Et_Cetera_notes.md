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

# Unpacking

when we have to pass multiple arguments separately, currently present in list format, if we want to make it inpack element by element itself we can use the \* operater while passing the argument there.

if the names of parameters a function requires are param1, param2, and param3, we can also pass the arguments to the function like this `func(param1=val1, param2=val2, param3=val3)`, we call it named arguments.

This will work when passed in any order.

We can leverage that feature when we want to unpack a dictionary.

since the dictionary also stores keys and values where order does not matter, when passed as unpacking automatically it unpacks into the keys and values it has stored separated by `=` signs and that's exactly what we want.

To unpack a dictionary, we use \*\* operator.

# \*args and \*\*kwargs

These allows us to pass and handle dynamic numbers of arguments and keyword arguments.

When we are writing parameters a function is gonna take we can specifiy there like `def foo(*args)` so that it can take any number of arguments and make a list out of it which can later be processed in the function as required.  
similarly, when \*kwargs is written it takes variable number of keyword arguments or what we called named parameter, and make a dictionary out of it and process accordingly.

# map()

map(function, iterable, \*iterables)

Return an iterator that applies function to every item of iterable, yielding the results. If additional iterables arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted

# list comprehension

it is a pythonic way to iterate through a list, running a function and generatring a brand new list, something similar we can do with map.

its just another syntax but the same logic as in map().

new syntax: newList = [func.ref for item im oldList someConditionToBeIncluded(Optional)].

# Filter

It is used to produce the same effect as the map but the difference is just that, the first arg ref function we pass is boolean.

# Dictionary Comprehension

It is also a pythonic way to iterate through a list and create a dictionary by writing the logic as the element to be added in the dictionary object.

# Enumerate

To iterate through a list with the elements and the index along with it also.

# Generators, yoeld and iterator

In Python, an iterator is an object that lets you loop through a sequence using **iter**() and **next**() methods, while a generator is a special kind of iterator built using a function with the yield keyword, which allows values to be produced one at a time, pausing and resuming the function’s state between calls; this enables lazy evaluation, meaning values are generated only when needed, making generators ideal for handling large datasets or infinite sequences efficiently without consuming much memory.

It is necessary because in order to modularize our code, if we try to return a large amount of data all at once, the mrmory might break.
