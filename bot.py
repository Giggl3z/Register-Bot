import random
import time
import os
import string
import requests
import json

names = json.loads(open("names.json").read())
message = input("Enter a message: ")

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

for username in names:
    username = username.lower() + str(random.randint(100, 999))
    password = ''.join(random.choice(chars) for i in range(8))
    email = username + "@gmail.com"

    registerData = json.dumps({
        "email": email,
        "username": username,
        "password": password
    })

    r = requests.post("https://sprx.io/api/auth/register", headers={"Content-Type": "application/json;charset=UTF-8"}, data=registerData)
    
    data = r.json()

    uid = data['user']['id']

    head = r.headers

    hdr = head

    token = hdr['Authorization']

    messageData = json.dumps({
        "uid": uid,
        "shout": message,
        "username": username,
        "userRank": 1
    })
    
    m = requests.post("https://sprx.io/api/shouts/post", headers={"Authorization": token,"Content-Type": "application/json;charset=UTF-8", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}, data=messageData)
    print("Registered '" + data['user']['username'] + "' and sent '" + message + "' to the chat")
    #time.sleep(2)