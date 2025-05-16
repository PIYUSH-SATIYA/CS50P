import emoji

str = input("Enter word or alias: ")

print("emojis is: " + emoji.emojize(str, language='alias'))