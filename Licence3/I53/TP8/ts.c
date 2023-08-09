#include "ts.h"

ts  ts_init_table(const char * id){
  ts tsymb = malloc(sizeof(struct ts_node));

  if (strlen(id) > TS_MAX_ID_SIZE) {
    printf("identificateur <%s> trop grand\n",id);
    exit(1);
  }
  strcpy(tsymb->id,id);
  tsymb->adr = TS_DEFAULT_ADR;
  tsymb->next = NULL;

  return tsymb;
}

int ts_retrouver_id(ts tsymb, const char * id){
  ts current = tsymb;
  while (current != NULL){
    if (strcmp(current->id, id) == 0) return current->adr;
    current = current->next;      
  }
  return -1;
}

int ts_ajouter_id(ts tsymb, const char *id){
  ts current = tsymb;
  if (current == NULL) {
    fprintf(stderr,"[warning] Erreur ts_ajouter_id: table vide\n");
    return -1;
  }

  while (current->next != NULL){
    if (strcmp(current->id, id) == 0)
      return current->adr;
    else
      current = current->next;
  }

  if (strcmp(current->id, id) == 0)
    return current->adr;
  else {
    current->next = ts_init_table(id);
    current->next->adr = current->adr + 1;
    current->next->next = NULL;
  }
  return current->adr + 1;
}

void ts_print_table(ts tsymb){
  ts current = tsymb;
  if (current == NULL){
    printf("(null)");
    return;
  }

  while (current->next != NULL){
    printf("(id:%s, adr:%d)-->",current->id,current->adr);
    current = current->next;
  }
  printf("(id:%s, adr:%d)\n",current->id,current->adr);
}

void ts_free_table(ts tsymb){
  ts current = tsymb, next;
  while (current!= NULL){
    next = current->next;
    free(current);
    current = next;
  }
}
