CC = gcc -Wall -g
YACC = bison -v
OBJS = parser.o lexer.o ts.o asa.o

arc: $(OBJS)
	$(CC) -o arc $(OBJS) -ll

lexer.o: lexer.c
	$(CC) -c lexer.c 
	
lexer.c: lexer.lex parser.h
	flex -o lexer.c lexer.lex

parser.o: parser.c 
	$(CC) -c parser.c 

parser.h: parser.y

parser.c: parser.y 
	$(YACC) -o parser.c -d parser.y

ts.o: ts.c ts.h
	$(CC) ts.c -c 

asa.o: asa.c asa.h
	$(CC) asa.c -c 
	
clean:
	rm -f *~ *.o arc
