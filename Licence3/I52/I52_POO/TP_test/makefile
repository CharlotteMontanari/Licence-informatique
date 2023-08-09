CFLAGS = -Wall -g
OBJ = oeuvre.o tableau.o exposition.o main.o

.SILENT:

prog.exe: $(OBJ)
	g++ $(OBJ) -o prog.exe

oeuvre.o: oeuvre.cc oeuvre.h
	g++ oeuvre.cc -c

tableau.o: tableau.cc tableau.h
	g++ tableau.cc -c

exposition.o: exposition.cc exposition.h tableau.h
	g++ exposition.cc -c

main.o: main.cc oeuvre.h tableau.h exposition.h
	g++ main.cc -c

clean:
	rm -f *.exe *.o