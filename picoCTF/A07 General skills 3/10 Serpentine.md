**Reto**
	
**Descripción**
	Find the flag in the Python script!
	[Download Python script](https://artifacts.picoctf.net/c/35/serpentine.py)

**Solución**
	1. Usando terminal de Windows y VSCode
		PS C:\Users\luise\Downloads> py .\serpentine.py
		C:\Users\luise\Downloads\serpentine.py:38: SyntaxWarning: invalid escape sequence '\ '
		  '''
		
		    Y
		  .-^-.
		 /     \      .- ~ ~ -.
		()     ()    /   _ _   `.                     _ _ _
		 \_   _/    /  /     \   \                . ~  _ _  ~ .
		   | |     /  /       \   \             .' .~       ~-. `.
		   | |    /  /         )   )           /  /             `.`.
		   \ \_ _/  /         /   /           /  /                `'
		    \_ _ _.'         /   /           (  (
		                    /   /             \  \
		                   /   /               \  \
		                  /   /                 )  )
		                 (   (                 /  /
		                  `.  `.             .'  /
		                    `.   ~ - - - - ~   .'
		                       ~ . _ _ _ _ . ~
		
		Welcome to the serpentine encourager!
		
		
		a) Print encouragement
		b) Print flag
		c) Quit
		
		What would you like to do? (a/b/c) b
		
		Oops! I must have misplaced the print_flag function! Check my source code!
		
		
		a) Print encouragement
		b) Print flag
		c) Quit
		
		What would you like to do? (a/b/c) a
		
		-----------------------------------------------------
		Keep it up!
		-----------------------------------------------------
		
		
		a) Print encouragement
		b) Print flag
		c) Quit
		
		What would you like to do? (a/b/c) b
		
		Oops! I must have misplaced the print_flag function! Check my source code!
		
		
		a) Print encouragement
		b) Print flag
		c) Quit
		
		What would you like to do? (a/b/c) c
		PS C:\Users\luise\Downloads>
		PS C:\Users\luise\Downloads>
		PS C:\Users\luise\Downloads> py '.\10 serpentine.py'
		C:\Users\luise\Downloads\serpentine.py:38: SyntaxWarning: invalid escape sequence '\ '
		  '''
		
		    Y
		  .-^-.
		 /     \      .- ~ ~ -.
		()     ()    /   _ _   `.                     _ _ _
		 \_   _/    /  /     \   \                . ~  _ _  ~ .
		   | |     /  /       \   \             .' .~       ~-. `.
		   | |    /  /         )   )           /  /             `.`.
		   \ \_ _/  /         /   /           /  /                `'
		    \_ _ _.'         /   /           (  (
		                    /   /             \  \
		                   /   /               \  \
		                  /   /                 )  )
		                 (   (                 /  /
		                  `.  `.             .'  /
		                    `.   ~ - - - - ~   .'
		                       ~ . _ _ _ _ . ~
		
		Welcome to the serpentine encourager!
		
		
		a) Print encouragement
		b) Print flag
		c) Quit
		
		What would you like to do? (a/b/c) b
		picoCTF{7h3_r04d_l355_7r4v3l3d_ae0b80bd}
		
		Oops! I must have misplaced the print_flag function! Check my source code!
		
		
		a) Print encouragement
		b) Print flag
		c) Quit
		
		What would you like to do? (a/b/c)

**Notes**
	1. Reto basado en análisis estático de Python.
	2. La flag estaba dentro del script.
	3. La función print_flag no se ejecutaba.
	4. Se revisó y modificó el flujo de ejecución.
	5. Se hizo la llamada a la función.
	6. Refuerza comprensión de flujo y lectura de código.

**Referencias**
	