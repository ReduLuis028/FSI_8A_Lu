import socket
from math import gcd
from Crypto.Util.number import inverse, long_to_bytes

HOST = "verbal-sleep.picoctf.net"
PORT = 64112
e = 65537

def get_data():
    s = socket.socket()
    s.connect((HOST, PORT))
    data = s.recv(4096).decode()
    s.close()

    lines = data.strip().split("\n")

    N = int(lines[0].split(":")[1].strip())
    c = int(lines[2].split(":")[1].strip())

    return N, c

# Guardar varios datos
data = []
print("[+] Collecting data...")

for _ in range(8):  # intenta varias veces
    try:
        N, c = get_data()
        print(f"[+] Got N: {N}")
        data.append((N, c))
    except:
        pass

print("[+] Searching for shared primes...")

# Buscar GCD
for i in range(len(data)):
    for j in range(i+1, len(data)):
        N1, c1 = data[i]
        N2, c2 = data[j]

        p = gcd(N1, N2)

        if p != 1:
            print("[+] Found shared prime!")

            q = N1 // p
            phi = (p-1)*(q-1)
            d = inverse(e, phi)

            m = pow(c1, d, N1)
            flag = long_to_bytes(m)

            print("[+] FLAG:", flag.decode())
            exit()

print("[-] Try running again (not enough collisions)")