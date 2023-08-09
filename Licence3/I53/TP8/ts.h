#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TS_MAX_ID_SIZE 31
#define TS_DEFAULT_ADR 32

struct ts_node;

struct ts_node{
  char id[TS_MAX_ID_SIZE + 1];
  int adr;
  struct ts_node *next;
};

typedef struct ts_node *ts;

ts  ts_init_table(const char *id);
int ts_retrouver_id(ts tsymb, const char *id);
int ts_ajouter_id(ts tsymb, const char *id);
void ts_print_table(ts tsymb);
void ts_free_table(ts tsymb);
