import requests
from datetime import datetime

TOKEN = "your token here"
USERNAME = "your username here"
ID = "readingraph"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# #Create your user account.
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": ID,
    "name": "Reading Tracker",
    "unit": "chapters",
    "type": "int",
    "color": "momiji"
}

##Create your graph.
# response = requests.post(url= graph_endpoint, json=graph_config, headers=header)
# print(response.text)

a_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

##Use the variable below for a past date.
# today = datetime(year=2024, month=6, day=20)
# formatted_data = today.strftime("%Y%m%d")

## Or the variable below for today's date.
today = datetime.now()

a_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many chapters did you read?\n")
}

quantity = {
    "quantity": input("How many chapters did you read?\n")
}

put_or_delete_api_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{formatted_data}"

##Add your tracked chapters.
response = requests.post(url= a_pixel_endpoint, json=a_pixel_config, headers=header)
print(response.text)

##Update numbers of chapters read.
# response = requests.put(url= put_or_delete_api_endpoint, json=quantity, headers=header)
# print(response.text)

##Delete chapters from a specific day.
# response = requests.delete(url= put_or_delete_api_endpoint, headers=header)
# print(response.text)