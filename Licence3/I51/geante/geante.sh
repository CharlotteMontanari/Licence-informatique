t=$1
max=$2
for((n=1;n<$max;n++))
do
    ./prog $t $n
done > geante.dat
gnuplot geante.plot