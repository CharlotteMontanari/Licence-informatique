#include "disjoint.h"

int main(int argc, char **argv) {
    if (argc < 2)
        return 0;
    int max = atoi(argv[1]);
    for (int n=0; n<max; n++) {
        init_disjoint(n);
        int p = n;
        int m = 0;
        while (p > 1) {
            int i = random() % n;
            int j = random() % n;
            disjoint ri = representant(i);
            disjoint rj = representant(j);
            if (ri != rj) {
                reunion(ri, rj);
                p--;
            }
            m++;
        }
        printf("n: %d \tm: %d\n", n, m);
        freeDisjoint(n);
    }
    return 0;
}