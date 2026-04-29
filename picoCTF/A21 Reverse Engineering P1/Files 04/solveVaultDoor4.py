data = "106 85 53 116 95 52 95 98 0x55 0x6e 0x43 0x68 0x5f 0x30 0x66 0x5f 0142 0131 0164 063 0163 0137 040 063 '0' 'd' 'c' '8' '5' 'b' 'e' 'd'"

result = ""

for x in data.split():
    if x.startswith("'") and x.endswith("'"): # char literal
        result += x[1:-1]
    elif x.startswith("0") and len(x) > 1 and x.isdigit(): # octal
        result += chr(int(x, 8))
    elif x.startswith("0x"): # hexadecimal
        result += chr(int(x, 16))
    else: # decimal
        result += chr(int(x))

print("picoCTF{"+ result+ "}")