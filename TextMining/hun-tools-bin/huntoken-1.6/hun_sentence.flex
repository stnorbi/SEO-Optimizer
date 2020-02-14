%option noyywrap

/* hun_sentence - mondatra bont� sz�r� */
/* 2003 (c) N�meth L�szl� <nemethl@gyorsposta.hu> */

/* 											*/
/*  Makr�defin�ci�k									*/
/* 											*/
/*  WORDCHAR: A szavak az ISO-8859-2 bet�i mellett sz�mokat, pontot,			*/
/*  paragrafus-, fok-, sz�zal�k- �s k�t�jelet, valamint HTML entit�sk�nt megadva	*/
/*  nagyk�t�jelet (&ndash;), valamint kvirtm�nuszt (&mdash;) tartalmazhatnak,		*/
/*  tov�bb� bet�szerepre nem vizsg�lt decim�lis UNICODE entit�st (p�ld�ul &345;).	*/
/*  Az ISO-8859-2 bet�i a locale csomag alapj�n automatikusan lettek kiv�logatva.	*/
/*  Tov�bbi inform�ci�k: man iso-8859-2.									*/

LATIN1 ("&Agrave"";"?|"&Atilde"";"?|"&Aring"";"?|"&AElig"";"?|"&Egrave"";"?|"&Ecirc"";"?|"&Igrave"";"?|"&Iuml"";"?|"&ETH"";"?|"&Ntilde"";"?|"&Ograve"";"?|"&Oslash"";"?|"&Ugrave"";"?|"&THORN"";"?|"&agrave"";"?|"&atilde"";"?|"&aring"";"?|"&aelig"";"?|"&egrave"";"?|"&ecirc"";"?|"&igrave"";"?|"&iuml"";"?|"&eth"";"?|"&ntilde"";"?|"&ograve"";"?|"&oslash"";"?|"&ugrave"";"?|"&thorn"";"?|"&yuml"";"?)
LATIN1LOWER ("&agrave"";"?|"&atilde"";"?|"&aring"";"?|"&aelig"";"?|"&egrave"";"?|"&ecirc"";"?|"&igrave"";"?|"&iuml"";"?|"&eth"";"?|"&ntilde"";"?|"&ograve"";"?|"&oslash"";"?|"&ugrave"";"?|"&thorn"";"?|"&yuml"";"?)

WORDCHAR ({LATIN1}|[a-zA-Z������������������\-.�%�0-9���������������������������������������������������������������]|"&ndash"";"?|"&mdash"";"?|"&"[0-9]+";"?)

/* WORDCHAR m�nusz a pont */

WORDCHAR2 ({LATIN1}|[a-zA-Z������������������\-�%�0-9���������������������������������������������������������������]|"&ndash"";"?|"&mdash"";"?|"&"[0-9]+";"?)

/* kisbet�k */
LOWER ({LATIN1LOWER}|[a-z�����������������������������������������])

