%option noyywrap

/* hun_clean - karaktereket t�rl�, illetve �talak�t� sz�r� */
/* 2003 (c) N�meth L�szl� <nemethl@gyorsposta.hu> */

/* Makr�defin�ci�k */

/* Sz�k�z �rt�k� szekvenci�k: sz�k�z, tabul�tor, nem t�r� sz�k�z. */

/* Az &nbsp; entit�st, �s a ,,kocsi vissza'' karaktert is felvessz�k ide */

SPACE ([ 	\240]|"&nbsp"";"?|"\r")

/* �j sor �rt�k� szekvenci�k */

/* A kocsi vissza karaktert az MS-DOS sz�vegek redund�ns k�dol�sa miatt */
/* nem �j sor, hanem sz�k�z �rt�k� karakternek k�doltuk. */

/* \n: �j sor */
/* \f: lapdob�s */
/* \v: f�gg�leges tabul�tor */

NEWLINE [\n\f\v]

%%

	/* bekezd�shat�rok */
	/* bemenet: legal�bb k�t sort�r�s + sz�k�z�k */
	/* kimenet: k�t sort�r�s */

	/* A k�vetkez�kkel nem foglalkozunk: */
	/* XXX Az &nbspvalami szekvenci�kb�l is t�r�lj�k az &nbsp-t */

	/* BE: Bekezd�shat�rok. A sorokban tabul�torok �s sz�k�z�k:	 */
	/* BE: 		 */
	/* BE:           */
	/* BE: 	   V�ge. */

	/* KI: Bekezd�shat�rok. A sorokban tabul�torok �s sz�k�z�k: */
	/* KI:  */
	/* KI: V�ge. */

{SPACE}*{NEWLINE}({SPACE}*{NEWLINE})+{SPACE}* {
		printf("\n\n");
	}

	/* sort�r�s */
	/* bemenet: egy sort�r�s sorv�gi �s k�vetkez� sor eleji sz�k�z�kkel */
	/* kimenet: egy sort�r�s */

	/* BE: Sort�r�s. Sz�k�z �s tabul�tor: 	 */
	/* BE: 		 Itt is a sor elej�n. */

	/* KI: Sort�r�s. Sz�k�z �s tabul�tor: */
	/* KI: Itt is a sor elej�n. */

{SPACE}*{NEWLINE}{SPACE}* {
		printf("\n");
	}

	/* els� sor elej�n l�v� sz�k�z�k t�rl�se */
^{SPACE}*

	/* sz�k�zsorozat �s nem t�r� sz�k�z�k lecser�l�se  egy sz�k�zre */
	/* bemenet: t�bb sz�k�z, vagyis SPACE szekvencia egym�s ut�n */
	/* kimenet: egy sz�k�z */

	/* BE: Sz�k�zsorozat. T�bb	     	sz�k�z �s   	  tabul�tor. */

	/* KI: Sz�k�zsorozat. T�bb sz�k�z �s tabul�tor. */

	/* BE: Nem t�r� sz�k�z:�V�ge. */

	/* KI: Nem t�r� sz�k�z: V�ge. */

{SPACE}* {
		printf(" ");
	}

	/* < �s > �tk�dol�sa */
	/* bemenet: <, vagy > */
	/* kimenet: &lt; vagy &gt; */

	/* BE: <> */

	/* KI: &lt;&gt; */
	
"<" {
	printf("&lt;");
}

">" {
	printf("&gt;");
}

	/* Windows karakterk�dok egy r�sz�nek �talak�t�sa */

"&#128"";"?|[\200] { printf("&euro;"); }
"&#130"";"?|[\202] { printf("&lsquor;"); } /* HTML 4.0-ban sbquo; */
"&#132"";"?|[\204] { printf("&ldquor;"); }  /* HTML 4.0-ban bdquo; */
"&#133"";"?|[\205] { printf("..."); }

"&#139"";"?|[\213] { printf("\""); }

"&#145"";"?|[\221] { printf("&lsquo;"); } /* 6 */
"&#146"";"?|[\222] { printf("&rsquo;"); } /* 9 */
"&#147"";"?|[\223] { printf("&ldquo;"); } /* 66 */
"&#148"";"?|[\224] { printf("&rdquo;"); } /* 99 */

