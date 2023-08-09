CFLAGS = -Wall -g
OBJ = analex.o

analex: lex.yy.c $(OBJ)
	gcc $(CFLAGS) $(OBJ) lex.yy.c -ll -o analex

lex.yy.c: pluslong.lex
	flex pluslong.lex

analex.o: analex.c analex.h
	gcc $(CFLAGS) analex.c -c

clean:
	rm -rf lex.yy.c analex