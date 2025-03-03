import pyshorteners

url = input("Type your URL here: ")

short_url = pyshorteners.Shortener().tinyurl.short(url)
print(short_url)