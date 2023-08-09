CFLAGS = -Wall -g
OBJ = serie.o saison.o episode.o main.o

prog.exe: $(OBJ)
	g++ $(OBJ) $(CFLAGS) -o prog.exe

serie.o: serie.cc serie.h
	g++ serie.cc -c

saison.o: saison.cc saison.h episode.h
	g++ saison.cc -c

episode.o: episode.cc episode.h
	g++ episode.cc -c

main.o: main.cc serie.h episode.h saison.h
	g++ main.cc -c

clean:
	rm -f *.exe *.o
