#include <stdio.h>

void main (void)
{   
    int intval = 255958283;
    void *vptr = &intval;

    printf ("The value of vptr as an int is %d\n", *((int *) vptr));
    printf ("The value of vptr as a char is %d\n", *((char *) vptr));
}
