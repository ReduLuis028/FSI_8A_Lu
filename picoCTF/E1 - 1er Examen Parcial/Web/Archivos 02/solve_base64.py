import base64

data = "cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzJDODA0MEVGfQ=="
decoded = base64.b64decode(data).decode()

print(decoded)