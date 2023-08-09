CFLAGS = -Wall -g
OBJ = heritage.o main.o

.SILENT:

prog: $(OBJ)
	g++ $(CFLAGS) $(OBJ) -o prog && ./prog

heritage.o: heritage.cc heritage.h
	g++ heritage.cc -c

main.o: main.cc heritage.h
	g++ main.cc -c

clean:
	rm -f *.o