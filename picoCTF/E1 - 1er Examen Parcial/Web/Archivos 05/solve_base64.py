import base64

part1 = "cGljb0NURntwcm94aWVzX2Fs"
part2 = "bF90aGVfd2F5X2QxYzBiMTEyfQ=="
decoded = base64.b64decode(part1+part2).decode()

print(decoded)