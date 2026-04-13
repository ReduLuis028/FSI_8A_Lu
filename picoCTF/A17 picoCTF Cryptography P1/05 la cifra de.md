**Challenge**
	
**Description**
	I found this cipher in an old book.
	Can you figure out what it says?
	Connect with nc fickle-tempest.picoctf.net 54280.
	**Hints**
		1. There are tools that make this easy.
		2. Perhaps looking at history will help

**Solution**
	1.  Connect to the server and obtain the following information:
		<script>
			Encrypted message:
			Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk
			
			Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd
			
			Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo 
			
			Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3x149hNchj}
			
			Ehk ktryy herq-ooizxetypd jjdcxnatoty ol f aordllvmlbkytc inahkw socjgex, bls sfoe gwzuti 1467 my Rjzn Hfetoxea Gqmexyt.
			
			Tnj Gimjyèrk Htpnjc iy ysexjqoxj dosjeisjd cgqwej yse Gqmexyt Doxn ox Fwbkwei Inahkw.
			
			Tn 1508, Ptsatsps Zwttnjxiax tnbjytki ehk xz-cgqwej ylbaql rkhea (g rltxni ol xsilypd gqahggpty) ysaz bzuri wazjc bk f nroytcgq nosuznkse ol yse Bnretèwp Cousex.
			
			Gplrfdo’y xpcuso butvlky lpvjlrki tn 1555 gx l cuseitzltoty ol yse lncsz. Yse rthex mllbjd ol yse gqahggpty fce tth snnqtki cemzwaxqj, bay ehk fwpnfmezx lnj yse osoed qptzjcs gwp mocpd hd xegsd ol f xnkrznoh vee usrgxp, wnnnh ify bk itfljcety hizm paim noxwpsvtydkse.
		</script>
	2. Once connected, copy the previously obtained text.
	3. Press the `Run autosolver` button ([Vigenere Cipher Autosolver](https://www.boxentriq.com/ciphers/vigenere-cipher#autosolver)):
		![[Files 05/01 Vigenere Cipher - Boxentriq - [www.boxentriq.com].png]]
	4. Una vez hecho, usar el modo `Decrypt` y, utilizar alguna de las claves proporcionadas hasta obtener la `flag`, en este caso fue la clave `GFLA` ([Vigenere Cipher Manual](https://www.boxentriq.com/ciphers/vigenere-cipher#manual)):
		![[Files 05/02 Vigenere Cipher - Boxentriq - [www.boxentriq.com].png]]
	5. Flag: `picoCTF{b311a50_0r_v1gn3r3_c1ph3r149cCcbe}`.

**Notes**
	

**References**
	[Boxentriq](https://www.boxentriq.com/)
	[Vigenere Cipher](https://www.boxentriq.com/ciphers/vigenere-cipher)