"&#150"";"?|[\226] { printf("&ndash;"); } /* -- */
"&#151"";"?|[\227] { printf("&mdash;"); } /* --- */

"&#153"";"?|[\231] { printf("&trade;"); } /* TM */

	/* decim�lis karakterk�d */
	/* feltessz�k, hogy az input latin-2, �s a 256-n�l kisebb k�dok
	/* is erre vonatkoznak. */

	/* bemenet: "&" max. 5 jegy� sz�m �s esetleg pontosvessz� */
	/* kimenet: latin-2 karakter, vagy a v�ltozatlan k�d, illetve */
	/* ha a sz�m a < �s > karakterek k�dja -> &lt; �s &gt; entit�s */
	/* �tk�dol�sra ker�lnek az UNICODE nagyk�t�jelek, �s id�z�jelek is */

	/* BE: (EEC&#041; (EEC&#041;	&#107	&#60;	&#337;	&#3456;	&#2343235325; */

	/* KI: (EEC) (EEC) k &lt; � &#3456; &#2343235325; */

"&#"[0-9]{1,5}";"? {
	// decim�lis karakterk�dok kezel�se
	// nem latin-1 eset�ben csak a magyar ����
	int i;
	i = atoi(yytext + 2);
	if (i == 38) printf("&amp;"); // & jel
	else if (i == 60) printf("&lt;"); // < jel
	else if (i == 62) printf("&gt;"); // > jel
	else if (i < 256) printf("%c", i); // latin-1
	else if (i == 337) printf("�");
	else if (i == 336) printf("�");
	else if (i == 369) printf("�");
	else if (i == 368) printf("�");
	// ismeretlen k�dot nem v�ltoztatjuk
	else ECHO;
}

		/* Ha hosszabb, mint 5 karakter a sz�m, nem v�ltoztatunk */
"&#"[0-9]{6,}";"? {
	ECHO;
}

	/* hexadecim�lis karakterk�d */
	/* XXX most nem foglalkozunk ezzel (ritka) */

	/* BE: &#xF456 &#Xabc; &#xABCDEF; */

	/* KI: &#xF456 &#Xabc; &#xABCDEF; */

"&#"[xX][0-9a-fA-F]+";"? {
	ECHO;
}

	/* XXX speci�lis �s szimb�lum HTML 4.0 entit�sokkal nem foglalkoztunk m�g */

	/* kiv�ve a 3 pont, �s a &quot; �talak�t�s�t */

	/* BE: &hellip; */

	/* KI: ... */

"&hellip"";"? { printf("..."); }

"&quot"";"? { printf("\""); }

	/* magyar id�z�jelek: HTML 4.0 -> SGML  */

	/* BE: &bdquo; */

	/* KI: &ldquor; */

"&bdquo"";"? { printf("&ldquor;"); }

"&sbquo"";"? { printf("&lsquor;"); }

	/* latin-1 HTML entit�sok r�szleges �talak�t�sa (most m�g latin-2-re) */
	/* �talak�t�s ott t�rt�nik, ahol a latin-2 megegyezik a latin-1-gyel */

	/* BE: &aacute; &Aacute; &otilde; &Otilde; &ucirc; &Ucirc; &ndash; &mdash; */

	/* KI: � � � � � � &ndash; &mdash; */

	/* "&nbsp"";"? { printf("%c",(char) 160); } */ // ez m�r lecser�lve */

	/* "&iexcl"";"? { printf("%c",(char) 161); } */ // ford�tott felki�lt�jel

	/* "&cent"";"? { printf("%c",(char) 162); } */
	/* "&pound"";"? { printf("%c",(char) 163); } */

"&curren"";"? { printf("%c",(char) 164); }

	/* "&yen"";"? { printf("%c",(char) 165); } */
	/* "&brvbar"";"? { printf("%c",(char) 166); } */
	
"&sect"";"? { printf("%c",(char) 167); }

	/* "&uml"";"? { printf("%c",(char) 168); } */
	/* "&copy"";"? { printf("%c",(char) 169); } */
	/* "&ordf"";"? { printf("%c",(char) 170); } */
	/* "&laquo"";"? { printf("%c",(char) 171); } */
	/* "&not"";"? { printf("%c",(char) 172); } */

	/* BE: &shy&shy; */

	/* KI:  */

