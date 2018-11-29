/*
 * abc.c
 * Copyright (C) 2018 vam <jpwan21@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

//#include "abc.h"
#include <stdio.h>
#include <malloc.h>

int main(){
   for(int i=0; i<100; i++)
   {
       long * p = malloc(i);
       printf("%x:%x\n",i,* (int *)(p-1));
   }
   return 0;
}
