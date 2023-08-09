CFLAGS = -Wall -g
OBJ = main.o complexe.o 

.SILENT:

prog: $(OBJ)
	g++ $(OBJ) -o prog
	./prog

complexe.o: complexe.cc complexe.h
	g++ $(CFLAGS) complexe.cc -c

main.o: main.cc complexe.h
	g++ $(CFLAGS) main.cc -c

clean:
	rm -f prog *.o