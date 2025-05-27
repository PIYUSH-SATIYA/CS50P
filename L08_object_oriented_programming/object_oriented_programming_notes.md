# A Tuple

It is very similar to a list, just the difference is that a tuple is immutable (the values can't be changed).

However we can still access its elements by indexing in the same fashion as we do in a list.

When we return multiple values in a function, a tuple of values get returned, however we can explicittely specify that like using the syntax like this.

-   `return (item1, item2)` (without parenthesis is also permissible and it will also be a tuple)

a typeError is thrown when we try to modify some elem of a tuple

all types of values can coexist in a tuple, similar to a tuple

# Classes and Objetcs

A class is a blueprint to create objects and store data in some specific fashion.

An obj is an instance of class, i.e. when we use class we are actually creating, modifying objects.

To initialize an object with some specific values, we have to define a constructor which is a function with the same name as the class and has its first argument as the word `self`.

in class we define constructor like

```python

    class ClassName:
        def __init__(self, param1, param2 ...):
            self.param1 = param1...
```

the param1 and param2 etc. are the parameters req. to create a new object, to assign them to something we syntax like above with self keyword,

-   The name of the variable with self keyword can be anything like self.anything = param1, but it is the convention to name it like that.

we can make some parameter in the constructor optional by setting it's default value to `None`

We cannot directly print an object as a whole directly just like we do with dictionary.  
To print something as a str in when our object is tried to print directly as a whole like print(objectName), we have to introduce a \_\_str\_\_ method.

-   it is also a function that returns some string and that string will be printed when the whole obj is tied to be printed like done above.
-   It takes only one argument that is the self variable.

We can define our custom methods also in our classes, which can be used by any of the instances of the class.
