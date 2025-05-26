import re

# our goal is to extract the user's username or anything from the twitter's url

url = input("URL: ").strip()
print(url)

# method - 1:

# username = url.replace("https://twitter.com/", "")      # it will just replace just the starting part of the url, but it may break when user inputs, my url is this: http....

# method - 2:

if matches := re.search(r"^https://(?:www\.)?twitter\.com/([0-9a-z_]+)", url):  # ?: means that group is not inclusive to acess via re.group() method
    print(f"username: {matches.group(1)}")

else:
    print("Invalid url")