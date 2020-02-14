%option noyywrap

/* hun_latin1 - ISO-8859-1 (illetve Windows-1252) bet�it entit�sokra alak�t� sz�r� */
/* 2003 (c) N�meth L�szl� <nemethl@gyorsposta.hu> */

%%

	/* [\240] { printf("%s", "&nbsp;" ); }  // ez m�r lecser�lve */

[\241] { printf("%s", "&iexcl;" ); }

[\242] { printf("%s", "&cent;" ); }
[\243] { printf("%s", "&pound;" ); }

	/** "&curren"";"? { printf("%c",(char) 164); } */
    
[\245] { printf("%s", "&yen;" ); }
[\246] { printf("%s", "&brvbar;" ); }
[\247] { printf("%s", "&sect;" ); }
[\250] { printf("%s", "&uml;" ); }
[\251] { printf("%s", "&copy;" ); }
[\252] { printf("%s", "&ordf;" ); }
[\253] { printf("%s", "&laquo;" ); }
[\254] { printf("%s", "&not;" ); }

	/* *BE: &shy&shy; */

	/* *KI:  */

	/** "&shy"";"? // elv�laszt�si hely jel�nek (felt�teles v. l�gy k�t�jel) t�rl�se */

[\256] { printf("%s", "&reg;" ); }
[\257] { printf("%s", "&macr;" ); }

	/* *BE: &deg; */

	/* *KI: � */

	/** "&deg"";"? { printf("%c",(char) 176); } // fokjel, megegyezik latin-2-vel */

[\261] { printf("%s", "&plusmn;" ); }
[\262] { printf("%s", "&sup2;" ); }
[\263] { printf("%s", "&sup3;" ); }

	/* *BE: &acute; */

	/* *KI: � */

	/** "&acute"";"? { printf("%c",(char) 180); } // vessz� �kezet, megegyezik a latin-2-vel */

[\265] { printf("%s", "&micro;" ); }
[\266] { printf("%s", "&para;" ); }
[\267] { printf("%s", "&middot;" ); }

	/* *BE: &cedil; */

	/* *KI: � */

	/** "&cedil"";"? { printf("%c",(char) 184); } // cedilla �kezet, megegyezik a latin-2-vel */

[\271] { printf("%s", "&sup1;" ); }
[\272] { printf("%s", "&ordm;" ); }
[\273] { printf("%s", "&raquo;" ); }
[\274] { printf("%s", "&frac14;" ); }
[\275] { printf("%s", "&frac12;" ); }
[\276] { printf("%s", "&frac34;" ); }
[\277] { printf("%s", "&iquest;" ); }
[\300] { printf("%s", "&Agrave;" ); }

	/* *BE: &Aacute; */

	/* *KI: � */

	/** "&Aacute"";"? { printf("%c",(char) 193); } */

	/* *BE: &Acirc; */

	/* *KI: � */

	/** "&Acirc"";"? { printf("%c",(char) 194); } */

	/* "&Atilde"";"? { printf("%c",(char) 195); } // bet�

	/* *BE: &Auml; */

	/* *KI: � */

	/** "&Auml"";"? { printf("%c",(char) 196); } */

[\305] { printf("%s", "&Aring;" ); }
[\306] { printf("%s", "&AElig;" ); }

	/* *BE: &Ccedil; */

	/* *KI: � */

	/** "&Ccedil"";"? { printf("%c",(char) 199); } */

[\310] { printf("%s", "&Egrave;" ); }

	/* *BE: &Eacute; */

	/* *KI: � */

	/** "&Eacute"";"? { printf("%c",(char) 201); } */

[\312] { printf("%s", "&Ecirc;" ); }

	/* *BE: &Euml; */

	/* *KI: � */

	/** "&Euml"";"? { printf("%c",(char) 203); } */

[\314] { printf("%s", "&Igrave;" ); }

	/* *BE: &Iacute; */

	/* *KI: � */

	/** "&Iacute"";"? { printf("%c",(char) 205); } */

	/* *BE: &Icirc; */

	/* *KI: � */

	/** "&Icirc"";"? { printf("%c",(char) 206); } */

[\317] { printf("%s", "&Iuml;" ); }
[\320] { printf("%s", "&ETH;" ); }
[\321] { printf("%s", "&Ntilde;" ); }
[\322] { printf("%s", "&Ograve;" ); }

	/* *BE: &Oacute; */

	/* *KI: � */

	/** "&Oacute"";"? { printf("%c",(char) 211); } */

	/* *BE: &Ocirc; */

	/* *KI: � */

	/** "&Ocirc"";"? { printf("%c",(char) 212); } */

	/* XXX Tipikus t�veszt�s: hull�mvonalas O jav�t�sa �-re */

	/* *BE: &Otilde; */

	/* *KI: � */

	/** "&Otilde"";"? { printf("%c",(char) 213); } */

	/* *BE: &Ouml; */

	/* *KI: � */

	/** "&Ouml"";"? { printf("%c",(char) 214); } */

	/* *BE: &times; */

	/* *KI: � */

	/** "&times"";"? { printf("%c",(char) 215); } */