"&shy"";"? // elv�laszt�si hely jel�nek (felt�teles v. l�gy k�t�jel) t�rl�se

	/* "&reg"";"? { printf("%c",(char) 174); } */
	/* "&macr"";"? { printf("%c",(char) 175); } */

	/* BE: &deg; */

	/* KI: � */

"&deg"";"? { printf("%c",(char) 176); } // fokjel, megegyezik latin-2-vel

	/* "&plusmn"";"? { printf("%c",(char) 177); } */
	/* "&sup2"";"? { printf("%c",(char) 178); } */
	/* "&sup3"";"? { printf("%c",(char) 179); } */

	/* BE: &acute; */

	/* KI: � */

"&acute"";"? { printf("%c",(char) 180); } // vessz� �kezet, megegyezik a latin-2-vel

	/* "&micro"";"? { printf("%c",(char) 181); } */
	/* "&para"";"? { printf("%c",(char) 182); } */
	/* "&middot"";"? { printf("%c",(char) 183); } */

	/* BE: &cedil; */

	/* KI: � */

"&cedil"";"? { printf("%c",(char) 184); } // cedilla �kezet, megegyezik a latin-2-vel

	/* "&sup1"";"? { printf("%c",(char) 185); } */
	/* "&ordm"";"? { printf("%c",(char) 186); } */
	/* "&raquo"";"? { printf("%c",(char) 187); } */
	/* "&frac14"";"? { printf("%c",(char) 188); } */
	/* "&frac12"";"? { printf("%c",(char) 189); } */
	/* "&frac34"";"? { printf("%c",(char) 190); } */
	/* "&iquest"";"? { printf("%c",(char) 191); } */
	/* "&Agrave"";"? { printf("%c",(char) 192); } */ // bet�

	/* BE: &Aacute; */

	/* KI: � */

"&Aacute"";"? { printf("%c",(char) 193); }

	/* BE: &Acirc; */

	/* KI: � */

"&Acirc"";"? { printf("%c",(char) 194); }

	/* "&Atilde"";"? { printf("%c",(char) 195); } // bet�

	/* BE: &Auml; */

	/* KI: � */

"&Auml"";"? { printf("%c",(char) 196); }

	/* "&Aring"";"? { printf("%c",(char) 197); } */ // bet�
	/* "&AElig"";"? { printf("%c",(char) 198); } */ // bet�

	/* BE: &Ccedil; */

	/* KI: � */

"&Ccedil"";"? { printf("%c",(char) 199); }

	/* "&Egrave"";"? { printf("%c",(char) 200); } */ // bet�

	/* BE: &Eacute; */

	/* KI: � */

"&Eacute"";"? { printf("%c",(char) 201); }

	/* "&Ecirc"";"? { printf("%c",(char) 202); } */ // bet�

	/* BE: &Euml; */

	/* KI: � */

"&Euml"";"? { printf("%c",(char) 203); }

	/* "&Igrave"";"? { printf("%c",(char) 204); } */ // bet�

	/* BE: &Iacute; */

	/* KI: � */

"&Iacute"";"? { printf("%c",(char) 205); }

	/* BE: &Icirc; */

	/* KI: � */

"&Icirc"";"? { printf("%c",(char) 206); }

	/* "&Iuml"";"? { printf("%c",(char) 207); } */ // bet�
	/* "&ETH"";"? { printf("%c",(char) 208); } */ // bet�
	/* "&Ntilde"";"? { printf("%c",(char) 209); } */ // bet�
	/* "&Ograve"";"? { printf("%c",(char) 210); } */ // bet�

	/* BE: &Oacute; */

	/* KI: � */

"&Oacute"";"? { printf("%c",(char) 211); }

	/* BE: &Ocirc; */

	/* KI: � */

"&Ocirc"";"? { printf("%c",(char) 212); }

	/* XXX Tipikus t�veszt�s: hull�mvonalas O jav�t�sa �-re */

	/* BE: &Otilde; */

	/* KI: � */

"&Otilde"";"? { printf("%c",(char) 213); }

	/* BE: &Ouml; */

	/* KI: � */

"&Ouml"";"? { printf("%c",(char) 214); }

	/* BE: &times; */

	/* KI: � */

