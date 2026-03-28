**Challenge**
	
**Description**
	The Rust saga continues? I ask you, can I borrow that, pleeeeeaaaasseeeee?
	Download the Rust code [here](https://challenge-files.picoctf.net/c_verbal_sleep/babfbee79718a6363826ba86300173ffde6d81577e9dd07d4130c53a7eecf6c3/fixme2.tar.gz).
	**Hints**
		1. https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html

**Solution**
	1. Descargar el archivo del sitio.
	2. Extraer la carpeta donde se encuentra el proyecto.
	3. Buscar errores en el código, arreglarlos.
		 Debes usarse **referencia mutable `&mut String`**
		<script class = "Error correction">
			use xor_cryptor::XORCryptor;
			
			fn decrypt(encrypted_buffer: Vec<u8>, borrowed_string: &mut String) {
			
			    let key = String::from("CSUCKS");
			
			    borrowed_string.push_str("PARTY FOUL! Here is your flag: ");
			
			    let res = XORCryptor::new(&key);
			    if res.is_err() {
			        return;
			    }
			    let xrc = res.unwrap();
			
			    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
			    borrowed_string.push_str(&String::from_utf8_lossy(&decrypted_buffer));
			    println!("{}", borrowed_string);
			}
			
			fn main() {
			    let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59", "63", "e1", "61", "25", "0d", "c4", "60", "f2", "12", "a0", "18", "03", "51", "03", "36", "05", "0e", "f9", "42", "5b"];
			
			    let encrypted_buffer: Vec<u8> = hex_values.iter()
			        .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
			        .collect();
			
			    let mut party_foul = String::from("Using memory unsafe languages is a: ");
			
			    decrypt(encrypted_buffer, &mut party_foul);
			}
		</script>
		Cambios clave:
			- `&String` → `&mut String`.
			- `let party_foul` → `let mut part.
			- `&party_foul` → `&mut party_foul.
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
			└─$ cd "fixme2 fixed"
			                                                                             
			┌──(kali㉿kali)-[~/fixme2 fixed]
			└─$ 
		</script>
	3. Ejecutar el proyecto:
		<script class = "CLI kali-linux">
			┌──(kali㉿kali)-[~/fixme2 fixed]
			└─$ cargo run
			   Compiling crossbeam-utils v0.8.20
			   Compiling rayon-core v1.12.1
			   Compiling either v1.13.0
			   Compiling crossbeam-epoch v0.9.18
			   Compiling crossbeam-deque v0.8.5
			   Compiling rayon v1.10.0
			   Compiling xor_cryptor v1.2.3
			   Compiling rust_proj v0.1.0 (/home/kali/fixme2 fixed)
			    Finished `dev` profile [unoptimized + debuginfo] target(s) in 13.56s
			     Running `target/debug/rust_proj`
			Using memory unsafe languages is a: PARTY FOUL! Here is your flag: picoCTF{4r3_y0u_h4v1n5_fun_y31?}
			                                                                             
			┌──(kali㉿kali)-[~/fixme2 fixed]
			└─$ 
		</script>
	4. Bandera: `picoCTF{4r3_y0u_h4v1n5_fun_y31?}`.

**Notes**
	

**References**
	