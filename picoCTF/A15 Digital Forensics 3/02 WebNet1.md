**Challenge**
	
**Description**
	We found this [packet capture](https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/capture.pcap) and [key](https://challenge-files.picoctf.net/c_fickle_tempest/d1e9add4e31989553f239ebf71ba5972f9bed7bd4932f931e14bfba80d75f815/picopico.key). Recover the flag.
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
		- En la otra lista despegable escoger `Cadena` o `Expresión regular`, y usar la string común de las banderas `picoCTF` o la expresión `picoCTF{.*?}` 
	4. Como se puede ver en la imagen, la bandera ya no se encuentra mas en ese lugar. 
		![[Archivos 02/Screenshot 2026-03-17 215349.png]]
	5. Al analizar un poco el paquete 91, ya que hay varios con coincidencia de la expresión regular, podemos exportar (`Files → Export Objects → HTTP`) el paquete del tráfico a nuestros archivos y verificar su contenido, ya que la bandera no está en texto plano sobre los paquetes en el `.pcap`. 
		<script class="Windows Powershell">
			PS C:\Users\luise\Downloads\Archivos 02> strings .\vulture.jpg | Select-String "picoCTF"
	
			picoCTF{honey.roasted.peanuts}
		</script>
		![[Archivos 02/vulture.jpg]]
	6. Bandera: `picoCTF{honey.roasted.peanuts}`.

**Notes**
	

**References**