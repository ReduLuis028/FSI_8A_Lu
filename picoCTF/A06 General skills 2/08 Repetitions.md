**Reto**
	
**Descripción**
	Can you make sense of this file?
	Download the file [here](https://artifacts.picoctf.net/c/476/enc_flag).
	
**Solución**
	1. Usando terminal de picoCTF
		   Lui5-picoctf@webshell:~$ wget https://artifacts.picoctf.net/c/476/enc_flag
		--2026-02-11 19:10:20--  https://artifacts.picoctf.net/c/476/enc_flag
		Resolving artifacts.picoctf.net (artifacts.picoctf.net)... 3.170.131.77, 3.170.131.18, 3.170.131.72, ...
		Connecting to artifacts.picoctf.net (artifacts.picoctf.net)|3.170.131.77|:443... connected.
		HTTP request sent, awaiting response... 200 OK
		Length: 349 [application/octet-stream]
		Saving to: 'enc_flag'
		
		enc_flag                    100%[===========================================>]     349  --.-KB/s    in 0s      
		
		2026-02-11 19:10:20 (10.8 MB/s) - 'enc_flag' saved [349/349]
		
		Lui5-picoctf@webshell:~$ ls    
		Addadshashanammu  enc_flag
		Lui5-picoctf@webshell:~$ cat enc_flag
		VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
		RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
		MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
		VkpEVGxaYVdFMVhSbFZrTTBKVVZXMTRWMDVHV2toalJYUlhDazFyV25sVVZXaHpWakpHZEdWRlZs
		aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
		Lui5-picoctf@webshell:~$ 
		Lui5-picoctf@webshell:~$ cat enc_flag | bse64 -d 
		-bash: bse64: command not found
		Lui5-picoctf@webshell:~$ cat enc_flag | base64 -d 
		VjFSQ2EyTXlSblJUV0dSVllrWmFWRmx0TlZOalJtUlhZVVU1YVZKVVZuaFdWekZoWVZkR2NrNVVX
		bUZTVmtwUVdWUkdibVZXVm5WUgpiSEJzWVRCd2VWVXhXbXBOUlRWSFdqTnNWZ3BYUjFKeVZGZHdW
		MlZzVWxaVmJFNW9UVVJDTlZaWE1XRlVkM0JUVW14V05GWkhjRXRXCk1rWnlUVWhzVjJGdGVFVlhi
		bTkzVDFWT2JsQlVNRXNLCg==
		Lui5-picoctf@webshell:~$ cat enc_flag | base64 -d | base64 -d
		V1RCa2MyRnRTWGRVYkZaVFltNVNjRmRXYUU5aVJUVnhWVzFhYVdGck5UWmFSVkpQWVRGbmVWVnVR
		bHBsYTBweVUxWmpNRTVHWjNsVgpXR1JyVFdwV2VsUlZVbE5oTURCNVZXMWFUd3BTUmxWNFZHcEtW
		MkZyTUhsV2FteEVXbm93T1VOblBUMEsK
		Lui5-picoctf@webshell:~$ cat enc_flag | base64 -d | base64 -d | base64 -d
		WTBkc2FtSXdUbFZTYm5ScFdWaE9iRTVxVW1aaWFrNTZaRVJPYTFneVVuQlpla0pyU1ZjME5GZ3lV
		WGRrTWpWelRVUlNhMDB5VW1aTwpSRlV4VGpKV2FrMHlWamxEWnowOUNnPT0K
		Lui5-picoctf@webshell:~$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d
		Y0dsamIwTlVSbnRpWVhObE5qUmZiak56ZEROa1gyUnBZekJrSVc0NFgyUXdkMjVzTURSa00yUmZO
		RFUxTjJWak0yVjlDZz09Cg==
		Lui5-picoctf@webshell:~$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
		cGljb0NURntiYXNlNjRfbjNzdDNkX2RpYzBkIW44X2Qwd25sMDRkM2RfNDU1N2VjM2V9Cg==
		Lui5-picoctf@webshell:~$ cat enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
		picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_4557ec3e}
		Lui5-picoctf@webshell:~$

**Notes**
	1. `base64` se usa para codificar y decodificar datos en Base64.
	2. Sintaxis para decodificar: `base64 -d archivo` o `cat archivo | base64 -d`.
	3. Algunos archivos pueden estar codificados varias veces (nested/base64 anidado), por lo que puede ser necesario aplicar `base64 -d` varias veces hasta obtener el contenido legible.
	4. Se recomienda verificar el contenido después de cada decodificación para confirmar si la flag es visible.
	5. El comando `cat` combinado con `base64 -d` permite procesar la salida sin modificar el archivo original.

**Referencias**