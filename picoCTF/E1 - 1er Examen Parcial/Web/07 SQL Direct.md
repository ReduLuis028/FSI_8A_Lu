**Challenge**
	
**Description**
	Connect to this PostgreSQL server and find the flag!
	`psql -h saturn.picoctf.net -p 49438 -U postgres pico`
	Password is `postgres`
	**Hints**
		1. What does a SQL database contain?

**Solution**
	1. Conectarse al servidor
	    - Usar `psql` con los datos proporcionados.
	    - Ingresar la contraseña: `postgres`.
	2. Explorar la base de datos
	    - `\l` → Ver todas las bases de datos disponibles.
	    - `\c pico` → Conectarse a la base de datos `pico`.
	    - `\dt` → Listar las tablas dentro de la base de datos.
	3. Encontrar la tabla interesante
	    - Se observa una tabla llamada `flags`.
	4. Consultar la información
	    - `select * from flags;`
	    - Esto muestra todos los registros de la tabla.
	5. Obtener la bandera
		- La flag aparece en uno de los campos (address del primer registro).
	6. Comandos
		`help`
		`\h`
		`\?`
		`\l`
		`\c pico`
		`\dt`
		`select flags`
		`^c`
		`select * from flags;`
	7. CLI:
		<script class = "CLI kali-linux">
			┌──(kali㉿kali)-[~]
			└─$ psql -h saturn.picoctf.net -p 49438 -U postgres pico
			Password for user postgres: 
			psql (18.1 (Debian 18.1-1), server 15.2 (Debian 15.2-1.pgdg110+1))
			Type "help" for help.
			
			pico=# help
			You are using psql, the command-line interface to PostgreSQL.
			Type:  \copyright for distribution terms
			       \h for help with SQL commands
			       \? for help with psql commands
			       \g or terminate with semicolon to execute query
			       \q to quit
			pico=# \h
			pico=# \?
			pico=# \l
			                                                    List of databases
			   Name    |  Owner   | Encoding | Locale Provider |  Collate   |   Ctype    | Locale | ICU Rules |   Access privileges   
			-----------+----------+----------+-----------------+------------+------------+--------+-----------+-----------------------
			 pico      | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | 
			 postgres  | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | 
			 template0 | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | =c/postgres          +
			           |          |          |                 |            |            |        |           | postgres=CTc/postgres
			 template1 | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | =c/postgres          +
			           |          |          |                 |            |            |        |           | postgres=CTc/postgres
			(4 rows)
			
			pico=# \c pico
			psql (18.1 (Debian 18.1-1), server 15.2 (Debian 15.2-1.pgdg110+1))
			You are now connected to database "pico" as user "postgres".
			pico=# \dt
			          List of tables
			 Schema | Name  | Type  |  Owner   
			--------+-------+-------+----------                                                                     
			 public | flags | table | postgres                                                                      
			(1 row)                                                                                                 
			                                                                                                        
			pico=# select flags
			pico-# ^C
			pico=# select * from flags;
			 id | firstname | lastname  |                address                 
			----+-----------+-----------+----------------------------------------
			  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}
			  2 | Leia      | Organa    | Alderaan
			  3 | Han       | Solo      | Corellia
			(3 rows)
			
			pico=# 
		</script>
	8. Bandera: `picoCTF{L3arN_S0m3_5qL_t0d4Y_31fd14c0}`.

**Notes**
	1. `psql`
	    - Cliente de línea de comandos para interactuar con PostgreSQL.
	2. `\l`
	    - Lista todas las bases de datos del servidor.
	3. `\c pico`
	    - Cambia a la base de datos donde está la información relevante.
	4. `\dt`
	    - Muestra las tablas disponibles (estructura de la base).
	5. `select * from flags;`
	    - Consulta todos los datos de la tabla `flags`.
	    - Aquí es donde normalmente se oculta la flag en retos básicos.

**References**
	