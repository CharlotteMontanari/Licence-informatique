CFLAGS = -Wall -g 
OBJ = disjoint.o main.o

.SILENT:

prog: $(OBJ)
	gcc $(OBJ) $(CFLAGS) -o prog

disjoint.o: disjoint.c disjoint.h
	gcc $(CFLAGS) disjoint.c -c

main.o: main.c disjoint.h
	gcc $(CFLAGS) main.c -c

clean:
	rm -f *.o prog