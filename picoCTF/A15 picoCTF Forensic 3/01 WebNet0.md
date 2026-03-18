**Challenge**
	
**Description**
	We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/66113619363fca174ef6bf56587007af1626f99c44fc5cf92333f9fd8876ce9a/capture.pcap) and [key](https://challenge-files.picoctf.net/c_fickle_tempest/66113619363fca174ef6bf56587007af1626f99c44fc5cf92333f9fd8876ce9a/picopico.key). Recover the flag.
	**Hints**
		1. Try using a tool like Wireshark.
		2. How can you decrypt the TLS stream?

**Solution**
	1. - **Abrir el `.pcap` en Wireshark**:
	    - Wireshark te permite ver todos los paquetes de la captura. Busca la sesión TLS (normalmente TCP puerto 443).   
	2. **Configurar la clave privada para descifrar TLS**:
	    - Ve a **Edit → Preferences → Protocols → TLS**.
	    - En **(Pre)-Master-Secret log filename**, o **RSA keys list**, agrega la clave que te dieron (`picopico.key`).
	    - Esto permite a Wireshark desencriptar la comunicación TLS y mostrar el contenido real.
	3. Hacer una búsqueda (`Edición → Buscar siguiente` o `Edit → Find next`):
		- Un vez en la búsqueda, de la lista despegable escojer `Detalles de paquete` o `Packet details`.
		- En la otra lista despegable escoger `Cadena` o `Expresión regular`, y usar la string común de las banderas `picoCTF` o la expresión `picoCTF{.*?}` ![[Archivos 01/Screenshot 2026-03-17 211613.png]]
		- Un vez encontrada la bandera, copiarla: `Pico-Flag: picoCTF{nongshim.shrimp.crackers}\r\n`, ![[Archivos 01/Screenshot 2026-03-17 211825.png]]

**Notes**
	

**References**