[\330] { printf("%s", "&Oslash;" ); }
[\331] { printf("%s", "&Ugrave;" ); }

	/* *BE: &Uacute; */

	/* *KI: � */

	/** "&Uacute"";"? { printf("%c",(char) 218); } */

	/* XXX Tipikus t�veszt�s: pontos U jav�t�sa �-re */

	/* *BE: &Ucirc; */

	/* *KI: � */

	/** "&Ucirc"";"? { printf("%c",(char) 219); } */

	/* *BE: &Uuml; */

	/* *KI: � */

	/** "&Uuml"";"? { printf("%c",(char) 220); } */

	/* *BE: &Yacute; */

	/* *KI: � */

	/** "&Yacute"";"? { printf("%c",(char) 221); } */

[\336] { printf("%s", "&THORN;" ); }

	/* *BE: &szlig; */

	/* *KI: � */

	/** "&szlig"";"? { printf("%c",(char) 223); } */

[\340] { printf("%s", "&agrave;" ); }

	/* *BE: &aacute; */

	/* *KI: � */

	/** "&aacute"";"? { printf("%c",(char) 225); } */

	/* *BE: &acirc; */

	/* *KI: � */

	/** "&acirc"";"? { printf("%c",(char) 226); } */

[\343] { printf("%s", "&atilde;" ); }

	/* *BE: &auml; */

	/* *KI: � */

	/** "&auml"";"? { printf("%c",(char) 228); } */

[\345] { printf("%s", "&aring;" ); }
[\346] { printf("%s", "&aelig;" ); }

	/* *BE: &ccedil; */

	/* *KI: � */

	/** "&ccedil"";"? { printf("%c",(char) 231); } */

[\350] { printf("%s", "&egrave;" ); }

	/* *BE: &eacute; */

	/* *KI: � */

	/** "&eacute"";"? { printf("%c",(char) 233); } */

[\352] { printf("%s", "&ecirc;" ); }

	/* *BE: &euml; */

	/* *KI: � */

	/** "&euml"";"? { printf("%c",(char) 235); } */

[\354] { printf("%s", "&igrave;" ); }

	/* *BE: &iacute; */

	/* *KI: � */

	/** "&iacute"";"? { printf("%c",(char) 237); } */

	/* *BE: &icirc; */

	/* *KI: � */

	/** "&icirc"";"? { printf("%c",(char) 238); } */

[\357] { printf("%s", "&iuml;" ); }
[\360] { printf("%s", "&eth;" ); }
[\361] { printf("%s", "&ntilde;" ); }
[\362] { printf("%s", "&ograve;" ); }

	/* *BE: &oacute; */

	/* *KI: � */

	/** "&oacute"";"? { printf("%c",(char) 243); } */

	/* *BE: &ocirc; */

	/* *KI: � */

	/** "&ocirc"";"? { printf("%c",(char) 244); } */

	/* XXX Tipikus t�veszt�s: hull�mvonalas o jav�t�sa �-re */

	/* *BE: &otilde; */

	/* *KI: � */

	/** "&otilde"";"? { printf("%c",(char) 245); } */

	/* *BE: &ouml; */

	/* *KI: � */

	/** "&ouml"";"? { printf("%c",(char) 246); } */

	/* *BE: &divide; */

	/* *KI: � */

	/** "&divide"";"? { printf("%c",(char) 247); } */

[\370] { printf("%s", "&oslash;" ); }
[\371] { printf("%s", "&ugrave;" ); }

	/* *BE: &uacute; */

	/* *KI: � */

	/** "&uacute"";"? { printf("%c",(char) 250); } */

	/* *BE: &ucirc; */

	/* *KI: � */

	/* XXX Tipikus t�veszt�s: pontos u jav�t�sa �-re */

	/** "&ucirc"";"? { printf("%c",(char) 251); } */

	/* *BE: &uuml; */

	/* *KI: � */

	/** "&uuml"";"? { printf("%c",(char) 252); } */

	/* *BE: &yacute; */

	/* *KI: � */

	/** "&yacute"";"? { printf("%c",(char) 253); } */

[\376] { printf("%s", "&thorn;" ); }
[\377] { printf("%s", "&yuml;" ); }

