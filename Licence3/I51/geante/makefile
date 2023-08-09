CFLAGS1 = -Wall -g -I ../lib -L ../lib
CFLAGS2 = -Wall -g -I ../lib
OBJ = geante.o

.SILENT:

prog: $(OBJ)
	gcc $(CFLAGS1) $(OBJ) -o prog -lgraphe -lm

geante.o: geante.c
	gcc $(CFLAGS2) geante.c -c

clean:
	rm -f *.o *.a *.png