"&times"";"? { printf("%c",(char) 215); }

	/* "&Oslash"";"? { printf("%c",(char) 216); } */ // bet�
	/* "&Ugrave"";"? { printf("%c",(char) 217); } */ // bet�

	/* BE: &Uacute; */

	/* KI: � */

"&Uacute"";"? { printf("%c",(char) 218); }

	/* XXX Tipikus t�veszt�s: pontos U jav�t�sa �-re */

	/* BE: &Ucirc; */

	/* KI: � */

"&Ucirc"";"? { printf("%c",(char) 219); }

	/* BE: &Uuml; */

	/* KI: � */

"&Uuml"";"? { printf("%c",(char) 220); }

	/* BE: &Yacute; */

	/* KI: � */

"&Yacute"";"? { printf("%c",(char) 221); }

	/* "&THORN"";"? { printf("%c",(char) 222); } */ // bet�

	/* BE: &szlig; */

	/* KI: � */

"&szlig"";"? { printf("%c",(char) 223); }

	/* "&agrave"";"? { printf("%c",(char) 224); } */ // bet�

	/* BE: &aacute; */

	/* KI: � */

"&aacute"";"? { printf("%c",(char) 225); }

	/* BE: &acirc; */

	/* KI: � */

"&acirc"";"? { printf("%c",(char) 226); }

	/* "&atilde"";"? { printf("%c",(char) 227); } */ // bet�

	/* BE: &auml; */

	/* KI: � */

"&auml"";"? { printf("%c",(char) 228); }

	/* "&aring"";"? { printf("%c",(char) 229); } */ // bet�
	/* "&aelig"";"? { printf("%c",(char) 230); } */ // bet�

	/* BE: &ccedil; */

	/* KI: � */

"&ccedil"";"? { printf("%c",(char) 231); }

	/* "&egrave"";"? { printf("%c",(char) 232); } */ // bet�

	/* BE: &eacute; */

	/* KI: � */

"&eacute"";"? { printf("%c",(char) 233); }

	/* "&ecirc"";"? { printf("%c",(char) 234); } */ // bet�

	/* BE: &euml; */

	/* KI: � */

"&euml"";"? { printf("%c",(char) 235); }

	/* "&igrave"";"? { printf("%c",(char) 236); } */ // bet�

	/* BE: &iacute; */

	/* KI: � */

"&iacute"";"? { printf("%c",(char) 237); }

	/* BE: &icirc; */

	/* KI: � */

"&icirc"";"? { printf("%c",(char) 238); }

	/* "&iuml"";"? { printf("%c",(char) 239); } */ // bet�
	/* "&eth"";"? { printf("%c",(char) 240); } */ // bet�
	/* "&ntilde"";"? { printf("%c",(char) 241); } */ // bet�
	/* "&ograve"";"? { printf("%c",(char) 242); } */ // bet�

	/* BE: &oacute; */

	/* KI: � */

"&oacute"";"? { printf("%c",(char) 243); }

	/* BE: &ocirc; */

	/* KI: � */

"&ocirc"";"? { printf("%c",(char) 244); }

	/* XXX Tipikus t�veszt�s: hull�mvonalas o jav�t�sa �-re */

	/* BE: &otilde; */

	/* KI: � */

"&otilde"";"? { printf("%c",(char) 245); }

	/* BE: &ouml; */

	/* KI: � */

"&ouml"";"? { printf("%c",(char) 246); }

	/* BE: &divide; */

	/* KI: � */

"&divide"";"? { printf("%c",(char) 247); }

	/* "&oslash"";"? { printf("%c",(char) 248); } */ // bet�
	/* "&ugrave"";"? { printf("%c",(char) 249); } */ // bet�

	/* BE: &uacute; */

	/* KI: � */

"&uacute"";"? { printf("%c",(char) 250); }

	/* BE: &ucirc; */

	/* KI: � */

	/* XXX Tipikus t�veszt�s: pontos u jav�t�sa �-re */

"&ucirc"";"? { printf("%c",(char) 251); }

	/* BE: &uuml; */

	/* KI: � */

"&uuml"";"? { printf("%c",(char) 252); }

	/* BE: &yacute; */

	/* KI: � */

"&yacute"";"? { printf("%c",(char) 253); }

	/* "&thorn"";"? { printf("%c",(char) 254); } */ // bet�
	/* "&yuml"";"? { printf("%c",(char) 255); } */ // bet�
