from base64 import b64decode
import string

# Leer archivos
with open(r"Here you put your path to the files.\Files 02\leak\usernames.txt") as f:
    usernames = [line.strip() for line in f]

with open(r"Here you put your path to the files.\Files 02\leak\passwords.txt") as f:
    passwords = [line.strip() for line in f]

# Buscar usuario
target = "cultiris"

if target not in usernames:
    print("User not found")
    exit()

idx = usernames.index(target)
password = passwords[idx]

print(f"[+] Found password: {password}")

# Intentos de decodificación
print("\n[+] Trying Base64:")
try:
    print("\t"+b64decode(password).decode())
except:
    print("\tNot Base64")

print("\n[+] Trying Hex:")
try:
    print("\t"+bytes.fromhex(password).decode())
except:
    print("\tNot Hex")

print("\n[+] Trying Caesar shifts:\n")

def caesar(s, shift):
    result = ""
    for c in s:
        if c.isalpha():
            base = 'a' if c.islower() else 'A'
            result += chr((ord(c) - ord(base) + shift) % 26 + ord(base))
        else:
            result += c
    return result

for i in range(26):
    decoded = caesar(password, i)
    if "picoCTF{" in decoded:
        print(f"[+] Found flag (shift {i}): {decoded}")
        break