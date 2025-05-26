a regular expression is a sequence of characters which defines search criteria for some text.
for example, in an email @ sign must be there, some username and domain are also requred.

-   this sets a fixed pattern the user input must follow, to get a valid email input.
-   we can think of it like some template.

# re library

if we have to check the validity of the user we can indeed write some conditionals and validate but it just make the code writign tedious and repetative.  
The `re` library comes with some great methods to validate and further process the inputs.

## The search method in re library

It searches in given string(second argument), for some pattern(first argument) defined by some special symbols like (. or \* or + or ? etc.)

-   . means any char except a newline
-   \* means 0 or more repeatations
-   \+ means 1 or more repeatations
-   ? means or 1 repeatation, means it makes something optional
-   ^ means start of the expressio
-   $ means end of the expression
-   [] some set of characters that are allowed
-   [^] some set of characters that are not allowed, means complementary set of what char are allowed.
    -   we can also specify the range of characters usnig the square bracket syntax like this [a-zA-Z0-9_] This means all letter from a to z, both lower case and upper case, all numbers, and an \_ is allowed only

## Character Classes

There are some built-in symbols assigned to some highly used patterns like the above is used for email.

-   e.g. The `\w` symbol is to represent a word containg alphanumeric characters and additionally an `_`
-   e.g. The `\W` is complement of the above set i.e. anything that is not alphanumeric and an `_`

The `|` meand logical `or`.  
The parenthesis are used to group things, for example set of top level domains can be made allowed regex by adding a or symbol in between and all of them can be grouped together. It is the same function as in math.

# Flags

These are some standard configuration which will be applied to our string.  
This is the third argument passed to the `re.search()` method.

-   e.g. The `re.IGNORECASE` ignores the case of our string as the name suggests.

# The return value of the re.search method

The re.search() method returns the groups if made in the regex, and can be accessed via the `re.group()` method, in the () we give 1 to access the first group and so on.

> out of the box:
> := the walrus operator, is assigns as well as asks a boolean question

# re.sub

It finds for some pattern and replaces it with some desired pattern, just a fancy version of the `replace()` method
