CC = gcc
CFLAGS = -Wall -g
LIBS = -lm
OBJS = lib/afd.o lib/afn.o lib/compregex.o
OBJS2 = lib/mygrep.o lib/afn.o lib/compregex.o lib/postfix_to_af.o

all: essai/af essai/mygrep

essai/af: lib/af.c $(OBJS)
	$(CC) $(CFLAGS) $^ $(LIBS) -o $@

essai/mygrep: $(OBJS2)
	$(CC) $(CFLAGS) $^ $(LIBS) -o $@ 

lib/afd.o: lib/afd.c
	$(CC) -c -g $^ -o $@

lib/afn.o: lib/afn.c
	$(CC) -c -g $^ -o $@

lib/compregex.o: lib/compregex.c
	$(CC) -c -g $^ -o $@

lib/mygrep.o: lib/mygrep.c
	$(CC) -c -g $^ -o $@

clean:
	rm -rf essai/* lib/*.o 
