def decode_a1z26(texto):
    resultado = ""
    
    for num in texto.split():
        if num.isdigit():
            n = int(num)
            if 1 <= n <= 26:
                resultado += chr(n + 64)  # Convierte a letra mayuscula (A=1 → 1+64=65 → 65=A en ASCII)
            else:
                resultado += "?"  # Por si hay numeros fuera de rango
        else:
            resultado += num  # Conservar simbolos como }

    return resultado


mensaje = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"
print(decode_a1z26(mensaje))