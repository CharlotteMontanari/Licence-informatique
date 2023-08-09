set term png
set output 'geante.png'
plot 'geante.dat' w l, 0.5*log(x), 0.7*log(x)