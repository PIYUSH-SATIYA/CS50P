# Unit Test

It means writing the test like for this input something should be output. Writing this kind of code is called a unit test. simply it is the test for functions written

# pytest

instead of manually writing all the test and test some code, bcoz that would literally be more lines of code for testing than the actual function

it is simplet third party library often comes with python to automate the testing thing to some extent

after installing with pip, to run the test we type the command pytest fileName.py instead of python3 fileName.py

# categories while testing

if all the assertion are written in one go and if any one of them goes off then the subsequent assertions do not get executed

to deal with this problem, we make differnt functions for testing different types of input and basically categorize the assertions in those functions

for example, to test the square function, we should make three functions separetely testing positve, negative and zero inputs

there may be exceptions too in the code to be tested, this can be tested like, 

def exceptionTesterFunction():
    with pytest.raises(TypeofErrorItShouldBeRaising):
        functionToBeTested(inputForTheExceptionIsToBeChecked)


The most imp thing is that we can desing test for the return values of the functions and not the side effects like what it is printing on the screen

# to organize the test

We may also have the whole folders of tests in order to keep them organized

We have to make a file named "\_\_init\_\_\.py" (without quotes), so that this whole folder will be considered as a package, even if the file is empty

This will help many frameworks like pytest, here it will run all the tests in all the files of this directory