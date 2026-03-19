import hashlib

hash_to_crack = "c20fa16907343eef642d10f0bdb81bf629e6aaf6c906f26eabda079ca9e5ab67"

with open("rockyou.txt","r",encoding="latin-1") as f:
    for line in f:
        pwd = line.strip()
        if hashlib.sha256(pwd.encode()).hexdigest() == hash_to_crack:
            print("Contraseña encontrada:", pwd)
            break