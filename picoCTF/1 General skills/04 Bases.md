**Reto
	
**Descripción
	What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.
	
**Solución
	1.  Usando código python en terminal de Windows		```
		import base64 as b
		print(b.b64decode("bDNhcm5fdGgzX3IwcDM1").decode())
		l3arn_th3_r0p35
		```
	picoCTF{l3arn_th3_r0p35}
	
**Notes
	1. Solucion 
		import base64 as b
		Carga la librería de Python que sabe codificar y decodificar Base64.
		as b solo es un alias corto.
		b.b64decode(...)
		Toma el texto en Base64 y lo convierte a bytes originales (datos reales).
		Base64 no cifra — solo transforma texto/binario a otro formato.

**Referencias
	