from Crypto.Util.number import long_to_bytes, inverse
import re

with open("values", "r") as f:
    data = f.read()

nums = list(map(int, re.findall(r"\d+", data)))
n = max(nums)
nums.remove(n)
c = max(nums)
nums.remove(c)
e = max(nums)
print("n = ", n)
print("c = ", c)
print("e = ", e)

# se obtienen de la factorizacion de 'n' en https://factordb.com/
p = 1891771437429478964908181306574287207137
q = 501332739776173570344039681219489434626477
tn = (p-1) * (q-1)
 
d = pow(e, -1, tn)
m = pow(c,d,n)
hex_str = hex(m)[2:]

# verificar que los digitos hexadecimales sean un numero par
if len(hex_str) % 2 != 0:
    hex_str = '0' + hex_str

decoded = bytes.fromhex(hex_str).decode()
print(f'\nDecodificado: {decoded}')

flag = decoded[::-1]
print(f'\nFlag : {flag}')