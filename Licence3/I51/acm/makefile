CFLAGS = -Wall -g -L../lib
OBJ = acm.o main.o

.SILENT:

prog: $(OBJ)
	gcc $(OBJ) $(CFLAGS) -o prog -lgraphe -lm

acm.o: acm.c acm.h 
	gcc $(CFLAGS) acm.c -c

main.o: main.c acm.h 
	gcc $(CFLAGS) main.c -c

clean:
	rm -f *.o *.png prog