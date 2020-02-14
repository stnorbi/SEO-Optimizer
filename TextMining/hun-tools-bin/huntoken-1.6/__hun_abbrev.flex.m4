/* AZ M4 FORR�SB�L ELO�LL�TOTT �LLOM�NY, EZT NE M�DOS�TSD! */
define(M4_MACRO_ABBREV,
"a"|"A"|"a."{SPACE}"m"|"A."{SPACE}"m"|"aug"|"Aug"|"bek"|"Bek"|"Bp"|"br"|"Br"|"B."{SPACE}"�."{SPACE}"�."{SPACE}"k"|"bt"|"Bt"|"Btk"|"c"|"C"|"cca"|"Cca"|"Cs"|"cs�t"|"Cs�t"|"Ctv"|"dec"|"Dec"|"dk"|"Dk"|"dny"|"Dny"|"dr"|"Dr"|"du"|"Du"|"Dzs"|"em"|"Em"|"ev"|"Ev"|"f"|"F"|"febr"|"Febr"|"felv"|"Felv"|"ford"|"Ford"|"f."{SPACE}"�"|"F."{SPACE}"�"|"fszla"|"Fszla"|"fszt"|"Fszt"|"gimn"|"Gimn"|"gr"|"Gr"|"Gy"|"h"|"H"|"hg"|"Hg"|"hiv"|"Hiv"|"honv"|"Honv"|"hrsz"|"Hrsz"|"hsz"|"Hsz"|"htb"|"Htb"|"id"|"Id"|"ifj"|"Ifj"|"ig"|"Ig"|"igh"|"Igh"|"ill"|"Ill"|"ind"|"Ind"|"isk"|"Isk"|"i."{SPACE}"e"|"I."{SPACE}"e"|"i."{SPACE}"m"|"I."{SPACE}"m"|"i."{SPACE}"sz"|"I."{SPACE}"sz"|"izr"|"Izr"|"jan"|"Jan"|"jegyz"|"Jegyz"|"j�l"|"J�l"|"j�n"|"J�n"|"kb"|"Kb"|"ker"|"Ker"|"kft"|"Kft"|"kht"|"Kht"|"kk"|"Kk"|"kkt"|"Kkt"|"kp"|"Kp"|"Kr"|"Kr."{SPACE}"e"|"Kr."{SPACE}"u"|"krt"|"Krt"|"K."{SPACE}"m."{SPACE}"f"|"k�v"|"K�v"|"luth"|"Luth"|"m"|"M"|"mb"|"Mb"|"megh"|"Megh"|"Mr"|"m�rc"|"M�rc"|"m."{SPACE}"�"|"M."{SPACE}"�"|"NB"|"nov"|"Nov"|"ny"|"Ny"|"nyug"|"Nyug"|"o"|"O"|"okl"|"Okl"|"okt"|"Okt"|"olv"|"Olv"|"ov"|"Ov"|"ovh"|"Ovh"|"p"|"P"|"pf"|"Pf"|"pl"|"Pl"|"Pp"|"Ptk"|"pu"|"Pu"|"ref"|"Ref"|"rkp"|"Rkp"|"r."{SPACE}"k"|"R."{SPACE}"k"|"rt"|"Rt"|"r�v"|"R�v"|"sgt"|"Sgt"|"s."{SPACE}"k"|"S."{SPACE}"k"|"St"|"sz"|"Sz"|"szept"|"Szept"|"szerk"|"Szerk"|"Szjt"|"Szt"|"t"|"T"|"tc"|"Tc"|"tkp"|"Tkp"|"t�rv"|"T�rv"|"tvr"|"Tvr"|"Ty"|"u"|"U"|"ua"|"Ua"|"ui"|"Ui"|"uo"|"Uo"|"v"|"v�"|"V"|"V�"|"vsz"|"Vsz"|"Zs"|"nyug.")
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

	/* BE: Pl.</s> <s>Jani szerint �pr.</s> <s>Kati kedvenc h�napja. */
	
	/* KI: Pl. Jani szerint �pr. Kati kedvenc h�napja. */

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
