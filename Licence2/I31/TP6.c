#include <stdio.h>
#include <stdlib.h>

typedef struct disque disque;
struct disque {
    unsigned int size;
    disque *next;
};

typedef struct {
    unsigned char id;
    unsigned int count;
    disque *first;
}tour;

tour *newTour(unsigned char id) {
    tour *t = (tour*)malloc(sizeof(tour));
    t -> id = id;
    t -> count = 0;
    t -> first = NULL;
    return t;
}

disque *newDisque(unsigned int s) {
    disque *d = (disque*)malloc(sizeof(disque));
    d -> size = s;
    d -> next = NULL;
    return d;
}

void print(tour* t) {
    if (t == NULL)
        return;
    if (t -> first != NULL) {
        disque *d = t -> first;
        printf("[%u", d -> size);
        while (d -> next != NULL) {
            printf(",%u", d -> next -> size);
            d = d -> next;
        } printf("]\n");
    return;
    }
}

int put(tour* t, disque *d) {
    if ((t == NULL) || (d == NULL))
        return 0;
    if (t -> first == NULL) {
        t -> first = d;
        t -> count += 1;
        return 1;
    } if (t -> first -> size < d -> size)
        return 0;
    d -> next = t -> first;
    t -> first = d;
    return 1;
}

disque *take(tour *t) {
    if ((t == NULL) || (t -> first == NULL)) 
        return NULL;
    disque *d = t -> first;
    t -> first = t -> first -> next;
    d -> next = NULL;
    return d;
}

int move(tour* origin, tour *destination) {
    if ((origin == NULL) || (origin -> first == NULL) || (destination == NULL))
        return 0;
    if (destination -> first == NULL) 
        return 0;
    disque *d = take(origin);
    return put(destination, d);
}

void destroy(tour *t) {
    if (t == NULL)
        return;
    disque *current = t -> first;
    disque *next = NULL;
    while (current != NULL) {
        next = current -> next;
        free(current);
        current = next;
    }
    free(t);
}

int main() {
    tour *tour1 = newTour(1);
    int nbre_disques = 0;
    int i;
    printf("Saisir le nombre de disque: ");
    scanf("%d", &nbre_disques);
    for (i=nbre_disques; i>0; i--) {
        disque *dis = newDisque(i);
        put(tour1, dis);
    }
    print(tour1);

    int tour_s, tours_d;
    printf("Entrer un déplacement en donnant la tour source et la tour destination: ");
    scanf("%d %d", &tour_s, &tours_d);
    
}
