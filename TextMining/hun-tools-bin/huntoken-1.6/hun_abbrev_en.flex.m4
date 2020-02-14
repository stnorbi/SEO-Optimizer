%option noyywrap

/* hun_abbrev - mondatok �sszevon�sa a val�sz�n�leg hib�san meg�llap�tott mondathat�rokn�l */
/* 2003 (c) N�meth L�szl� <nemethl@gyorsposta.hu> */

%s NUMBEGIN

/* nagybet� �s paragrafusjel */

UPPER [A-Z��������ۧ�������������������������������]

/* nem sz�karakter */
NONWORDCHAR ([^a-zA-Z������������������\-.�%�0-9���������������������������������������������������������������])

/* sz�k�z, vagy �j sor karakter */
SPACE [ \n]

/* mondathat�r */
BOUNDARY ".</s>"{SPACE}"<s>"

WPL ".</s>"{SPACE}"<s>"

/* r�vid�t�sek makr� (k�lso �llom�nyb�l t�ltodik be) */

ABBREV (M4_MACRO_ABBREV)
%%

	/* Sorsz�mok, ha mondatkezd�k */

	/* BE: <s>25.</s> <s>Magyarorsz�g */

	/* KI: <s>25. Magyarorsz�g */

	/* BE: <s>25.</s> <s>� */

	/* KI: <s>25. � */

"<s>"[0-9]+ { ECHO; BEGIN(NUMBEGIN); }

<NUMBEGIN>{BOUNDARY}{UPPER} {
	print_abbrev(yytext);
}

<NUMBEGIN>. {
	ECHO;
	BEGIN(INITIAL);
}

	/* z�r�jelezett d�tum */
	
	/* BE: <s>A 2002.</s> <s>(IV. 25.)</s> <s> */

	/* KI: <s>A 2002. (IV. 25.)  */

[0-9]+{BOUNDARY}"("([VX]?"I"{1,3}|"I"?[VX])"."({SPACE}[0-9]+".")?")</s>"{SPACE}"<s>" {
	print_abbrev(yytext);
}

	/* �gyiratsz�m + d�tum */

	/* BE: <s>A 25/2002.</s> <s>(IV.</s> <s>25.)</s> <s> */

	/* KI: <s>A 25/2002. (IV. 25.)  */

	/* BE: <s>A 25/2002.</s> <s>(IV. 25.)</s> <s> */

	/* KI: <s>A 25/2002. (IV. 25.)  */

{SPACE}[0-9]+"/"[0-9]+{BOUNDARY}"("([VX]?"I"{1,3}|"I"?[VX])".</s>"({SPACE}"<s>"[0-9]+".")?")</s>"{SPACE}"<s>" {
 	print_abbrev(yytext);
}

{SPACE}[0-9]+"/"[0-9]+{BOUNDARY}"("([VX]?"I"{1,3}|"I"?[VX])"."({SPACE}[0-9]+".")?")</s>"{SPACE}"<s>" {
 	print_abbrev(yytext);
}

	/* �gyiratsz�m + d�tum II. */

	/* BE: <s>A 25/2002.</s> <s>(IV.</s> <s>25.) */

	/* KI: <s>A 25/2002. (IV. 25.) */

{SPACE}[0-9]+"/"[0-9]+{BOUNDARY}"("([VX]?"I"{1,3}|"I"?[VX])".</s>"{SPACE}"<s>" {
 	print_abbrev(yytext);
}

	/* �gyiratsz�m + d�tum III. */

	/* BE: <s>A 25/2002.</s> <s>(IV.25.) */

	/* KI: <s>A 25/2002. (IV.25.) */

{SPACE}[0-9]+"/"[0-9]+{BOUNDARY}"("([VX]?"I"{1,3}|"I"?[VX])"."([0-9]+".")?")" {
 	print_abbrev(yytext);
}

	/* paragrafusjel, �s sorsz�mot k�veto sz�m, vagy d�tum r�mai sz�mmal */

	/* BE: <s>A 25.</s> <s>� szerint 2002.</s> <s>IV. hav�ban. */

	/* KI: <s>A 25. � szerint 2002. IV. hav�ban. */

[0-9]+{BOUNDARY}([�0-9]|[VX]?"I"{1,3}"."|"I"?[VX]".") {
	print_abbrev(yytext);
}

[0-9]+{BOUNDARY}([VX]?"I"{1,3}|"I"?[VX]){BOUNDARY}[0-9] {
	print_abbrev(yytext);
}


	/* Monogramok (B. Jen�) */
	
	/* BE: B.</s> <s>Jen�. */

	/* KI: B. Jen�. */

	/* BE: A.</s> <s>E.</s> <s>X.</s> <s>Wilson. */

	/* KI: A. E. X. Wilson. */

{NONWORDCHAR}({ABBREV}{BOUNDARY}|{UPPER}{BOUNDARY})+ {
	print_abbrev(yytext);
}

	/* R�mai sz�mok (VI. Lajos), kiv�ve CD. */

	/* BE: XIV.</s> <s>Lajos. */

	/* KI: XIV. Lajos. */

	/* BE: Ott a CD.</s> <s>Hallod? */

	/* KI: Ott a CD.</s> <s>Hallod? */

{NONWORDCHAR}"CD"{BOUNDARY} { ECHO; }  /* robusztus */

{NONWORDCHAR}[IVXLCMD]+{BOUNDARY} { print_abbrev(yytext); }  /* robusztus */


	/* Pl. eset�ben mindig megsz�ntetj�k a mondathat�rt. */

	/* BE: Pl.</s> <s>P�ter �s Marcsa pl.</s> <s>25 f�nkot is ehetne. */
	
	/* KI: Pl. P�ter �s Marcsa pl. 25 f�nkot is ehetne. */

{NONWORDCHAR}?[Pp]"l"{BOUNDARY} { print_abbrev(yytext); }  /* l., L. */

	/* Gyakori r�vid�t�sek */

	/* BE: In apr.</s> <s>I was at Sci.</s> <s>Corp.</s> <s>Mexico. */
	
	/* KI: In apr. I was at Sci. Corp. Mexico. */

	/* {NONWORDCHAR}{ABBREV}{BOUNDARY} { print_abbrev(yytext); } */

	/* ,,stb.'' eset�ben nem vonunk egybe. (A macska, kutya stb. Az els�... */

	/* tokeniz�l�s ut�n mondatv�gir�vid�t�s-jav�t�s */

"<w>CD\n</w>\n<c>.</c>" {
        ECHO;
}

"<w>"({ABBREV}|[A-Z]|[IVXLCMD]+)"\n</w>\n<c>.</c>" {
	strcpy(yytext + (yyleng - 14), ".\n</w>");
	printf("%s", yytext);
}

	/* hun_sentclean kieg�sz�t�se */

"\n\n</s>" {
	printf("\n</s>");
}

%%
/* 
 * <s> �s </s> c�mk�k t�rl�se, �s ki�r�s
 */
int print_abbrev(const char * s)
{
	char buff[8192];
	int i, j = 0;
	for (i = 0; i < strlen(s); i++) {
		if (strncmp(s+i, "<s>", 3) == 0) i+=2;
		else if (strncmp(s+i, "</s>", 4) == 0) i+=3;
		else { 
			buff[j] = s[i];
			j++;
		}
	}
	buff[j] = '\0';
	printf("%s",buff);
}
