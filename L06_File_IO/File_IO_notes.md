# open method

It enables us to open files in read (r), write (w), and append(a) mode in code, and read, write, and append to it.

we can assign a variable to it while opening a file and use it for later operations in code like  
    file = open("fileName.txt", "w")  

The open method takes two arguments and, first one is the name of the file to be opened and second one is the mode in which we want to open the file, which depends on the requirements in the code  

closing the file is also necessary, with the method file.close()

## Modes to open files

1. "w" : with this mode we can write in a file, but each time opened in this mode and performing an operation the file is newly created and overwrites the older content.  
2. "r" : with this mode we can just read from the file, we can't modify it.  
3. "a" : with this mode we can append to the file which means the older content will stay as it is and new content will be appended to it.  

## with as keyword

to not close the file each name, we can use with as keyword like  
    with open("FileName", "W") as varToBeAssigned

    we can do operations on the file with the variables assigned to it, whatever to be done with this file must be written under this line with one indent and if nothing is written below that indent or just completed then the file is automatically closed.  

## readline method

The method realine() reads a file (opened in r mode) line by line and returns a list of those lines.  

Instead of first storing the lines and then again iterating through them, we can use simpler and memory efficient thing like this  

    for line in file:
        and iterate through the lines
    
This automatically appends a new line after reading one line from any file

# Reading a CSV file

a CSV means comma separated file  
in that a line represents a row and each comma represents the end of a column  
we can split the line using the method split and get an array of elem which are entries of columns in a particular row  

If our csv file has some commas or quotes in the actual values or as the grammer of whatever is written inside the file,  
we have to use a built in library called 'CSV', to resolve the clashes and not reinvent the whole wheel.  

there is a function called reader which reads the files and figures it out where are the actual separators commas and where are the other ones

## Reading as a Dictionary

To read as a dictionary, we have to use the dictReader method:  
* in that case we have to specify the names of the columns, which will then act as the keys to access values in any row  
* The entries in the first row acts as the keys or the names of the columns  
* dictionary reader can also read the csv with more than two columns too  

# writing in a csv file  

we can use the writer method with writerow

if we use the csv library, it would automatically manage escaping

# Writing a dictionary in csv

If we do not know in which order the columns are, it is difficult to write using above method  
that's why we use the dictionary, for which we just have to know the names of the columns and it takes care of the order itself


# Reading and Writing other file formats also

"pillow" is a great library to deal with all such files