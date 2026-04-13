**Challenge**
	
**Description**
	Theres tapping coming in from the wires.
	What's it saying nc fickle-tempest.picoctf.net 60540.
	**Hints**
		1. [What kind of encoding uses dashes and dots?](https://en.wikipedia.org/wiki/Morse_code)
		2. The flag is in the format PICOCTF{}

**Solution**
	1. Connect to the server and obtain the following information:
		<script>
			.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .- -.. . ----- ----- ----- ----. .---- }
		</script>
	2. Once connected, copy the previously obtained text.
	3. Decrypt using the following code [[Files 06/decode Morse code.py]]
	4. Alternatively, install the Python package `morse-talk`, using the command `pip install morse-talk`.
		Usando la terminal de picoCTF:
		<script>
			Lui5-picoctf@webshell:~$ python
			Python 3.10.12 (main, Jan 26 2026, 14:55:28) [GCC 11.4.0] on linux
			Type "help", "copyright", "credits" or "license" for more information.
			>>> import morse_talk as mtalk
			>>> 
			>>> morse = ".--. .. -.-. --- -.-. - ..-.  -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .- -.. . ----- ----- ----- ----. .----"
			>>> 
			>>> decoded = mtalk.decode(morse)
			>>> 
			>>> print("PICOCTF{" + decoded[7:] + "}")
			PICOCTF{M0RS3C0D31SFUNADE00091}
			>>> 
		</script>
	5. Flag: `PICOCTF{M0RS3C0D31SFUNAD00091}`.

**Notes**
	

**References**
	