CFLAGS = -Wall -g
OBJ = graphe.o inout.o disjoint.o

.SILENT:

libgraphe.a: $(OBJ)
	ar -cr libgraphe.a $(OBJ)

graphe.o: graphe.c
	gcc $(CFLAGS) graphe.c -c


inout.o: inout.c
	gcc $(CFLAGS) inout.c -c

disjoint.o: disjoint.c disjoint.h
	gcc $(CFLAGS) disjoint.c -c

clean:
	rm -f *.o *.a