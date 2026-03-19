**Challenge**
	General Skills

**Description**
	Can you conjure the right bytes? The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_foggy_cliff/d27c2f999687b0f698327b21bd54e7e34562144d644271562158ba8f615314b0/app.py).
	Connect to the program with netcat:`$ nc foggy-cliff.picoctf.net 57811`
		**Hints**
			1. No copy-pasta, please - use Python!

**Solution**
	1. Comando a utilizar: `(python3 -c "print('e'*1751)"; cat) | nc foggy-cliff.picoctf.net 57811`
	2. Usando terminal de picoCTF
		Lui5-picoctf@webshell:~$ (python3 -c "print('e'*1751)"; cat) | nc foggy-cliff.picoctf.net 57811
		⊹──────[ BYTEMANCY-1 ]──────⊹
		☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
		
		Send me ASCII DECIMAL 101 1751 times, side-by-side, no space.
		
		☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
		⊹─────────────⟡─────────────⊹
		==> picoCTF{h0w_m4ny_e's???_706320e0}

**Notes**
	1. **Proceso Python** (`python3 -c "print('e'*1751)"` → genera **1751 caracteres `e`**):
		- `;`: Indica la ejecución del comando anterior de si mismo (`print(...)`), y después ejecutar el siguiente comando (`cat`).
		- `cat`: Mantiene abierta la conexión para recibir la respuesta del servidor.
		- `|`: Envía la salida al siguiente programa.
		- `nc`: Conecta con el servidor y envía los datos.
	2. El código del reto

**References**
	