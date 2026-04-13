def load_table(filename):
    table = [] 
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "|" in line:
                row = line.split("|")[1].strip().split()
                table.append(row)
    return table

def decrypt(cipher, key, table):
    result = ""
    for c, k in zip(cipher, key):
        row_index = ord(k) - ord('A')  # fila según la clave
        row = table[row_index]
        col_index = row.index(c)       # buscar letra cifrada
        result += chr(col_index + ord('A'))  # columna = letra original
    return result

table = load_table("table.txt")
flag_encrypted = "UFJKXQZQUNB"
key = "SOLVECRYPTO"

print(decrypt(flag_encrypted, key, table))