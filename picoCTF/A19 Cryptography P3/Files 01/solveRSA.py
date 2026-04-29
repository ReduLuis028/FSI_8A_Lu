from gmpy2 import iroot
import re

with open("ciphertext", "r") as f:
    data = f.read()

nums = re.findall(r"\d+", data)
N = int(nums[0])
e = int(nums[1])
c = int(nums[2])
print("n = ", N)
print("c = ", c)
print("e = ", e)

m, exact = iroot(c, e)
if exact:
    m_int = int(m)
    m_bytes = m_int.to_bytes(
        (m_int.bit_length() + 7) // 8,
        "big"
    )
    print("\nFLAG:")
    print(m_bytes.decode(errors="ignore"))
else:
    print("[-] No es raíz exacta")