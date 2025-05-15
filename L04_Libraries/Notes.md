# APIs (applicatino programming interface)

If we read the documentation of itunes we can contruct a url like this on our own to get data from its website in specific format called JSON(generally used) which can be then processed on server or locally by machines

https://itunes.apple.com/search?entiy=song&limit=1&term=weezer

opening this with a browser, a 'request' will be sent to the web address itunes.apple.com 
    to search: 
    an entity called song,
    limit the searches to 1,
    search for the term weezer in that entity,

it will send the approproate data in particular format (JSON) which we can process accordingly

to make this request on our on using code we should have something that sends request instead of a browser this can be done using 'requests' library of python

# The JSON (JavaScript Object Notation) format

it the a format to store some text data using curly braces, quaotes and colons

The braces represent a block
in that key value pairs of data will be stored

