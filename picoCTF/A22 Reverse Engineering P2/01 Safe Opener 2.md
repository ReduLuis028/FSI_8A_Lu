**Challenge**
	
**Description**
	What can you do with this file?
	I forgot the key to my safe but this [file](https://artifacts.picoctf.net/c/288/SafeOpener.class) is supposed to help me with retrieving the lost key.
	Can you help me unlock my safe?
	**Hints**
		1. Download and try to decompile the file.

**Solution**
	1. Download the file and analyze it ith windows integrated tools:
		1. `Get-ChildItem -Path "the path to the file.class or folder"`:
			- Lists files and folders.
			- Similar to `ls` in Linux.
			- `-Path` specifies where to search.
		2. `-Recurse`:
			- Performs a recursive search.
			- Also searches inside subfolders.
		3. `-File`:
			- Includes only files.
			- Ignores directories/folders.
		4. `|`:
			- Pipe operator.
			- Sends the output of the command on the left to the command on the right.
			- Similar to passing data between commands.
		5. `Select-String "picoCTF"`:
			- Searches for the string `"picoCTF"` inside the files received from the previous command.
			- Similar to `grep` in Linux.
	2. So the complete command: `Get-ChildItem -Path "." -Recurse -File | Select-String "picoCTF"`.
		- means:	Search through all files in the current folder and its subfolders for any text containing `picoCTF`.
	3. Run the previous command to get the following output:
		![[Screenshot 2026-05-06 213341.png]]
	4. Flag: `picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_5bfbd6f1}`.

**Notes**
	

**References**
	