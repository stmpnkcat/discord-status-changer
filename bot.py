import time
import requests
import os

url = "https://discord.com/api/v10/users/@me/settings"

file = open("text.txt", "r")
lines = file.readlines()

def change_status(message):
    
    header = {
        "authorization": os.getenv("DISCORD_API"),
    }

    json_data = {
        "status": "online",
        "custom_status": {
            "text": message
        }
    }
    request = requests.patch(url, headers=header, json=json_data)

while True:

    for line in lines:
        
        change_status(line.split("\n")[0])
        time.sleep(3)
