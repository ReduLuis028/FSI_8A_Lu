**Challenge**
	
**Description**
	http://wily-courier.picoctf.net:53537/
	**Hints**
		Look at the problem category

**Solution**
	1. Descargar el archivo del sitio:
		- Ya sea dando clic derecho y `Guardar la imagen`.
		- Usando `wget` + clic derecho `Copiar dirección del vínculo`. 
	2. Comandos a usar:
		- `sudo gem install zsteg`
		- `export RUBY_THREAD_VM_STACK_SIZE=500000000`
		- `zsteg concat_v.png`
	3. Una vez hecho, usar CLI:
		<script>
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 01]
			└─$ sudo gem install zsteg
			[sudo] password for kali: 
			Fetching zsteg-0.2.14.gem
			Fetching zpng-0.4.6.gem
			Fetching iostruct-0.7.0.gem
			Fetching rainbow-3.1.1.gem
			Successfully installed rainbow-3.1.1
			Successfully installed iostruct-0.7.0
			Successfully installed zpng-0.4.6
			Successfully installed zsteg-0.2.14
			Parsing documentation for rainbow-3.1.1
			Installing ri documentation for rainbow-3.1.1
			Parsing documentation for iostruct-0.7.0
			Installing ri documentation for iostruct-0.7.0
			Parsing documentation for zpng-0.4.6
			Installing ri documentation for zpng-0.4.6
			Parsing documentation for zsteg-0.2.14
			Installing ri documentation for zsteg-0.2.14
			Done installing documentation for rainbow, iostruct, zpng, zsteg after 1 seconds
			4 gems installed
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 01]
			└─$ export RUBY_THREAD_VM_STACK_SIZE=500000000
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 01]
			└─$ zsteg concat_v.png 
			imagedata           .. text: "\n\n\n\n\n\n\t\t"
			chunk:0:IHDR        .. file: Adobe Photoshop Color swatch, version 0, 1280 colors; 1st RGB space (0), w 0xb9a0, x 0x802, y 0, z 0; 2nd HSB space (1), w 0, x 0, y 0, z 0                                    
			b1,b,lsb,xy         .. text: "picoCTF{imag3_m4n1pul4t10n_sl4p5}\n"
			b1,bgr,lsb,xy       .. <wbStego size=0x941a5b ext=nil data="\xB6\xAD\xB6}\xDB\xB2lR\x7F\xDF\x86\xB7c\xFC\xFF\xBF\x02Zr\x8E\xE2Z\x12\xD8q\xE5&MJ-X:\xB5\xBF\xF7\x7F\xDB\xDFI\bm\xDB\xDB\x80m\x00\x00\x00\xB6m\xDB\xDB\xB6\x00\x00\x00\xB6\xB6\x00m\xDB\x12\x12m\xDB\xDB\x00\x00\x00\x00\x00\xB6m\xDB\x00\xB6\x00\x00\x00\xDB\xB6mm\xDB\xB6\xB6\x00\x00\x00\x00\x00m\xDB" even=true hdr=nil enc=nil mix=true controlbyte="[">                                                                                                   
			b2,r,lsb,xy         .. text: ["U" repeated 8 times]
			b2,r,msb,xy         .. file: VISX image file
			b2,g,lsb,xy         .. file: VISX image file
			b2,g,msb,xy         .. file: SoftQuad DESC or font file binary - version 15722
			b2,b,msb,xy         .. text: "UfUUUU@UUU"
			b4,r,lsb,xy         .. text: "\"\"\"\"\"#4D"
			b4,r,msb,xy         .. text: "wwww3333"
			b4,g,lsb,xy         .. text: "wewwwwvUS"
			b4,g,msb,xy         .. text: "\"\"\"\"DDDD"
			b4,b,lsb,xy         .. text: "vdUeVwweDFw"
			b4,b,msb,xy         .. text: "UUYYUUUUUUUU"
			                                                                                                      
			┌──(kali㉿kali)-[/run/media/kali/ESD-USB/Archivos 01]
			└─$
		</script>
	4. Bandera: `picoCTF{imag3_m4n1pul4t10n_sl4p5}`.

**Notes**
	1. `sudo gem install zsteg`
	    - Instala la herramienta `zsteg` de Ruby, que permite analizar imágenes PNG en busca de datos ocultos en distintos canales de color y bits.
	2. `export RUBY_THREAD_VM_STACK_SIZE=500000000`
	    - Aumenta el tamaño de stack para Ruby. Necesario en imágenes grandes para que `zsteg` no falle al analizar.
	3. `zsteg concat_v.png`
	    - Escanea la imagen `concat_v.png` en múltiples modos (`b1,b,lsb`, `b2,r,msb`, etc.) para buscar texto o archivos ocultos.
	    - Salida importante: `b1,b,lsb,xy .. text: "picoCTF{imag3_m4n1pul4t10n_sl4p5}"`, que contiene la bandera.
**References**
	