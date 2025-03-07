import pyshorteners

url = input("Paste your URL here: ")
short_url = pyshorteners.Shortener().tinyurl.short(url)
print(f"Here's your shortened URL: {short_url}")