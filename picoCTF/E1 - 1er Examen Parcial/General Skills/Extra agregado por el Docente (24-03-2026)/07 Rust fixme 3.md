**Challenge**
	
**Description**
	Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag!Download the Rust code [here](https://challenge-files.picoctf.net/c_verbal_sleep/dcdaf491b35c1d0f5075e9583edbbb7aaea1dffb6ad32bc000e4d87b5200ff7b/fixme3.tar.gz).
	**Hints**
		1. Read the comments...darn it!

**Solution**
	1. Descargar el archivo del sitio.
	2. Extraer la carpeta donde se encuentra el proyecto.
	3. Buscar errores en el código, arreglarlos.
		Solo **descomentar el bloque `unsafe`**:
		<script class = "Error correction">
			unsafe {
			    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
			
			    let decrypted_ptr = decrypted_buffer.as_ptr();
			    let decrypted_len = decrypted_buffer.len();
			
			    let decrypted_slice = std::slice::from_raw_parts(decrypted_ptr, decrypted_len);
			
			    borrowed_string.push_str(&String::from_utf8_lossy(decrypted_slice));
			}
		</script>
	4. Instalar `Rust` si no se le tiene:
		- `sudo apt update` ← Actualizar ya que podría pasar que no instale por eso.
		- `sudo apt install rustc cargo -y`
	5. Dirigirse hacia la carpeta donde esta el proyecto:
		<script class = "CLI kali-linux">
			┌──(kali㉿kali)-[~]
			└─$ ls               
			 Desktop    Documents      'fixme2 fixed'   Pictures   Templates
			 disk       Downloads      'fixme3 fixed'   Public     venv
			 disk.img  'fixme1 fixed'   Music           sstv       Videos
			                                                                             
			┌──(kali㉿kali)-[~]
			└─$ cd "fixme3 fixed"
			                                                                             
			┌──(kali㉿kali)-[~/fixme3 fixed]
			└─$ 
		</script>
	6. Ejecutar el proyecto:
		<script class = "CLI kali-linux">
			┌──(kali㉿kali)-[~/fixme3 fixed]
			└─$ cargo run
			   Compiling crossbeam-utils v0.8.20
			   Compiling rayon-core v1.12.1
			   Compiling either v1.13.0
			   Compiling crossbeam-epoch v0.9.18
			   Compiling crossbeam-deque v0.8.5
			   Compiling rayon v1.10.0
			   Compiling xor_cryptor v1.2.3
			   Compiling rust_proj v0.1.0 (/home/kali/fixme3 fixed)
			    Finished `dev` profile [unoptimized + debuginfo] target(s) in 7.01s
			     Running `target/debug/rust_proj`
			Using memory unsafe languages is a: PARTY FOUL! Here is your flag: picoCTF{n0w_y0uv3_f1x3d_1h3m_411}
			                                                                             
			┌──(kali㉿kali)-[~/fixme3 fixed]
			└─$ 
		</script>
	7. Bandera: `picoCTF{n0w_y0uv3_f1x3d_1h3m_411}`.

**Notes**
	

**References**
	