%option noyywrap

/* hun_sentbreak - hossz� mondatok t�rdel�se */
/* 2003 (c) N�meth L�szl� <nemethl@gyorsposta.hu> */

/* Makr�defin�ci�k */

/* sz�k�z, vagy �j sor karakter */
SPACE [ \n]

        #define SLEN 10000
%%

        /* nagyon hossz� mondatok t�r�se */
        
"<s>"[^\n]* {
	if (yyleng > SLEN) {
            char * s = yytext;
            char r;
            int i;
            for (i = 0; i < yyleng / SLEN; i++) {
                r = s[SLEN];
                s[SLEN] = '\0';
                fprintf(stderr,"%s\n</s>\n<s>",s);
                s[SLEN] = r;
                s += SLEN;
            }
            fprintf(stderr,"%s",s);
        } else {
            printf("%s", yytext);
        }
}
