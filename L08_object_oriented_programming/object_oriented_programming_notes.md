Object Oriented Programming is just another way of solving the same kind of problem, a way to encapsulate and to represent real world entities in code.

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

# Getteres, Setters and Properties

These are the concepts of OOP to encapsulate the attributes of an object and make them protected from directly accessible and modifiable without any validation.

Actually the getters and setters are just functions in python with some specialities, and with function we can encapsulate the attributes for different purposes and define some validating conditions there to make code, readable, reusable and future-proof.

## Getter

It is having the same name as the attribute, whose value we want to get.  
It takes only one argument and that is self.

we put the keyword `@property`
above the definition of the getter to set it as a getter in pythonic way

## Setter

It is also having the same name as the attribute, whose value we want to set.  
It takes two argument and that is self and the value which we want to assign to the attribute.

we put the keyword `@nameOfAttribute.setter`
above the definition of the getter to set it as a setter in pythonic way.

Conventionally and to save the interpreter from being confused, we put `_` before the name of the attribute wherever we are using it internally, except in the `__init__` method.

The name of the getter and setter are kept same as the name of the attribute so that whenever we want to get or set the value of the attrubute, we make it pass through the getter an setter.  
and we do not put an `_` before the name of the attribute in the init method because when initialising the obeject we still want to go it through the setter, and the validations in it.

> In python the keyword prefixed with @ are called decorators, which are just another function that makes some other functions just behave differently.

### The crux of all these

In python, there is no built in mechanism to define some variable to be private and some others public.  
It is just based on convention that if a variabl name starts with an underscore (or double underscore for more emphsizement) it is meant to be private and please just don't touch it.

-   but there is nothign stopping us from doing that.

# Types and classes

In python everything is just a class and its instances,

We can confirm it by the `type()` method in which we give integers, or strings or lists or anything and all of them just comes out to be a class.

It just feels like you will use classes and object from now onwards, but in python you always have been.

# Class variables and Class methods

We ideally use classes when we want to instantiate some real world entity like integer, or str, or somethings related to students.

Often in that case we come accross a requirement that some variable and methods need not to be separately initialised for all the instances of the class, and there comes the class methods and class variables.

These are variables and methods define once in the class and there will be only one copy of it shared among all the instances(objects) of the class.

### How to define them

The class methods and class variables does not require any constructor, hence they don not require access to the self context.

Those are written under the `@classmethod` decorator (only for class methods)

so in the method where we have to pass the self argument, we pass the `cls` argument which passes the context of the whole class.

Then we do not need to instantiate the class to use the method.  
we can use it with `Classname.method(arguments)`

> Ideally classes should be put in its separate file, or atleast define at the top of the file.

# Inheritance

There may be some properties attributes overlapping between the class bacause they might fall under same parent.

For that we can leverage the concept of inheritance to make the flow of the code clear.

To specify the parent class of some class, we write the oarent name in paranthesis after the child class name like:

-   class Childclass(Parent)

To use the init methods of the parent class we use the syntax like this:

-   super().\_\_init\_\_(name)

The method super() just specifies that take this from its parent and, in the parenthesis after the \_\_init\_\_ the name of the attribute which is to be used from the parent is written

# Operator Overloading in python

Operator overloading allows user-defined classes to redefine the behavior of Python's built-in operators (`+`, `-`, `*`, etc.) when used with objects of user defined classes objects.

There are perdefined dunder methods for conventional operators for example:

| Operator | Magic Method               |
| -------- | -------------------------- |
| `+`      | `__add__(self, other)`     |
| `-`      | `__sub__(self, other)`     |
| `*`      | `__mul__(self, other)`     |
| `/`      | `__truediv__(self, other)` |
| `==`     | `__eq__(self, other)`      |
| `<`      | `__lt__(self, other)`      |
| `>`      | `__gt__(self, other)`      |

the two argums passed self and other, they will act as operands for the new operator, and the result will be returned from that method

-   e.g. the `+` operator add only integer and concatenates strings, but if we have to add the vectors which has two components, we can not add them directly, but we can modify the `__add__` method to add them appropiately and return in appropriate format also.

# just off topic but necessary:

> When we write or pass just the name of the function (means without parenthesis), we are passing just the reference to it, may be handled by some other function or in some other way, and when we write it with parenthesis, we are actually calling it.
