 
#include <stdbool.h>
 
#include "dictionary.h"
node* dict[50];
 
unsigned long hash(unsigned char *str)
{
unsigned long hash = 5381;
int c;
 
while (c = *str++)
hash = ((hash << 5) + hash) + c; 
return hash%500000; 
    
} 
return true;
}
else{
overview = overview->next;
}
}
return false;
}
typedef struct node{
char* wordd;
struct node* next;
}node;
 
bool load(const char* dictionary)
{
FILE* fp = fopen(dictionary, "r");
if (fp == NULL)
{
printf("Could not open %s.\n", dictionary);
return false;
}
char* wordload;
 
while(fscanf(fp,"%s/n",wordload)!=EOF){
int index;
node* point = (node*) malloc(sizeof(node));
strncpy(point->wordd, wordload);
 
index = hash(wordload);
if(dict[index] == NULL){
dict[index] = point;
}
else{
point->next = dict[index];
dict[index] = point;
}
 
} number++;
}
 
int number;
unsigned int size(void)
{
return number;
}
 
bool unload(void)
{
int i
for(i=0; i < 500000; i++){
node* ptr = dict[i];
free(ptr);
}
return false;
}
