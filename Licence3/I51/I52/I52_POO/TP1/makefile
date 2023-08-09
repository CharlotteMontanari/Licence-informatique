CFLAGS = -Wall -g
OBJ = echangiste.o main.o complexe.o

.SILENT:

prog: $(OBJ)
	g++ $(CFLAGS) $(OBJ) -o prog && ./prog

echangiste.o: echangiste.cc echangiste.h complexe.h
	g++ $(CFLAGS) echangiste.cc -c

main.o: main.cc echangiste.h
	g++ $(CFLAGS) main.cc -c

complexe.o: complexe.cc complexe.h
	g++ $(CFLAGS) complexe.cc -c

clean:
	rm -f prog *.o