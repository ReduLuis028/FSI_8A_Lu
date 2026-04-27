import socket
import re
import hashlib

HOST = "verbal-sleep.picoctf.net"
PORT = 60516

# Lista rápida (primero intenta esto)
quick_list = [
    "password", "123456", "admin", "letmein",
    "qwerty", "password123", "welcome", "iloveyou",
    "qwerty123"
]

def crack(hash_value):
    # 1. Intento rápido
    for word in quick_list:
        if len(hash_value) == 32 and hashlib.md5(word.encode()).hexdigest() == hash_value:
            return word
        if len(hash_value) == 40 and hashlib.sha1(word.encode()).hexdigest() == hash_value:
            return word
        if len(hash_value) == 64 and hashlib.sha256(word.encode()).hexdigest() == hash_value:
            return word

    # 2. Fallback: rockyou.txt
    try:
        with open("rockyou.txt", encoding="latin-1") as f:
            for word in f:
                word = word.strip()

                if len(hash_value) == 32 and hashlib.md5(word.encode()).hexdigest() == hash_value:
                    return word
                if len(hash_value) == 40 and hashlib.sha1(word.encode()).hexdigest() == hash_value:
                    return word
                if len(hash_value) == 64 and hashlib.sha256(word.encode()).hexdigest() == hash_value:
                    return word
    except FileNotFoundError:
        print("[-] rockyou.txt no encontrado (usando solo quick_list)")

    return None

# Conectar
s = socket.socket()
s.connect((HOST, PORT))

while True:
    data = s.recv(4096).decode()
    print(data)

    # Detectar hash (orden importante: 64 → 40 → 32)
    match = re.search(r"([a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32})", data)
    if not match:
        break

    hash_value = match.group(1)
    print("[+] Hash:", hash_value)

    password = crack(hash_value)

    if not password:
        print("[-] No encontrado")
        break

    print("[+] Password:", password)

    # Enviar respuesta
    s.send((password + "\n").encode())

s.close()