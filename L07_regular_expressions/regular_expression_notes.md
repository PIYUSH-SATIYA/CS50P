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
-   ^ means start of the expressio
-   $ means end of the expression
-   [] some set of characters that are allowed
-   [^] some set of characters that are not allowed, means complementary set of what char are allowed.
