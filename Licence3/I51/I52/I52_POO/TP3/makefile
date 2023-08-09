CFLAGS = -Wall -g
OBJ = complexe.o main.o polynome.o

.SILENT:

prog: $(OBJ)
	g++ $(OBJ) -o prog && ./prog

complexe.o: complexe.cc complexe.h
	g++ complexe.cc -c

main.o: main.cc complexe.h
	g++ main.cc -c

polynome.o: polynome.cc polynome.h
	g++ polynome.cc -c

clean:
	rm -f *.o