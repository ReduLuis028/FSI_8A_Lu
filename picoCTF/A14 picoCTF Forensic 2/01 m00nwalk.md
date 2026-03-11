**Challenge**
	
**Description**
	Decode this [message](https://challenge-files.picoctf.net/c_fickle_tempest/816c75fc4b45dfc4ab4c4caad4ac738a3e0cfb3825fedda2a753eb5360c477bb/message.wav) from the moon

**Solution**
	1. Se trato de solucionar leyendo cadenas de texto con la esperanza de encontrar la bandera mediante lo usual
		No fue así ya que solo se encontró esta secuencia de caracteres que nos dice que ahí esta la bandera pero imposible de usar (`CTF0F{CF>�6-t!u}`).
			PS C:\Users\luise\Downloads\exiftool-13.52_64> (Select-String -Path message.wav -Pattern "CTF.*?}").Matches.Value
			CtFlD�=�2C$�����N�g�␦�a���;�R�9ݰ�Ck�+�:.E�J\J�D�9P*�Lv��ڼɞ�q�ܱ���˨���7/E>�H'M�K�DF8�'���2�^���,�緔�'��}
			CtF�G�EIA�9�.U!�Xz�������ᬕ�C�����-���:�L���     ��$g0::�AfG6J4J=GOA�85-��       5��]ԯȇ�<���ֵ��T�~�����S��-�L#�/�:0CTI�L2M�J~E�=�3�'␦�
						���|�{���,���t�     ���
											   ���,�y�%ޣ�B7�#�3IA�K�R+UOP�GZ<f.�
																				�q����γ�␦�S���G�G������e�?����
																											  ��+�8�CL�Q@T�S�P~J�A#6l(��'���̹��=�������}
			CTF~D�>�59* 6r�U�����bӬ�
								   ���.����n������z
												   6�,:J�K�H,A�5�'@�-���Ț�z���/�!���~�4�3��R(E9xG�Q�WBXmSTI~:�'i���#�����F�!�Y�g�{Ȏ�t���␦�->�JnS�W�WeSPK�?�1�!-���ڮ��a�M�_���C���=ܮ��␦�-= =kH}
			CTF0F{CF>�6-t!u}
			CTF�E}
			CTFwF�C�>7      -� =�v����ؼ���D�(�6�A����Γ�R��oO#z+�1O6�8�9Z9=7�3�.�(<!��P���@������տ+����
																									  ����<�����K�"R/;�DLnP}
			PS C:\Users\luise\Downloads\exiftool-13.52_64>
	2. Comando usados para el uso del repositorio de [colaclanth](https://github.com/colaclanth/sstv.git)
		`git clone https://github.com/colaclanth/sstv.git`
		`cd sstv` 
		`sudo python3 setup.py install`
		`sstv -d message.wav -o result.png`
		`display result.png`
	3. Resultados (la bandera es mostrada al final por el comando `display result.png`: `picoCTF{beep_boop_im_in_space}`):
		┌──(kali㉿kali)-[~]
		└─$ git clone https://github.com/colaclanth/sstv.git
		Cloning into 'sstv'...
		remote: Enumerating objects: 221, done.
		remote: Counting objects: 100% (59/59), done.
		remote: Compressing objects: 100% (10/10), done.
		remote: Total 221 (delta 51), reused 49 (delta 49), pack-reused 162 (from 1)
		Receiving objects: 100% (221/221), 1.01 MiB | 910.00 KiB/s, done.
		Resolving deltas: 100% (139/139), done.
		                                                                                                                                                                                                             
		┌──(kali㉿kali)-[~]
		└─$ cd sstv 
		                                                                                                        
		┌──(kali㉿kali)-[~/sstv]
		└─$ sudo python3 setup.py install
		[sudo] password for kali: 
		/usr/lib/python3/dist-packages/setuptools/dist.py:759: SetuptoolsDeprecationWarning: License classifiers are deprecated.
		!!
		
		        ********************************************************************************
		        Please consider removing the following classifiers in favor of a SPDX license expression:
		
		        License :: OSI Approved :: GNU General Public License v3 (GPLv3)
		
		        See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
		        ********************************************************************************
		
		!!
		  self._finalize_license_expression()
		running install
		/usr/lib/python3/dist-packages/setuptools/_distutils/cmd.py:90: SetuptoolsDeprecationWarning: setup.py install is deprecated.
		!!
		
		        ********************************************************************************
		        Please avoid running ``setup.py`` directly.
		        Instead, use pypa/build, pypa/installer or other
		        standards-based tools.
		
		        See https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html for details.
		        ********************************************************************************
		
		!!
		  self.initialize_options()
		/usr/lib/python3/dist-packages/setuptools/_distutils/cmd.py:90: EasyInstallDeprecationWarning: easy_install command is deprecated.
		!!
		
		        ********************************************************************************
		        Please avoid running ``setup.py`` and ``easy_install``.
		        Instead, use pypa/build, pypa/installer or other
		        standards-based tools.
		
		        See https://github.com/pypa/setuptools/issues/917 for details.
		        ********************************************************************************
		
		!!
		  self.initialize_options()
		running bdist_egg
		running egg_info
		creating sstv.egg-info
		writing sstv.egg-info/PKG-INFO
		writing dependency_links to sstv.egg-info/dependency_links.txt
		writing entry points to sstv.egg-info/entry_points.txt
		writing requirements to sstv.egg-info/requires.txt
		writing top-level names to sstv.egg-info/top_level.txt
		writing manifest file 'sstv.egg-info/SOURCES.txt'
		reading manifest file 'sstv.egg-info/SOURCES.txt'
		adding license file 'LICENSE'
		writing manifest file 'sstv.egg-info/SOURCES.txt'
		installing library code to build/bdist.linux-x86_64/egg
		running install_lib
		running build_py
		creating build/lib/sstv
		copying sstv/__main__.py -> build/lib/sstv
		copying sstv/decode.py -> build/lib/sstv
		copying sstv/spec.py -> build/lib/sstv
		copying sstv/__init__.py -> build/lib/sstv
		copying sstv/command.py -> build/lib/sstv
		copying sstv/common.py -> build/lib/sstv
		creating build/bdist.linux-x86_64/egg
		creating build/bdist.linux-x86_64/egg/sstv
		copying build/lib/sstv/__main__.py -> build/bdist.linux-x86_64/egg/sstv
		copying build/lib/sstv/decode.py -> build/bdist.linux-x86_64/egg/sstv
		copying build/lib/sstv/spec.py -> build/bdist.linux-x86_64/egg/sstv
		copying build/lib/sstv/__init__.py -> build/bdist.linux-x86_64/egg/sstv
		copying build/lib/sstv/command.py -> build/bdist.linux-x86_64/egg/sstv
		copying build/lib/sstv/common.py -> build/bdist.linux-x86_64/egg/sstv
		byte-compiling build/bdist.linux-x86_64/egg/sstv/__main__.py to __main__.cpython-313.pyc
		byte-compiling build/bdist.linux-x86_64/egg/sstv/decode.py to decode.cpython-313.pyc
		byte-compiling build/bdist.linux-x86_64/egg/sstv/spec.py to spec.cpython-313.pyc
		byte-compiling build/bdist.linux-x86_64/egg/sstv/__init__.py to __init__.cpython-313.pyc
		byte-compiling build/bdist.linux-x86_64/egg/sstv/command.py to command.cpython-313.pyc
		byte-compiling build/bdist.linux-x86_64/egg/sstv/common.py to common.cpython-313.pyc
		creating build/bdist.linux-x86_64/egg/EGG-INFO
		copying sstv.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
		copying sstv.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
		copying sstv.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
		copying sstv.egg-info/entry_points.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
		copying sstv.egg-info/requires.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
		copying sstv.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
		zip_safe flag not set; analyzing archive contents...
		creating dist
		creating 'dist/sstv-0.1-py3.13.egg' and adding 'build/bdist.linux-x86_64/egg' to it
		removing 'build/bdist.linux-x86_64/egg' (and everything under it)
		Processing sstv-0.1-py3.13.egg
		Copying sstv-0.1-py3.13.egg to /usr/local/lib/python3.13/dist-packages
		Adding sstv 0.1 to easy-install.pth file
		Installing sstv script to /usr/local/bin
		
		Installed /usr/local/lib/python3.13/dist-packages/sstv-0.1-py3.13.egg
		Processing dependencies for sstv==0.1
		Searching for PySoundFile
		Reading https://pypi.org/simple/PySoundFile/
		Downloading https://files.pythonhosted.org/packages/2a/b3/0b871e5fd31b9a8e54b4ee359384e705a1ca1e2870706d2f081dc7cc1693/PySoundFile-0.9.0.post1-py2.py3-none-any.whl#sha256=db14f84f4af1910f54766cf0c0f19d52414fa80aa0e11cb338b5614946f39947
		Best match: PySoundFile 0.9.0.post1
		Processing PySoundFile-0.9.0.post1-py2.py3-none-any.whl
		Installing PySoundFile-0.9.0.post1-py2.py3-none-any.whl to /usr/local/lib/python3.13/dist-packages
		Adding PySoundFile 0.9.0.post1 to easy-install.pth file
		detected new path './sstv-0.1-py3.13.egg'
		
		Installed /usr/local/lib/python3.13/dist-packages/PySoundFile-0.9.0.post1-py3.13.egg
		Searching for scipy==1.16.3
		Best match: scipy 1.16.3
		Adding scipy 1.16.3 to easy-install.pth file
		detected new path './PySoundFile-0.9.0.post1-py3.13.egg'
		
		Using /usr/lib/python3/dist-packages
		Searching for numpy==2.3.5
		Best match: numpy 2.3.5
		Adding numpy 2.3.5 to easy-install.pth file
		Installing f2py script to /usr/local/bin
		Installing numpy-config script to /usr/local/bin
		Installing f2py3 script to /usr/local/bin
		Installing f2py3.13 script to /usr/local/bin
		
		Using /usr/lib/python3/dist-packages
		Searching for pillow==11.3.0
		Best match: pillow 11.3.0
		Adding pillow 11.3.0 to easy-install.pth file
		
		Using /usr/lib/python3/dist-packages
		Searching for cffi==2.0.0
		Best match: cffi 2.0.0
		Adding cffi 2.0.0 to easy-install.pth file
		
		Using /usr/lib/python3/dist-packages
		Searching for pycparser==2.23
		Best match: pycparser 2.23
		Adding pycparser 2.23 to easy-install.pth file
		
		Using /usr/lib/python3/dist-packages
		                                                                                                        
		┌──(kali㉿kali)-[~/sstv]
		└─$ sstv -d message.wav -o result.png
		[sstv] Searching for calibration header... Found!    
		[sstv] Detected SSTV mode Scottie 1
		[sstv] Decoding image...   [######################################################################] 100%
		[sstv] Drawing image data...
		[sstv] ...Done!
		                                                                                                        
		┌──(kali㉿kali)-[~/sstv]
		└─$ display result.png

**Notes**
	

**References**
	https://github.com/colaclanth/sstv