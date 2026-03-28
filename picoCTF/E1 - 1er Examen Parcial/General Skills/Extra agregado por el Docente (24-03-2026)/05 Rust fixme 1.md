**Challenge**
	
**Description**
	Have you heard of Rust? Fix the syntax errors in this Rust file to print the flag!Download the Rust code [here](https://challenge-files.picoctf.net/c_verbal_sleep/3f0e13f541928f420d9c8c96b06d4dbf7b2fa18b15adbd457108e8c80a1f5883/fixme1.tar.gz).
	**Hints**
		1. Cargo is Rust's package manager and will make your life easier. See the getting started page [here](https://doc.rust-lang.org/book/ch01-03-hello-cargo.html)
		2. [println!](https://doc.rust-lang.org/std/macro.println.html)
		3. Rust has some pretty great compiler error messages. Read them maybe?

**Solution**
	1. Descargar el archivo del sitio.
	2. Extraer la carpeta donde se encuentra el proyecto.
	3. Buscar errores en el código, arreglarlos.`**
		Cambios principales:
			- **Faltaba `;`**
			    let key = String::from("CSUCKS");
			    Antes no terminaba la línea.
			- **`ret;` → `return;`**
			    if res.is_err() {  
			        return;  
			    }
			    `ret` no existe en Rust.
			- **Formato de `println!`**
				println!("{}", ...)
		<script class = "Error correction">
			use xor_cryptor::XORCryptor;
			
			fn main() {
			    // Key for decryption
			    let key = String::from("CSUCKS"); // ← faltaba ;
			
			    // Encrypted flag values
			    let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59", "63", "e1", "61", "25", "7f", "5a", "60", "50", "11", "38", "1f", "3a", "60", "e9", "62", "20", "0c", "e6", "50", "d3", "35"];
			
			    let encrypted_buffer: Vec<u8> = hex_values.iter()
			        .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
			        .collect();
			
			    let res = XORCryptor::new(&key);
			    if res.is_err() {
			        return; // ← era "ret"
			    }
			    let xrc = res.unwrap();
			
			    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
			    println!(
			        "{:?}", // ← formato correcto
			        String::from_utf8_lossy(&decrypted_buffer)
			    );
			}
		</script>
		Cambios clave:
			- errores de sintaxis (`;`).
			- palabra clave (`return`).
			- formato de impresión (`{}` en lugar de `:?`).
	1. Instalar `Rust` si no se le tiene:
		- `sudo apt update` ← Actualizar ya que podría pasar que no instale por eso.
		- `sudo apt install rustc cargo -y`
	2. Dirigirse hacia la carpeta donde esta el proyecto:
		<script class = "CLI kali-linux">
			┌──(kali㉿kali)-[~]
			└─$ ls
			 Desktop    Documents       fixme1.tar.gz   main.rs    Public      venv
			 disk       Downloads      'fixme2 fixed'   Music      sstv        Videos
			 disk.img  'fixme1 fixed'  'fixme3 fixed'   Pictures   Templates
			                                                                             
			┌──(kali㉿kali)-[~]
			└─$ cd "fixme1 fixed"
			                                                                             
			┌──(kali㉿kali)-[~/fixme1 fixed]
			└─$ 
		</script>
	3. Ejecutar el proyecto:
		<script class = "CLI kali-linux">
			┌──(kali㉿kali)-[~/fixme1 fixed]
			└─$ cargo run
			    Updating crates.io index
			  Downloaded either v1.13.0
			  Downloaded crossbeam-utils v0.8.20
			  Downloaded xor_cryptor v1.2.3
			  Downloaded crossbeam-deque v0.8.5
			  Downloaded crossbeam-epoch v0.9.18
			  Downloaded rayon-core v1.12.1
			  Downloaded rayon v1.10.0
			  Downloaded 7 crates (379.2KiB) in 5.32s
			   Compiling crossbeam-utils v0.8.20
			   Compiling rayon-core v1.12.1
			   Compiling either v1.13.0
			   Compiling crossbeam-epoch v0.9.18
			   Compiling crossbeam-deque v0.8.5
			   Compiling rayon v1.10.0
			   Compiling xor_cryptor v1.2.3
			   Compiling rust_proj v0.1.0 (/home/kali/fixme1)
			    Finished `dev` profile [unoptimized + debuginfo] target(s) in 17.46s
			     Running `target/debug/rust_proj`
			"picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}"
		</script>
	4. Bandera: `picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}`.

**Notes**
	

**References**
	