encrypted = "àÒÆÞ¦È¬ëÙ£ÖÓÚåÛÑ¢ÕÓ¨ÍÕÄ¦í"
key = "picoctf"

flag = "".join(
    chr((ord(c) - ord(key[i % len(key)]) + 256) % 256)
    for i, c in enumerate(encrypted)
)
print(flag)