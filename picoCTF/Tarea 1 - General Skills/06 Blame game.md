**Reto**
	
**Descripción**
	Someone's commits seems to be preventing the program from working. Who is it?You can download the challenge files here: [challenge.zip](https://artifacts.picoctf.net/c_titan/156/challenge.zip)

**Solución**
/		1. Descomprimir el archivo 06 challenge.zip
/		2. Usando terminal de Git haciendo clic derecho sobre la carpeta > Mostrar más opciones > Open Git Bash here
		luise@CANGURO028 MINGW64 ~/Downloads/06 challenge/drop-in (master)
		$ ls
		message.py
		
		luise@CANGURO028 MINGW64 ~/Downloads/06 challenge/drop-in (master)
		$ python message.py
		  File "C:\Users\luise\Downloads\06 challenge\drop-in\message.py", line 1
		    print("Hello, World!"
		         ^
		SyntaxError: '(' was never closed
		
		luise@CANGURO028 MINGW64 ~/Downloads/06 challenge/drop-in (master)
		$ python message.py
		Hello, World!
		
		luise@CANGURO028 MINGW64 ~/Downloads/06 challenge/drop-in (master)
		$ git branch -a
		* master
		
		luise@CANGURO028 MINGW64 ~/Downloads/06 challenge/drop-in (master)
		$ git log
			commit 83afd3ebd7899251a19d290df92fd1bfc9998adb (HEAD -> master)
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 760de15c177831fee8b2965e57d1461423ad5ed0
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 7fce0961829b0262ed95799aa430822cac6c6a0b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit daa2679f1c00642ef399fadcd52cf8f9c16020f7
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 7b07ab4c87df7198ce8c0ece9f67e8b7f1ddb9f8
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit ce6f53e9ec9c806561d26d7dde9fa2be8631a39f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 81e4152cf926c532e66d48bc4080c552d6bb5541
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit c5834754acc74e7d59d0176d60b733c45bda9391
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 6a25a3c73308327cff74f10ce4b9dd808115a62c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 02499e54a508323d04b7670c1a9e571ee0c7517e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 14cc9e58d2500cf54cfe8cdea72f1eb74798b81b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit fcfdde9f250d79cfcb8588e791c0bb106f58482d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 9d6900b4f5ad96d5062ab380a0dda051aee524f5
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit e49962325d383e0518cb6f642bc958eeea5dcf44
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit a4b3d2b8824b740ed953d075386d711c73b32854
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit ec0cdccf53214eab5cbd1d32d862a73f06626eb1
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 605855f88e18b2409b2873b1714b5a5340f4f813
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 35384c4191e95df15c5013e96d0f3c08e4e62581
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 0e8044c974d374da58c57e893859fb7e7de67e06
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit dc7e53c13e059fc056de93a3080b30dab7411094
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 63e646ae7b5dfe90c27d894f139b92894fde65f3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 30b85c2403c181af6dd21a66548cbb18c11d87ed
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit d1888cc55894783ea338f16dd1832730400ad4bb
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 3c8c74d5b5a56df1e119cc1fc260c62ded9c0b22
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit d7e9b11c91f4de0d2e480b1557760e2d42517aae
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 6867b21ce694b4acf219a3c6a47a046a2e59e618
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 3ca1d5815a2e95eac036e91616890983ffcf33d3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 496c762a6419416a7ef6f6c275d55605db48ef11
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit e7f50ebba8ddcfaf0dfbff81b3446e25f6bda915
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 0ddd949eacec4e9daa11c5e9a5cb9a50380b3a07
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit c8c8ae56a4f045d6e87f9bb4a8ac330019e159ca
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit ad94de975ec615172ae44dab5be9443d1c894d1d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit de6c5c82ba39044f44e79891eeccd49450812288
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 513665aa48b01f5747b2f34f749d2b830efb91b4
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 21d4a3dde629753ecfd38346420547ea643e87e1
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 33bcd035facd7d9364e934fb0734812668438b1e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit b51b3ebd3e860373e6a0953b64b61df7f928f11a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 87d6565c324848a213af9b94e2ce5e668a8fc937
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit e6505ae13ee3d62b42a94fdedba7f9629e8d520c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 8b51b6bf698127731b445f4394df111f73bce3b2
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 8ab037b22fa61eec531426ea44f081daeb159131
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 0d65996c785bc860418f56f6f712109fe587c09d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 0161d322ddddc2d23d6cad6799af52cb5059ed9a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 3d84800ffc2cc9fa0f087a424a2520fdf11b9866
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 5ff461c9a95801707b47055069baededc390660c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 7433ee6df4847cdfb7bad696b52315cdb4a7b2d5
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit c6cc2e5a33a25c16fc65fb6785c293369cb3de75
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 70b3ac0bd852632b8d8c788a999ede156a4af507
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 6a182edb2f025dac8fab965df371537dc18ec9b4
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 89714c9a0f192e3abb92d5586e6c3f5101ed6d05
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit a4d8f41fa8623213feca94707bc03a177ede82ce
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 1a06523c02fba860c1be68827a933b45117eb802
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 71e05a97b634d57644bf251fe43ecc942fa6a0da
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit e51d32633beadeeca26a5cb18af7b3e99665d1e5
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 3fbef3b5dd68768654aeec16744c9e0bc12ffbb1
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 583a47701a8badd0c5ec416a21d2bd2d3ade2000
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit a3db66430e6ea01acada1ea7cbca8d547cb6ec7b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 656740265d69e1423978f262de49f4e182534d93
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit bdada7fdcc4913a38483fd95e46f385a3fc5a6e4
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit c42c337327988e30c9a8669faa489711b3953ffc
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 73d12b1b4873e64d47d3e0a7a61448b26063f5ff
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 360003d08af0e97a5aeeecd6ee8c8feb99930751
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit de552a35cd2e41ed3b0c8b74bf2961bb1ae2a11f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 0815f74c95ee97ac0742894933a9922e6053217f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit cf59664e63e822839cc06787fdb6196ef49d4e5f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 88858e113a5b8344303fabb490be78d289fb9424
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 9449de6dad2cf42be8c069c104abda578a58632b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 732a508bcc65bca91f3d79474b0ac69ead19b807
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit fe0b8a27315b8c12d834684008ab9e0e7aa55f97
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 25aef724e519dc90ba0f4ce563a5b1cce520f866
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 63d93bcfb162b8aa36fd63a96551fb7f179c1a41
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 8bc37ecbf3111e3443e7faa1d9252ae830761a0c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 109322a0bb5ff9d75f54ec7ce12d30d30ec947c4
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit cb9e1e8a1a6415e31ba9b492be5d9fe3e7843142
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit ce1d652b6357bb28d8abab9c18eb66dee872cbc4
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 806140942d819acfeafe91db0513f6d0c9526200
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit a1e649fdb94e20539859336e53cdc34f1a6bd0b2
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 93423f6b84cb97ac1200d484b9f0be8bbdcb747b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 0714febe2c46c0efa2c6158d7df399e66259503a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 411e2c3d89127a186e1b5dfc5a7a07104b0ca2aa
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit fbf18d83a0faefcade318e533717fc84e353c6b7
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit da244f007c0f7dd7e041a5470d5420cc943c3528
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 9d472cd2c1ce8ea1fd923055a1b124496d3b7387
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 7f9b362dffff60244d6c6ea5cbd81d1f94a7e341
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 71272f61dbc439b173c1ce33a64b5e4909873974
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 33739f904587abca17c57bb8c3a0432e7b529567
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit c9547cf5797546e954faee403a435d50d2cfdb9a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit f0a10c73e61bba2465bff0cd6863fa8a914be422
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 652f905fca479fe4341f3634fe75b0f5aca97df3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 1dd0d1b517b7fa5a58eb1f9b117def2ec3e0eeb4
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 62a39a60a673e45414d0aa9ae413c199795b1ec5
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 3905f28d75d451277b9b11761fb2780776ad8d3d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 98e529b3ef32a247ce6d7bf3369e072ed2dcd6f0
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 94bfb421ce7bdabbe3edaa110e8038e460141cde
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit bcc27c2a8b36559170c09fccfa555b3c25ed6856
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 10d0e8b6829aa2f593c3ff604f9813739edd94f8
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit ee67c9547d2c8841c9251f553d79783dfa0c3101
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 481d5517762affe5a6f062c48f7e5f1985db8439
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 4f15b1164844bbbc80c6cb83ab40c663e592e470
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit c079bc6679d81f57116f1c62cf42b6a71ffd583d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 61273a764174ec148e9f2bc6eecac42d849ee7e2
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 311e5e36b8b41877bfc4301cae7aaaca016b22e2
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit d269c22aeb0c03957bd29bf946d6c52bf116ddc0
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 000396c41fe7eca59a3e0cebb881844ff040deb0
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 78220c4a98ea5f7a037f4d8ea65032335dae38c6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit f31c4ce1589475893b844c85789bf336bcf34ff7
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit c2ddc4893a9d3f61c56d106b6a3e6857c153019f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 37cb743a7f4961e1eb2ee272840657f2a93c123e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 4b364c303491c99f89d561cd51ed1f614b389406
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit a7f11487a1b60a78f4a9676f93f32ab2d4930d3d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit dd9c9e3224d67b2b4f838ffa3953f323fef93602
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 47c87fa7df99d5d207b697c62a80fef0274144e7
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 20435e5bafe6c0ccd3a17fc549ebba803042d005
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 94581be25ce1d19e80da64c8ccf92edde27efbb3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 6464624ff01129be96516644bd213c5c98fcc7f8
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit c4c65dfff9ead1be42d13c376f68c3293fbdaa76
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 3f7cf2193f22e6e45e57fd9ced6af558a4d4c073
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 5133e7bbc71fadf7b0ce1d274eb37663da32abcb
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit f32e6edadd158d57dbfa83a2293ca98ae895f5b2
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit afb1076ca2bccdd05166cd577225f6388e39faf3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 86554b4817f114e56dec415ca177a2ecfab428a1
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit d9e27a077685a9f6d1f2c71942f5e31be8b950c8
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 1dec70d0ad4cfd2d49b5a77eddca7dce6487891f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 3fce43d997412ca1b11eb09c6bf0db41f8dc8750
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit d8789d1566847f0d6e863055afa3f7487a25a982
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 105cf5c2e744f9b72855f1a44a4d940dc5050e4f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit d5b075fceb6731f85d2585c04ce814a64f40d10d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 511048a5deb7290efd06bf9405e2ac3d66eef4a5
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 1db4fb419558c24883ef7f786be1e105c0c6f689
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit f00929942cfb15118ed78e916c7dd725082afa61
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit fa9ac839dce34b3c3da92912f359be94545612eb
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 3f5f8a6ca4ebe583bf768cbc4edf63a5316f2339
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 749be1fa6a0d7c8f2816de8fdd7c1edcbdfc1034
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 8d20698d769e99811b4adaec71b5cef827b0b91b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 6d21e86806be9ce3ea095ea5147a1d244d52d18f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 1a9ceebfdf60111aa350a13df2ef488da710b164
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 88a19bb2fc3c69ba2365f6f67df8eb8d0b7423dd
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 7203df485ba624dcf1f2e6ec491b28ebbe86ed63
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit a33d08d89e415af4684cb4553250f28102222bf0
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit abacade7685f7d0687a5362e3247a6cdf8736518
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 86a92a81f5da7fdbc91cc5564834c88fd31343a9
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 1dd699822006a5d6f2fdf4c9f2df90eda8406c0a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit ecbdc2267bde765ea984f2552a5f42cf46fe7593
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit d456ee934adce20f53b625afb9bab358457fb820
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit f258369ade82931c11ac6f22282da5bd6ac5e7df
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit f1d6772dabb689dd0af57bc610b1153dc5bdc53a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit b4fd6667f4c9d2f436b8c45e98c4be4ee65d206d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 19ea6e5c3aa76f5781075931b11d2878b5b55975
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 230e19ea7e0c97465d715b669b594eed4581f129
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 1032d9e17a66107602271fb8e7c956b622881510
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 1fc2820d7dd66932fb76250b843161c1b8cb6b27
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 524c786d0320832da6ca5a96b6d7a29a4df05218
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 5e1bce0c1c0051848c0234a30f7bc4499ff86e4b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 0279f59f64b004a1fe3d96de13653c28fd5dac81
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 427bcf1263d604dbe6a1407f915596cde3b8be1a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:03 2024 +0000
			
			    important business work
			
			commit 750fc695c74f38a9eb9971e3d900ad2f7c404e41
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 6c9420eb4a93d77597746c7369b5e6ce2991b983
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 4802fdf9ceeb056a9efbd9156762ae44b5f737ea
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 035844015e31edaba5f5583a41a03502867e44f5
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit c25b7fb62cd3d1023773af7ca513a59460af575d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d8ec1cd74a7792153251200e8c269a4325c7f375
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 6695daccbd08b9d29bcda0aea4cd8d563bceba79
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 030a7d31d9c93e2cd9b11e1606de28931b21ef85
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 298185e692073b1c4283ed6119bee535a5988700
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 2c8684771d82b5a85451af646d32196fa049554f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 0d1cadaa84db4ceca5ba78e894c91c2b3e273894
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 386fa704fa9c2e9bf069da7b26161163861bcacf
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit cfe7d0e61ea293588732de7d72ccca048c78b5d6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit eb6b0301d52e482bbadae89cacd082a61633e147
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 2330525570a3e6aaa3fa5278242a9d881ae93f2f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit c48b2098fd23e7ab9e73d6e5fc311873a993c9e8
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 2baab6dac5d9573d66054357f56c05bbd81161e9
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit b9183acb329a01720c75d45ef8d8a3a608f64c33
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit f71cb53197ac5c3d97adc4612c10d2a5d3d647a2
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 7d5f037093aa415f01b944523264b0becb9424ca
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 0f18c5fb852e7f266583b5e33ee525e7c8754796
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 7aa2fe0a8a7db97bd9c0d12e9ef0234cba8237f6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 740698315bb86feaf54a7a32129b791ee3b5bb05
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 959e7016de0c3817c3558a7e88298411c474f209
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 5821005817899807a4a9aa587d0673c3417cc63e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d573cac8a55157eb76420056e1fa2978c9238dd8
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit c69d63742c6e41e1eb29bf7271ac25ff584840e8
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit a862cc256de3464d3a4cc6ef62d479dc30893ab4
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 3cec5c072757a3fe15769be15d092f19c7abfa77
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 4a77e8d1b00bc3022112174b9444b11120c0a6c1
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit f218c31112da55774b2bd24ad0abf085e56deab7
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d913b322cc24ab48d29221b87c5d45aa53931fea
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 5e5b7ed2d987f620afe90c05410f958dbb98b1c7
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 8f1a531b9727806ffee6e2cccf435932ea0c7277
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 627ae222573016e2a68c9af9bbb3f28ce38524e8
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 0ae2c20b984df347f188e0d6194dc936c41df9fd
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit dab725886bb898e02016f8a5ecac4b871df0b2b9
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 9629d0121d94518ffc04cb9e18b43a473a7951e5
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 0d563c60f0b951712484a9f65f76e22f21662dd5
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit ed34f61f6859864e2323fac16a8aaead36f0dd06
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit ede189520ba37a28b2afa96d79fd4f0d1365f5bc
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 70e6493f0ef78e15f8dcd1824f96be39c9d59436
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 2ed34ed3ba9f9d3858ed270a97a7c8ade12a05fc
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 9620975364c438fb50d7251a8cfac19ebbcf1270
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit da2dfd9b83c8604e96bad58db2069cb2915a0f23
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 747bc33d0ac1b730746ccb6a8c32ea7365bfb784
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 224b4553044be5d006e75c800d2f33ffab1be9be
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit b74adf6f0c5593d84e44ff93d5888b00c8d841ea
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 82877978fa2ce4be2f522b6aefabf1d6fa46e020
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit cddb5bc19078920cb1f7375f3ec1790ba95fe916
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit c39c05c9e6fcdd2a814dfcb47886b1efc379c5c6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 646d07734539e9c9e14172d325de47b9a380e883
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 620c425368acf84943506af6a4f86bb082ddefa4
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit c4de9a36a286c010c992dc65b1328ba18f42f4ed
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 859210072b6f82dfafe46a121ea54f4731268025
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 4d2c7171d691d104cb4bf5c4b492f9150c478ec4
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit aaeb431511ac543f064d4a24d5b63aa780a628e3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 9f4c7a00b29b8f4b29fb3d8df3a96a111b263564
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit b43a07874a75b9d5b6ebebe5fd11f70b004af412
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 20738ab0f06bcf96c9433009d8a33baefe914133
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 1fdc31a57f626c359cf982d898d9760f8ac13796
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d46d7d9b83d7991a10b1d90e1fd9e1fc4d0cf52f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 4fffd2407d6d816a548539caf7fc67d6b94daa8b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d1735be68a51639179970005b8a34973cf05ad0a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit c706f898939266bec62617ef4d7b1e8d70c412db
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit cd579e40b7bfab9dfa1e8b6a856b8bde67f2fde4
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 7539a3ba72316daca20e6cb0beaa50b56a508383
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 038c5fdbabca039bb1f5bdcc5e797f20559849bf
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit dd41e12e090617cd0280a1f696355c4542e1c21e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 57bc4a2acbb551006d4a9708a62a5ee408d0d62e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 85be16a43dba6e5ac4e847d6636efed64190fe20
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit e81e6bcc8ab8576b0d631939af92ee12adef0417
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 8823281a3def013f312a03d3f1921c5c79d360ac
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 8bb20667a788c270e9ff986db2946096935a3c25
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit fa68ddff1dfc58ccb1ca6f9b8cecbc0780a84987
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit a18ca9f049e71428ded1d5df44fc691fcf028e72
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit cd30a7917e72c8f2a6a51dccb50abcfa35307bb3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 2aae8541c10bd11ca1382a91093e04754643e05d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 5a4e4109fea76626c7fc5f2e005642e42fd0372b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 7957add3f504c01d4e83d0c8afb9604f6060ef67
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit f266d8fbbeb46bab8116657eb371e9e24fdaade6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 82a3ca37870a4eaaa641aa44acdfcbf2a1ff9a3b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 1139e16a7b9c083e35cf4a859adab672b913e002
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit a890540617fcffbd083239d8622951e4c6e41fb6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 943d94d8def387d5b95e6e7e1f7e4d5e9a57423b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 24941d7f558bae997a9a213a0e7c5f113550b157
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 41da1de30b028f70d6ceb823afec8be06efbcf1d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit a38f282b2de507dc4739adda9b67b8025686cf70
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 36dfe7d632af6936e6133f94e8a63f4c0d363216
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 294e484accc167bcf1a76975277d29310c77255a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 43d3ea4a03c609a6b003a2af64ac42bbd3315562
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 52a2dbe6767e6beede90760417be7c443744b417
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 4bd698eb663e434e557b828fbf9ddb4c09e8e9cf
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d9b09f51f77c9d28ed2092f78107a31eabfc83ab
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit db46b7fd3d7e84e14ef3e012d4ceefd33d881b39
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 67c3344e1d877143cc5dfb3f64182c8c98419b14
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 067f7f50faaede22eb60904e43777396a15ad14c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 337bd1a8c1775472fc5b0607df9714876d718c7c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit a7baddaf838a0c8a5fda116f6ad38c38f13f1081
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit b8cb06118a37d81490690c2650a083403b90671b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 8b00187a5d07787d8d5a4057194e41b499c53f8e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 2745fde56b1d435d83ffca04dc1a79994dcb4925
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit b52cd3c7c8197eae5120afd3c13dfe6c2536f79e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 144d12adbf3c22e06d312d34d3c5843d06901ba3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit dced0cfd27fb94b5f986c0de870a2896bef72bb3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 3c29af0e7cfda45fde7eb09bb211973e06b2ae33
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d9af92ed97ef5b75dd25c5f91f0763414147743b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 49d3e301eb986aa7dcaf2d1875106df4181fb94b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 1680f951637a9a7fe75f5ed39f0d4ad0e891d819
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 4f4d7834425c7d3963fc5c5b2255735e22b3f214
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 30a7a62cb5307f1cbb5b650e732523812a8b604b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 6cc4d10ee892173f080c694e9336d076729748be
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d54cc74b29ba4b6b09e7bc80f9ff09c4594bb259
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 3c9cd4abfcd7b2fa824d64b452223f5b8cdc52cf
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 4bc214bd68c2a9570bfaf0a63ddde79b111c877d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit b60beaed49a06a2509b491df8c073c8dfb805532
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 72c79ee91847a7ea6e5c110df5793f1679261963
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 2d27e889181f94d324039de0d16218194643c540
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 6d48350e999ee8557510cb1b8c0584735fcb914b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 7b65f90f35f153970c6b63e92c59349d01840857
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d0ecabbdf715ae0dee60d2a15bfe180d76a2833f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 38f1ce2262404fa236cf166da5f871b38667bfb5
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 1e8ec77adeac62557081f960e25d1c0a9dd4a3ed
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 9e22b92eb8cc9343134ea004ae904321cafbd1e3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit e5497aaf5cfa6f056e38386363989473e0615c01
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 7f1ac4a9bceb21c4c8bafe015d9b93e6d853458e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 86896d22032e9c3c4c9b3409d0163371f348cbd6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 3045d45b8dd721305e211e4244bc6aecceb74529
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit a4176be7c3cefeaa15236bd3cbbc8e1d208a9ed8
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 1673ebccab094ccb379f15c485301b280315cf7a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit f65928b1c22a7e41f11b448a42215f5734ab7b2d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit c16b5c3d155e5e9bdeef4fec1c410af45aff1e44
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 89262c0fb9de09aa91f6d5347340c8b1bd61f406
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 420dfd0fc57e7fdedfb031b778b45cc9cda80bf5
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit c9181034fb284d37bd66b8d1b691bc3c27f65406
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 2d3e6daa934f574e1dde41bc9d4399a47e109c44
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d2e5ff039725c8f76a0e9461d096230a2fe55670
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit fe3d0fbb6ccb588a0603b2f1f2dae7c87fc2f56f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 50f1d276c31c3b1e6d0291786019774bb03233af
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 49ce002ba8fb98a5dc05b6f27d642fbdfc9c42c6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit a107648986ab625f13062ed58264570064f950fc
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 86d0767ef70d4dcdfbceec49c0ad67936b120b8b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 54e1bed7078bb4ad8a987376892ae64e203d06e6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit bce8f39ac9a69868049012338dc4c8296e4f623a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 5733e0ad6d5e4fcca9063c9badfb9359f61668bd
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit e440e02991e349f7c13397645b7d98765933a084
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit dec2002d2036507348342b04205cd3fab7e39e16
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 51099f062760e99d36c7ec9d01c8dbdf6d232283
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit b60be0de2a754871c3796781513918286d23ee0a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit f029e88bad67702a2a117f7a30f6482b8a948b88
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 307502dfb9306c5fec51a597de2d2ca1ed23e773
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 6da99773ee2617f0f9bbbc0b57cea0e5184e025f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit f85ab915802ee930b1bce84d892479d1d4566fff
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 35922a6fc51314d5aafe3a69766d7d548816ab54
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 40d1c42399ce42e3f719ea6c7ae850e8efcc1158
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit bfec1ab902d392c523dfd8f0389da7101a3df590
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 1de4b82bbeacb5edbe245c590317637b99de5cc3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit f0fdfaa95df8017c7fb0795981a6ee1209b6c5ac
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 651c2c70c3c109088e9bd57fca7474114850484a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 3b39dd769fc042aebb667e1993f89d7251e67b4c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 199d82c4609b4fc3686a98269522fd2bff024694
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit a60fdd5b28683c99c4244c2f5d8dfe90bc986f08
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 47130ae52657a968a8d8a84fd115bbb52942eca8
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit cab8973d95b9b7c3f4c54d8582a887e074d822e2
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 6f767649533c587c470f006c1930933f4a440369
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 5228f2896117ecd3714e99f19de32ee1a8431440
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d1f927a0a89c90db7db1f62b3ce79dceeed8e7f5
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 23226f6213947d854dc5c7c451a1bd338734c064
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 55097ec95a04953389a22c87b88c71e4392e0d9c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit ae1949ae7494253b166d064a02ad0c9de327417c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit a2a158aa64a7574f83499b4f9668a008809f4d8e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit e59d10793523ec8f45e456b95572bd2fcc1a6369
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 6722ab2776d5c5f52851189400d24a5e030f59a4
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 999588f4074ce7c64c98c489beb6770aee510820
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 7c5b2be6df0f169f8e2a186a9b060ade42376968
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 00e70c2bef6c829a8e26858ed5538bf9a0f6f213
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 58ba70a4449294031069281c406bbb468ffe0dea
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 7d1cc1089b04e7cf3b54cee283f401a92bebbc93
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit c11a4b792ce1e386a9253170ebaf5b3d7fd69b0a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit b67264882abb7dc240777f4f39776fb49efa81a9
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 0c80c083000eb91c8ce33cd75a938a4da7b1df21
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d2e66e9a79bec239df44bb96fe63ea11c4edb76f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit f5dbf98d10c8bc05b0e540b79023b0ed0c43c3c5
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit cae9807e28ebfe05cd22a73a2978764d11e0cc3d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit ae28f5297ebbb7f1e8cc5c6c1ebbd41967880622
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 8580628877deebc89a4618214fca1b015447f385
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 3cf8611f15284203ef2fcfa89c946a806d92797e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 39ce04d2d9c43157f6ce30915112a68fe7fbc4cb
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 23c691f9bcb93f68ddd6a44ad0cc39b2d3924c7f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 1732c216a23775dfba97c452e311729b03a8844a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit ce6a5607da49bda8b7646b89ead429522856ed63
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 0900af189e0130912dc5895135bcf541dc0746b7
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 0cc513d3ee2eccc25ef4f0641183a4905673111b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 1069c7ea1ee3075928b106045fb3307eba88284e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit f156a18594b34537136868e572aa27b8dccc1d75
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit b3f367a047022b145535f9fcf90ca22952adda8b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 22a825f785bd10273245e213e25662667ed6d739
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit e678b5b77271877ae37813be010b855cf742b7ea
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit aebb62dfc5497587efa82a46231a9477d2ae33dc
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit badf77963931b03fea174ed5894b3ad4647f1990
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit a74ec8e41684ac918d25fd8df6b360fcf5acb80b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 820da46c3b39508031fccdd48959a4c6e2f4746b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 2e9d8465093fe57c776b8f608aac5de7a2b86ff5
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 3db9fb1cfb8b79353f31dfa356898638dd54ae3d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 6453f410f66e44255c67aa33f43c7319cf69f7f1
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit e24685b1081230a478f4c38e614e35a44e55af48
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d6f93c6a0c6ab403cb74bbd6014bf9c77b132700
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit f36846bd686d5ca4c455164eb6852fa0a1dd02c8
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 791f430998944eff16b7880c6eaa23af84c9d551
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit c458ed5b31711300b0153222a77a415597db1306
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 466406ed399a34e9aa9b80e5dc36ad9b7009cd73
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 29fab23c2a0309d200f63d0515f68501f9fb250a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit cd1b9e494388ed5fa959fd9a317f4e5674789c22
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 3dd074f935b828e3d08164213bd6b663cd541cf6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit ecee200d29023efdc86fd6c4a4be2e4c704e918f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d8e5a46232cfdb3014a4114b50b8014806502408
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 23aca33e84b21812f6bc0fe18871cb08221d702f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 2ce7605934a3ff72c2f5354f9d8bde6511ab893a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit c2b2612d1569be43005b68d5fd00a45fb7c90efb
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit a5029161764ff49079755e057ced6c6185f012dc
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit febc7772bcc0fe8e0c52999496500e98f2484530
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 518940d437a4465227e3e2d8feafffe1127fb735
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 9c3e2f1c14ed4f3d7549a3e1ee3241c5c13f1a41
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 3e58d336be29db913a73ac6ddcafe415e120658b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 9242a7064e25ebbbfb79494535c0639338ab1b44
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit e741094e3c729cf5a1d7462d40e58d91a720948a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 5dff1aa9c6df7af6bbc045e6eb16216c8416ae1f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 3044c50b2e542533e701a5e47fc2767ff133b0b9
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 5757c959ecaad73a518a49dbd73637867714d02c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 685eb6bd23198e7141ab7d03eada60870ad0fd0d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 00cb9df10127d569a63db3e086c2458e7ce43910
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 939ed4c981861d98e1f1f4d908188d61be5f2ea1
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 6a3d5d6fc418dd1cecf97b6fba35e0abe2c01acb
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 8b2211e1adffdeebe9cca2141a5ee869350e1d17
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 9a3cfcca625f54d4a0484f8a745fcaa59eb6fa1e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit daf41f0db48ba7c562593a9fb7281a710bab5df1
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 8570fe4bcb8860e1efc1ac2a35335d321071e8b9
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 7688bb891ac820f30d1287045f1068506a0af062
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 7a8d775d90a9e80929eb4b0f74071e17d8ef7647
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit fca0cb3973c025a07522fdabe7bc78bc5923e9b1
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d35ac157f085cd59ba255c8aaacaa338d90b3231
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 46743047185907246f702cf61a0f25afa4966628
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 92473e0880882908d1d1e30c79505f90087a1a5d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit ba8d405fdd5aa2bbb1a6fe523b4ac8dd0cb99b98
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 9580bd60a08b8d58961663fa272ee77fbcc3602b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit d33ebd51a7f3b2f1b9a87d76bbba58da1d827f7c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 6ba4f51af15e51973f3173c881631695eea7fb47
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 66ad16fd5fe23088c64b5a8a10527818a643314b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit fb5369165ba4ca38331080d8b5c8f3d92942403d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:02 2024 +0000
			
			    important business work
			
			commit 200d1e6e0f7a804dfb04ad1bd19816898a3e9585
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 9dbdac6b9babb5755cc80c45e3117f2e53bbdd02
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 41770734d3833e36e07ae6625d2414a56ef93617
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 7c6a1e24f9d6ac6713169eeb7f8565f0625fe4e6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 1d18bc09fb5db254e61d29c3f616c6db17964b79
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 4f7480055d5d283867bf01a726feee15c4f04323
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 5ccafea1a7e3e0d3cbdd289c849521c850d68550
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 26338f32441e0c7fb5537285ace55cdc1cd34a04
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit da1e6c11dfe308ee2c17b587e3a23d01a3b4153f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 97732b67241405f8ba9d0177ab03ea29a146641a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 8a727ff4e33ecd952829e1e114a9952b51b8702f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 9eebc4d708f5f9a03d2be564b33bf7c84c0d5faa
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 5df2814da1025808e44243ce667b764ec91f593e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 7a6c91368e6b8c31213cc966009651c37adbda1f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit b0b3d73da882fd2be00abaef037fb8c5a6b08575
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit b9fd00c439163202540ad3368e6eefe6079bb7d9
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 9a3bddb6c3d5fc2e28b3840f390e770c4e57c32f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 5f3c38747a714c4a758501d2d375120b799bfb4e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit b05adca218d715b6c9faddfa686a86441f52d821
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 687c77b303f14961f6ab8151f6d56083215ccb7f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 1b2e4338560dd672775b293d1b90ebbcab359bdc
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 9e91af2f0bd20b272df401065d9ae4a1f6583c5a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 414b553ff6b000d029c5e2435f6f6aeea0a306bb
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 4cea521d1cc778068c79309b20183917fc623a27
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 4a4e2fbd7ff4cc80a8226caed7fc7895085018b4
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit d2a3ad1a2118653e70463980dcc009261ced82cf
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 6e4ab90df97c19671f9042280290b678e8cc5454
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit d5998bd47fe66c7477d7bcfb0172f712cf5fdfda
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit cf8bfee7c365fdfe5f1be87c889b9d4c4507a6c6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit e6079bf284f4a21ec9b8aec1b629d7ccd9c74f8b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 912ab03fca6c7e041b769165e1f604f386bb1efb
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 3b52ab121ec29d0fb814245d4414ee5e12badbbe
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 378c110c3dc1d2122b76be9af6465ba0db78a182
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 5f6dd70ca788c49c240b3742420039c2637fe252
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 48b1ddcdb2066d54c156b8e8e3267db0212b4ff9
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 17cd84e5c5d3ba3a4a51064b4597eb09b82ec26a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit a93ff73809c72e20c2b4847394fa2bf86db718d3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 958649f80c8d4bed80045a28f6f4fb71e9af7bba
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 255a8bf698b075f245f31a85222e2dd063f1bfa9
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit d56e2beaff8ae2aa3373d2adeaf9adce4a78a2db
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 56c2ce35f87151ab37491ad7efeb93289af617ae
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 85a7e94c77beaab305d6aca7176257c46e63d579
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit a34af5664d391a6086fbe53c0887c4c773b5a3fd
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 94bd75264cbd5e071e7a1c042a13e8d254fff052
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit fd48d9152fda60eda1fb169e7cc515d98cabf706
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 06d9cba8e70ee59c287d5785774181d18531a27f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit a91fedfe9b9870dc3ea77853ed96df8201a8d870
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 2a8abf753b4e72c1aa2c6d7d1d83fb046d28f02c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit ec596b4c531e75382d629720e505552bf1dac5ad
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 6fdb818a8a8af9fadf77e4d3a30c5a956a67c3e6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 6dd7a6d43fc32226e696b50ef5f208d2c40e5cf1
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 32d31696f6920b8dae3e5efd0c5b51436a0ff42b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit fd9bb51bd1774202a631fe09652e0107d60eed57
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit cb1c9738b82739b0f46b35fd2a14a6cfa3976a6d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 077f45173e350e43bdcc7ca5d5ac0249ab495b98
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 9e2dc8c3351552b7e7f85da06b90d5f32314c246
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 36f100c1969b890b00f2d0528e598631ae1bfb5a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 4eeb57eeaf57a8552e332ef326ae5ae73d9e4e4d
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit b794d40c25c15abb385052c3cc8015c9ad9e0e8c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit eff0df02794d6c422b9e35dac8144e5d3f529b4b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 92186d670432af21c01f0671d2d0f767b949839e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 6aa5ca19e27bc41f9ae9c60e4fb997da554ebd53
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 2be103fb2fe27e49fd9e78266cf102d470979c7e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit edb8b028ec6acaccb54467629b8c9b47d96711e4
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 36ea5ed2584bf453fc3ab6222f9c7f21399bb6c3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 8d60a995f27039a0b82a99ded600f56c24eb11a0
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 8a29eb72fd27eac0a285d1dde5afff56c93a41b3
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit e4fb43c6c8c0025949a96a6d0fec38a3e3044253
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 4ff91e620a731beb6fbd5588246a071883a773a9
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit d6a409ae83e57bc103913b32a68f61857de70ca8
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 87d54ea3eddbeda99c2129e696d330466d94488a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 6bf4296a8d00c429441101e5cbb73e4e6f450365
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 4f572b2cb8915c572639078c941095a3f979c7dc
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit cd9b4c693914a152e72df9a487f9e18901ea52d0
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 8d7e2560e2875a838df78a07791593aa1b4a54de
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 3445cc01ea9619efb1acd4ea2ed19b5c3ede1575
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit c4d3161c744c6bd98aa31dfc8f78758388ab4e1a
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 990abed5ec7dee6dca94488aafb18397bc4ca308
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 4f3be9994bc1b1e0897a63a1c1d510b38ca429af
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 99b6913dff8f6db06eaa7c6232f463851010fac0
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 7d7cf365cd307150330caa5133758bea85cf4883
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit d15d44e6ce2002079450d61e69287ffa7a647ac6
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 83564cdca0807081ce90bee34f0aa2a21efd8b05
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 5d25de27ee9e62fcdceb7836cd2ed9ef52afef60
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 11a7fed8b1378b536cbc6b4ac6559df7ee8fdf82
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit c6a97da550b7881a6268955b1fe2cb0c52f935ed
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 051a7f3057a1a0113171368f0a5795f2845cb604
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 5a703de1b0ca3ddccdf5aa74e5ba9398cdb63167
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 231d857c28689db5a06b64d0096069973c27de4c
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 496f9a952ea27cf4e702ab604b0d3339164f173b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit b4ccf566d5aa54607fc656272f00fd5e29b24070
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit fdb14c072a0f1e483d795aab6371bdb5d4b40c9e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 4edee9486bba6fa754781d02371a8c845df267d0
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit a6ff118a4f2e4ac926c5e34c581d05ca15c44b69
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 9500034198652af0286003cf435c22b769be8c4e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 7d97835ff37464c00cfc2089b2d7e8ea54b6e13f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 0351e0474493168ca76441c24630c17554fd09ca
			Author: picoCTF{@sk_th3_1nt3rn_d2d29f22} <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    optimize file size of prod code
			
			commit c9e851509190f5887e91339ee18087e3e77ebfda
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    create top secret project
			
			    important business work
			
			commit 496f9a952ea27cf4e702ab604b0d3339164f173b
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit b4ccf566d5aa54607fc656272f00fd5e29b24070
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit fdb14c072a0f1e483d795aab6371bdb5d4b40c9e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 4edee9486bba6fa754781d02371a8c845df267d0
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit a6ff118a4f2e4ac926c5e34c581d05ca15c44b69
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 9500034198652af0286003cf435c22b769be8c4e
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 7d97835ff37464c00cfc2089b2d7e8ea54b6e13f
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    important business work
			
			commit 0351e0474493168ca76441c24630c17554fd09ca
			Author: picoCTF{@sk_th3_1nt3rn_d2d29f22} <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    optimize file size of prod code
			
			commit c9e851509190f5887e91339ee18087e3e77ebfda
			Author: picoCTF <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    create top secret project
		
		luise@CANGURO028 MINGW64 ~/Downloads/06 challenge/drop-in (master)
		$ git log --oneline
			83afd3e (HEAD -> master) important business work
			760de15 important business work
			7fce096 important business work
			daa2679 important business work
			7b07ab4 important business work
			ce6f53e important business work
			81e4152 important business work
			c583475 important business work
			6a25a3c important business work
			02499e5 important business work
			14cc9e5 important business work
			fcfdde9 important business work
			9d6900b important business work
			e499623 important business work
			a4b3d2b important business work
			ec0cdcc important business work
			605855f important business work
			35384c4 important business work
			0e8044c important business work
			dc7e53c important business work
			63e646a important business work
			30b85c2 important business work
			d1888cc important business work
			3c8c74d important business work
			d7e9b11 important business work
			6867b21 important business work
			3ca1d58 important business work
			496c762 important business work
			e7f50eb important business work
			0ddd949 important business work
			c8c8ae5 important business work
			ad94de9 important business work
			de6c5c8 important business work
			513665a important business work
			21d4a3d important business work
			33bcd03 important business work
			b51b3eb important business work
			87d6565 important business work
			e6505ae important business work
			8b51b6b important business work
			8ab037b important business work
			0d65996 important business work
			0161d32 important business work
			3d84800 important business work
			5ff461c important business work
			7433ee6 important business work
			c6cc2e5 important business work
			70b3ac0 important business work
			6a182ed important business work
			89714c9 important business work
			a4d8f41 important business work
			1a06523 important business work
			71e05a9 important business work
			e51d326 important business work
			3fbef3b important business work
			583a477 important business work
			a3db664 important business work
			6567402 important business work
			bdada7f important business work
			c42c337 important business work
			73d12b1 important business work
			360003d important business work
			de552a3 important business work
			0815f74 important business work
			cf59664 important business work
			88858e1 important business work
			9449de6 important business work
			732a508 important business work
			fe0b8a2 important business work
			25aef72 important business work
			63d93bc important business work
			8bc37ec important business work
			109322a important business work
			cb9e1e8 important business work
			ce1d652 important business work
			8061409 important business work
			a1e649f important business work
			93423f6 important business work
			0714feb important business work
			411e2c3 important business work
			fbf18d8 important business work
			da244f0 important business work
			9d472cd important business work
			7f9b362 important business work
			71272f6 important business work
			33739f9 important business work
			c9547cf important business work
			f0a10c7 important business work
			652f905 important business work
			1dd0d1b important business work
			62a39a6 important business work
			3905f28 important business work
			98e529b important business work
			94bfb42 important business work
			bcc27c2 important business work
			10d0e8b important business work
			ee67c95 important business work
			481d551 important business work
			4f15b11 important business work
			c079bc6 important business work
			61273a7 important business work
			311e5e3 important business work
			d269c22 important business work
			000396c important business work
			78220c4 important business work
			f31c4ce important business work
			c2ddc48 important business work
			37cb743 important business work
			4b364c3 important business work
			a7f1148 important business work
			dd9c9e3 important business work
			47c87fa important business work
			20435e5 important business work
			94581be important business work
			6464624 important business work
			c4c65df important business work
			3f7cf21 important business work
			5133e7b important business work
			f32e6ed important business work
			afb1076 important business work
			86554b4 important business work
			d9e27a0 important business work
			1dec70d important business work
			3fce43d important business work
			d8789d1 important business work
			105cf5c important business work
			d5b075f important business work
			511048a important business work
			1db4fb4 important business work
			f009299 important business work
			fa9ac83 important business work
			3f5f8a6 important business work
			749be1f important business work
			8d20698 important business work
			6d21e86 important business work
			1a9ceeb important business work
			88a19bb important business work
			7203df4 important business work
			a33d08d important business work
			abacade important business work
			86a92a8 important business work
			1dd6998 important business work
			ecbdc22 important business work
			d456ee9 important business work
			f258369 important business work
			f1d6772 important business work
			b4fd666 important business work
			19ea6e5 important business work
			230e19e important business work
			1032d9e important business work
			1fc2820 important business work
			524c786 important business work
			5e1bce0 important business work
			0279f59 important business work
			427bcf1 important business work
			750fc69 important business work
			6c9420e important business work
			4802fdf important business work
			0358440 important business work
			c25b7fb important business work
			d8ec1cd important business work
			6695dac important business work
			030a7d3 important business work
			298185e important business work
			2c86847 important business work
			0d1cada important business work
			386fa70 important business work
			cfe7d0e important business work
			eb6b030 important business work
			2330525 important business work
			c48b209 important business work
			2baab6d important business work
			b9183ac important business work
			f71cb53 important business work
			7d5f037 important business work
			0f18c5f important business work
			7aa2fe0 important business work
			7406983 important business work
			959e701 important business work
			5821005 important business work
			d573cac important business work
			c69d637 important business work
			a862cc2 important business work
			3cec5c0 important business work
			4a77e8d important business work
			f218c31 important business work
			d913b32 important business work
			5e5b7ed important business work
			8f1a531 important business work
			627ae22 important business work
			0ae2c20 important business work
			dab7258 important business work
			9629d01 important business work
			0d563c6 important business work
			ed34f61 important business work
			ede1895 important business work
			70e6493 important business work
			2ed34ed important business work
			9620975 important business work
			da2dfd9 important business work
			747bc33 important business work
			224b455 important business work
			b74adf6 important business work
			8287797 important business work
			cddb5bc important business work
			c39c05c important business work
			646d077 important business work
			620c425 important business work
			c4de9a3 important business work
			8592100 important business work
			4d2c717 important business work
			aaeb431 important business work
			9f4c7a0 important business work
			b43a078 important business work
			20738ab important business work
			1fdc31a important business work
			d46d7d9 important business work
			4fffd24 important business work
			d1735be important business work
			c706f89 important business work
			cd579e4 important business work
			7539a3b important business work
			038c5fd important business work
			dd41e12 important business work
			57bc4a2 important business work
			85be16a important business work
			e81e6bc important business work
			8823281 important business work
			8bb2066 important business work
			fa68ddf important business work
			a18ca9f important business work
			cd30a79 important business work
			2aae854 important business work
			5a4e410 important business work
			7957add important business work
			f266d8f important business work
			82a3ca3 important business work
			1139e16 important business work
			a890540 important business work
			943d94d important business work
			24941d7 important business work
			41da1de important business work
			a38f282 important business work
			36dfe7d important business work
			294e484 important business work
			43d3ea4 important business work
			52a2dbe important business work
			4bd698e important business work
			d9b09f5 important business work
			db46b7f important business work
			67c3344 important business work
			067f7f5 important business work
			337bd1a important business work
			a7badda important business work
			b8cb061 important business work
			8b00187 important business work
			2745fde important business work
			b52cd3c important business work
			144d12a important business work
			dced0cf important business work
			3c29af0 important business work
			d9af92e important business work
			49d3e30 important business work
			1680f95 important business work
			4f4d783 important business work
			30a7a62 important business work
			6cc4d10 important business work
			d54cc74 important business work
			3c9cd4a important business work
			4bc214b important business work
			b60beae important business work
			72c79ee important business work
			2d27e88 important business work
			6d48350 important business work
			7b65f90 important business work
			d0ecabb important business work
			38f1ce2 important business work
			1e8ec77 important business work
			9e22b92 important business work
			e5497aa important business work
			7f1ac4a important business work
			86896d2 important business work
			3045d45 important business work
			a4176be important business work
			1673ebc important business work
			f65928b important business work
			c16b5c3 important business work
			89262c0 important business work
			420dfd0 important business work
			c918103 important business work
			2d3e6da important business work
			d2e5ff0 important business work
			fe3d0fb important business work
			50f1d27 important business work
			49ce002 important business work
			a107648 important business work
			86d0767 important business work
			54e1bed important business work
			bce8f39 important business work
			5733e0a important business work
			e440e02 important business work
			dec2002 important business work
			51099f0 important business work
			b60be0d important business work
			f029e88 important business work
			307502d important business work
			6da9977 important business work
			f85ab91 important business work
			35922a6 important business work
			40d1c42 important business work
			bfec1ab important business work
			1de4b82 important business work
			f0fdfaa important business work
			651c2c7 important business work
			3b39dd7 important business work
			199d82c important business work
			a60fdd5 important business work
			47130ae important business work
			cab8973 important business work
			6f76764 important business work
			5228f28 important business work
			d1f927a important business work
			23226f6 important business work
			55097ec important business work
			ae1949a important business work
			a2a158a important business work
			e59d107 important business work
			6722ab2 important business work
			999588f important business work
			7c5b2be important business work
			00e70c2 important business work
			58ba70a important business work
			7d1cc10 important business work
			c11a4b7 important business work
			b672648 important business work
			0c80c08 important business work
			d2e66e9 important business work
			f5dbf98 important business work
			cae9807 important business work
			ae28f52 important business work
			8580628 important business work
			3cf8611 important business work
			39ce04d important business work
			23c691f important business work
			1732c21 important business work
			ce6a560 important business work
			0900af1 important business work
			0cc513d important business work
			1069c7e important business work
			f156a18 important business work
			b3f367a important business work
			22a825f important business work
			e678b5b important business work
			aebb62d important business work
			badf779 important business work
			a74ec8e important business work
			820da46 important business work
			2e9d846 important business work
			3db9fb1 important business work
			6453f41 important business work
			e24685b important business work
			d6f93c6 important business work
			f36846b important business work
			791f430 important business work
			c458ed5 important business work
			466406e important business work
			29fab23 important business work
			cd1b9e4 important business work
			3dd074f important business work
			ecee200 important business work
			d8e5a46 important business work
			23aca33 important business work
			2ce7605 important business work
			c2b2612 important business work
			a502916 important business work
			febc777 important business work
			518940d important business work
			9c3e2f1 important business work
			3e58d33 important business work
			9242a70 important business work
			e741094 important business work
			5dff1aa important business work
			3044c50 important business work
			5757c95 important business work
			685eb6b important business work
			00cb9df important business work
			939ed4c important business work
			6a3d5d6 important business work
			8b2211e important business work
			9a3cfcc important business work
			daf41f0 important business work
			8570fe4 important business work
			7688bb8 important business work
			7a8d775 important business work
			fca0cb3 important business work
			d35ac15 important business work
			4674304 important business work
			92473e0 important business work
			ba8d405 important business work
			9580bd6 important business work
			d33ebd5 important business work
			6ba4f51 important business work
			66ad16f important business work
			fb53691 important business work
			200d1e6 important business work
			9dbdac6 important business work
			4177073 important business work
			7c6a1e2 important business work
			1d18bc0 important business work
			4f74800 important business work
			5ccafea important business work
			26338f3 important business work
			da1e6c1 important business work
			97732b6 important business work
			8a727ff important business work
			9eebc4d important business work
			5df2814 important business work
			7a6c913 important business work
			b0b3d73 important business work
			b9fd00c important business work
			9a3bddb important business work
			5f3c387 important business work
			b05adca important business work
			687c77b important business work
			1b2e433 important business work
			9e91af2 important business work
			414b553 important business work
			4cea521 important business work
			4a4e2fb important business work
			d2a3ad1 important business work
			6e4ab90 important business work
			d5998bd important business work
			cf8bfee important business work
			e6079bf important business work
			912ab03 important business work
			3b52ab1 important business work
			378c110 important business work
			5f6dd70 important business work
			48b1ddc important business work
			17cd84e important business work
			a93ff73 important business work
			958649f important business work
			255a8bf important business work
			d56e2be important business work
			56c2ce3 important business work
			85a7e94 important business work
			a34af56 important business work
			94bd752 important business work
			fd48d91 important business work
			06d9cba important business work
			a91fedf important business work
			2a8abf7 important business work
			ec596b4 important business work
			6fdb818 important business work
			6dd7a6d important business work
			32d3169 important business work
			fd9bb51 important business work
			cb1c973 important business work
			077f451 important business work
			9e2dc8c important business work
			36f100c important business work
			4eeb57e important business work
			b794d40 important business work
			eff0df0 important business work
			92186d6 important business work
			6aa5ca1 important business work
			2be103f important business work
			edb8b02 important business work
			36ea5ed important business work
			8d60a99 important business work
			8a29eb7 important business work
			e4fb43c important business work
			4ff91e6 important business work
			d6a409a important business work
			87d54ea important business work
			6bf4296 important business work
			4f572b2 important business work
			cd9b4c6 important business work
			8d7e256 important business work
			3445cc0 important business work
			c4d3161 important business work
			990abed important business work
			4f3be99 important business work
			99b6913 important business work
			7d7cf36 important business work
			d15d44e important business work
			83564cd important business work
			5d25de2 important business work
			11a7fed important business work
			c6a97da important business work
			051a7f3 important business work
			5a703de important business work
			231d857 important business work
			496f9a9 important business work
			b4ccf56 important business work
			fdb14c0 important business work
			4edee94 important business work
			a6ff118 important business work
			9500034 important business work
			7d97835 important business work
			0351e04 optimize file size of prod code
			c9e8515 create top secret project
			
			luise@CANGURO028 MINGW64 ~/Downloads/06 challenge/drop-in (master)
			$ git show 0351e04
			commit 0351e0474493168ca76441c24630c17554fd09ca
			Author: picoCTF{@sk_th3_1nt3rn_d2d29f22} <ops@picoctf.com>
			Date:   Tue Mar 12 00:07:01 2024 +0000
			
			    optimize file size of prod code
			
			diff --git a/message.py b/message.py
			index 7df869a..326544a 100644
			--- a/message.py
			+++ b/message.py
			@@ -1 +1 @@
			-print("Hello, World!")
			+print("Hello, World!"
			
			luise@CANGURO028 MINGW64 ~/Downloads/06 challenge/drop-in (master)
			$

	Banderas obtenida:
		picoCTF{@sk_th3_1nt3rn_d2d29f22}

**Notes**
/		1. Cómo funciona el reto:  
		El archivo `message.py` tenía un error de sintaxis que impedía ejecutar el programa.  
		El error fue introducido en un commit específico.  
		El objetivo era revisar el historial de Git para identificar quién hizo el cambio.  
		La bandera se encontraba en el autor del commit que rompió el código.

/		2. Método utilizado:  
		Se ejecutó `python message.py` para detectar el error.  
		Se revisaron las ramas con `git branch -a` (solo existía `master`).  
		Se consultó el historial con `git log` y `git log --oneline`.  
		Se inspeccionó el commit sospechoso usando `git show <hash>`.  
		Se identificó el autor que eliminó el paréntesis en el `print`.

/		3. Resultados:  
		Commit que rompió el código: 0351e0474493168ca76441c24630c17554fd09ca  
		Autor del commit: picoCTF{@sk_th3_1nt3rn_d2d29f22}  
		Bandera obtenida: picoCTF{@sk_th3_1nt3rn_d2d29f22}

/		4. Aprendizaje:  
		Git permite rastrear exactamente quién hizo cada cambio.  
		`git log` muestra el historial de commits.  
		`git show` permite ver qué modificación se realizó.  
		Un pequeño cambio en código puede romper completamente un programa.

**Referencias**
	