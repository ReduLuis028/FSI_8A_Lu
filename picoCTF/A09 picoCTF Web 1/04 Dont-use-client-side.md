**Reto**
	
**Descripción**
	Can you break into this super secure portal?http://fickle-tempest.picoctf.net:51325

**Solución**
	1. Se accede al sitio utilizando el navegador Chrome.
	2. Se inspecciona el código fuente (F12 → Sources).
	3. Se localiza el archivo JavaScript encargado de validar el login. 
	4. Se observa que la validación de usuario y contraseña se realiza completamente del lado del cliente.
	5. Analizando el código, se identifica directamente la flag dentro del script.
		<script type="text/javascript">
			  function verify() {
			    checkpass = document.getElementById("pass").value;
			    split = 4;
			    if (checkpass.substring(0, split) == 'pico') {
			      if (checkpass.substring(split*6, split*7) == 'eb02') {
			        if (checkpass.substring(split, split*2) == 'CTF{') {
			         if (checkpass.substring(split*4, split*5) == 'ts_p') {
			          if (checkpass.substring(split*3, split*4) == 'lien') {
			            if (checkpass.substring(split*5, split*6) == 'lz_2') {
			              if (checkpass.substring(split*2, split*3) == 'no_c') {
			                if (checkpass.substring(split*7, split*8) == 'b45}') {
			                  alert("Password Verified")
			                  }
			                }
			              }
			            }
			          }
			        }
			      }
			    }
			    else {
			      alert("Incorrect password");
			    }
			  }
		</script>
	1. No fue necesario realizar fuerza bruta ni explotación adicional.
		picoCTF{no_clients_plz_2eb02b45}
**Notes**
	

**Referencias**
	