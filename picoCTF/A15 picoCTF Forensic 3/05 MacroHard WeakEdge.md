**Challenge**
	
**Description**
	I've hidden a flag in this file. Can you find it? [Forensics_is_fun.pptm](https://challenge-files.picoctf.net/c_wily_courier/d78815176c19ddc85a1388233268d2f4c459fcbbaab197b4a29ebafc88294c54/Forensics_is_fun.pptm)

**Solution**
	1. Convertir el archivo a un `.zip`
		<script>
			PS G:\Mi unidad\Ingeniería en Computación\IC 9no Semestre\Optativa VII Fundamentos de la Seguridad de la Información\FSI_8A_Lu\picoCTF\A15 picoCTF Forensic 3\Archivos 05> mv Forensics_is_fun.pptm archivo.zip
		</script>
	2. Visualizar el archivo que menciona en la descripción del reto `I've hidden a flag` entonces podemos intuir que hay un rchivo llamo `hidden`
		Tomar el contenido y quitar los espacios: `ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ`
		Decodificar lo encontrado Base64: 
			PS G:\Mi unidad\Ingeniería en Computación\IC 9no Semestre\Optativa VII Fundamentos de la Seguridad de la Información\FSI_8A_Lu\picoCTF\A15 picoCTF Forensic 3\Archivos 05\archivo> `[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ=="))`
			flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}
		![[Screenshot 2026-03-18 161210.png]]
	3. O bien usando la terminal de Windows Powershell:
		Comandos:
			- Buscar el archivo `hidden`: `Get-ChildItem -Recurse -Filter hidden`
			- Ver su contenido: `Get-Content .\ppt\slideMasters\hidden`
			- Decodificar Base64: `[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ=="))`
		<script>
			PS G:\Mi unidad\Ingeniería en Computación\IC 9no Semestre\Optativa VII Fundamentos de la Seguridad de la Información\FSI_8A_Lu\picoCTF\A15 picoCTF Forensic 3\Archivos 05\archivo> Get-ChildItem -Recurse -Filter hidden
	
	
			    Directorio: G:\Mi unidad\Ingeniería en Computación\IC 9no Semestre\Optativa VII Fundamentos de la Seguridad de la Información\FSI_8A_Lu\picoCTF\A15
			    picoCTF Forensic 3\Archivos 05\archivo\ppt\slideMasters
			
			
			Mode                 LastWriteTime         Length Name
			----                 -------------         ------ ----
			------     18/03/2026  12:12 p. m.             99 hidden
			
			
			PS G:\Mi unidad\Ingeniería en Computación\IC 9no Semestre\Optativa VII Fundamentos de la Seguridad de la Información\FSI_8A_Lu\picoCTF\A15 picoCTF Forensic 3\Archivos 05\archivo> Get-Content .\ppt\slideMasters\hidden
			Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
			PS G:\Mi unidad\Ingeniería en Computación\IC 9no Semestre\Optativa VII Fundamentos de la Seguridad de la Información\FSI_8A_Lu\picoCTF\A15 picoCTF Forensic 3\Archivos 05\archivo> [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String("ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ=="))
			flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}
		</script>
	4. Bandera: `picoCTF{D1d_u_kn0w_ppts_r_z1p5}`.

**Notes**
	

**References**