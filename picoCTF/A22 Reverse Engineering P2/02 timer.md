**Challenge**
	
**Description**
	You will find the flag after analysing this apkDownload [here](https://artifacts.picoctf.net/c/449/timer.apk).
	**Hints**
		1. Decompile.
		2. mobsf or jadx.

**Solution**
	1. Download the file: `wget https://artifacts.picoctf.net/c/449/timer.apk`.
	2. Install the tool we will use: `sudo apt install apktool`.
	3. Decompile as indicated in the `hint`: 
		<script class = 'kali'>
			┌──(kali㉿kali)-[~]
			└─$ apktool d timer.apk     
			I: Using Apktool 2.7.0-dirty on timer.apk
			I: Loading resource table...
			I: Decoding AndroidManifest.xml with resources...
			I: Loading resource table from file: /home/kali/.local/share/apktool/framework/1.apk
			I: Regular manifest package...
			I: Decoding file-resources...
			I: Decoding values */* XMLs...
			I: Baksmaling classes.dex...
			I: Baksmaling classes3.dex...
			I: Baksmaling classes2.dex...
			I: Copying assets and libs...
			I: Copying unknown files...
			I: Copying original files..
		</script>
	4. Then go to the folder `timer` created with the previous command and search for the flag with the coomand:
		- `grep -rni "picoCTF{"`
		<script class = 'kali'>
			┌──(kali㉿kali)-[~]
			└─$ ls                      
			Desktop    Downloads  Pictures  Templates  timer.apk
			Documents  Music      Public    timer      Videos
			                                                                              
			┌──(kali㉿kali)-[~]
			└─$ cd timer
			                                                                              
			┌──(kali㉿kali)-[~/timer]
			└─$ ls
			AndroidManifest.xml  kotlin    res    smali_classes2
			apktool.yml          original  smali  smali_classes3
			                                                                              
			┌──(kali㉿kali)-[~/timer]
			└─$ grep -rni "picoCTF{"
			smali_classes3/com/example/timer/BuildConfig.smali:15:.field public static final VERSION_NAME:Ljava/lang/String; = "picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}"
			apktool.yml:64:  versionName: picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}
			                                                                              
			┌──(kali㉿kali)-[~/timer]
			└─$
		</script>
	5. Flag: `picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}`.

**Notes**
	

**References**
	