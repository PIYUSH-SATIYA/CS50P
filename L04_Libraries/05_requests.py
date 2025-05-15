import json
import requests
import sys

if len(sys.argv) != 2:  # first one the name of the program and other the name of the 
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])


# This response printed have only two main entries in the dictionary resultCount and results
    # interestingly the whole of the data is packed into one single array and paired with 'results'
    # print(response.json())


# we can make the result prettir using another python library called JSON which formats the data and make it easier to read

# print(json.dumps(response.json(), indent = 4))
# still there is no change in the data, except the way of formating

# we can get some meaningfull data too if we have read the docs for that api proprly (here we can see it from just seeing the output json file)
    #here in the value of the key results we have another dictionary which has a key called "trackName" and its value is the name of the some of the band to be searched with the "term"
    # to get the multiple songs we should make multiple searches, so we have to increase the limit in the url (again we come to know this using a url)

newResp = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

obj = newResp.json()

#Now to iterate through the responses(newResp) stored in obj as the json

for result in obj["results"]:
    print(result["trackName"])