/* mondaton bel�l el�fordul� karakterek */
CHARINSNT ([\(\)\-[\],; "]|("&ndash"";"?)|("&mdash"";"?)|("&ldquor"";"?)|("&raquo"";"?))*
CHARINSNTN {CHARINSNT}"\n"?{CHARINSNT}

/* egyszer� mondathat�rok, kiv�ve a sz�n bel�li pont */
BOUNDARY ([.?!])

/* mondatban szerepl� karakterek, kiv�ve a sz�k�z */
SNTCHAR [^.?!\n]

/* mondat kezd� karaktere, ponttal kezdhet�nk mondatot: */
/* pl.: .hu vita a neten */
SNTBEGIN [^?!\n ]"\n"?

/* egyszer� mondat */
/* XXX Az �r�sjelek itt nem tapad�k, hogy elfogadja a
/* helyes�r�snak nem megfelel� sz�vegeket is: Sz�p az id� ! */
SIMPLESNT ({SNTCHAR}"\n"?)*{BOUNDARY}*

/* mondathat�r ut�n j�het� z�r� id�z�jelek. */
ENDQUOPAR ("\""|"&rdquo""r"?";"|"&laquo;"|"''"|"'"|")"|"]"){BOUNDARY}*

%%

	/* egyszer� mondat */
	
	/* BE: �. A kutya ugat. J�? */

	/* KI: <s>�.</s> <s>A kutya ugat.</s> <s>J�?</s> */

	/* BE: A kutya ugat. J� */
	/* BE: lenne, ha abbahagyn�! */

	/* KI: <s>A kutya ugat.</s> <s>J� */
	/* KI: lenne, ha abbahagyn�!</s> */

	/* BE: Ez itt m�r */
	/* BE:  */
	/* BE: k�l�n bekezd�s! */

	/* KI: <s>Ez itt m�r */
	/* KI: </s> */
	/* KI: <s>k�l�n bekezd�s!</s> */

{SNTBEGIN}{SIMPLESNT} {
	printf("<s>%s</s>",yytext);
}
	/* egyszer� mondat szoros id�z�jelekkel, z�r�jelekkel */
	
	/* BE: "A kutya ugat." &ldquor;J�?&rdquo; ,,Nem.'' */

	/* KI: <s>"A kutya ugat."</s> <s>&ldquor;J�?&rdquo;</s> <s>,,Nem.''</s> */

{SNTBEGIN}{SIMPLESNT}{ENDQUOPAR}+ {
	printf("<s>%s</s>",yytext);
}

	/* mondathat�r t�ll�p�sek: */

	/* Ha a mondatz�r� �r�sjel ut�n nem nagybet�, hanem kisbet� k�vetkezik. */

	/* BE: N. korm�nyz�s�gi sz�khely. */

	/* KI: <s>N. korm�nyz�s�gi sz�khely.</s> */

	/* BE: N. */
	/* BE: korm�nyz�s�gi sz�khely. */

	/* KI: <s>N. */
	/* KI: korm�nyz�s�gi sz�khely.</s> */

	/* BE: A www.ak�rmi.hu. */

	/* KI: <s>A www.ak�rmi.hu.</s> */

	/* BE: A mond. folyt. */
	/* BE: (mivel?) kisbet�s a folytat�s (bizony!)! */

	/* KI: <s>A mond. folyt. */
	/* KI: (mivel?) kisbet�s a folytat�s (bizony!)!</s> */

	/* BE: - N�zd a! - mondta az egyik. */
	
	/* KI: <s>- N�zd a! - mondta az egyik.</s> */

	/* BE: A 4. jav�t�csomagot. */
	
	/* KI: <s>A 4. jav�t�csomagot.</s> */
	
	/* BE: 3434/1992. �vi elsz�mol�s. */
	
	/* KI: <s>3434/1992. �vi elsz�mol�s.</s> */

	/* BE: "J�t s j�l! Ebben �ll a nagy titok" - figyelmezteti */
	/* BE: Kazinczy k�lt�t�rsait. */

	/* KI: <s>"J�t s j�l!</s> <s>Ebben �ll a nagy titok" - figyelmezteti */
	/* KI: Kazinczy k�lt�t�rsait.</s> */
	
	
	/* BE: - Szia P�terk�m! Holnap tal�lkozunk - mondta Gizi. */

	/* KI: <s>- Szia P�terk�m!</s> <s>Holnap tal�lkozunk - mondta Gizi.</s> */

{SNTBEGIN}({SIMPLESNT}{BOUNDARY}{ENDQUOPAR}*{CHARINSNTN}{LOWER})+{SIMPLESNT}{ENDQUOPAR}* {
	printf("<s>%s</s>",yytext);
}

	/* Ha a mondatz�r� �r�sjel ut�n k�t�jel k�vetkezik esetleg id�z�jel */
	/* k�zbe�kel�d�s�vel */

	/* BE: A "Ne m�r!"-ral az a baj. */

	/* KI: <s>A "Ne m�r!"-ral az a baj.</s> */

{SNTBEGIN}({SIMPLESNT}{BOUNDARY}{ENDQUOPAR}"-"{WORDCHAR})+{SIMPLESNT}{ENDQUOPAR}* {
	printf("<s>%s</s>",yytext);
}

	/* Ha a mondatz�r� pont ut�n sz�karakter k�vetkezik k�zvetlen�l, de nem pont! */

	/* BE: A WWW.AKARMI.HU. */

	/* KI: <s>A WWW.AKARMI.HU.</s> */

{SNTBEGIN}({SIMPLESNT}[.]{WORDCHAR2})+{SIMPLESNT}{ENDQUOPAR}* {
	printf("<s>%s</s>",yytext);
}

	/* Ha a mondatz�r� �r�sjel ut�n k�zvetlen�l vessz�, vagy pontosvessz� */
	/* k�vetkezik, kombin�lva a kisbet�s lehet�s�ggel: */

	/* BE: Azt mondta, hogy "Na!", "Csin�ld!" �s �gy tov�bb. */

	/* KI: <s>Azt mondta, hogy "Na!", "Csin�ld!" �s �gy tov�bb.</s> */

{SNTBEGIN}({SIMPLESNT}{BOUNDARY}{ENDQUOPAR}*([,;:]|{CHARINSNTN}{LOWER}))+{SIMPLESNT}{ENDQUOPAR}* {
	printf("<s>%s</s>",yytext);
}

	/* Ha a mondatban z�r�jeles r�sz tal�lhat�. */

	/* BE: A macska (csal�dj�ban a 25.) Katinak ny�vogott. */

	/* KI: <s>A macska (csal�dj�ban a 25.) Katinak ny�vogott.</s> */

{SNTBEGIN}{SIMPLESNT}"("[^.!?)]+[.?!][^.!?)]*")"{SIMPLESNT}{BOUNDARY}{ENDQUOPAR}* {
	printf("<s>%s</s>",yytext);
}

	/* az elozok kombin�ci�ja */

	/* BE: A Cica 4.0 4. r�sze j�?, Macsk�k, �s m�s k�nyvek. */
	
	/* KI: <s>A Cica 4.0 4. r�sze j�?, Macsk�k, �s m�s k�nyvek.</s> */

{SNTBEGIN}(({SIMPLESNT}{BOUNDARY}{ENDQUOPAR}*{CHARINSNTN}{LOWER})|({SIMPLESNT}{BOUNDARY}{ENDQUOPAR}"-"{WORDCHAR})|({SIMPLESNT}[.]{WORDCHAR2})|({SIMPLESNT}{BOUNDARY}{ENDQUOPAR}*([,;:]|{CHARINSNTN}{LOWER}))|({SIMPLESNT}"("[^.!?)]+[.?!][^.!?)]*")"))+{SIMPLESNT}{ENDQUOPAR}* {
	printf("<s>%s</s>",yytext);
}
