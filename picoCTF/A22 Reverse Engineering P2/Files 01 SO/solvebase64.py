import base64

texto = input("Enter base64 to decode: ")
decodificado = base64.b64decode(texto).decode()

print("picoCTF{"+ decodificado+ "}")