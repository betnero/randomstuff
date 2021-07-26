#include <stdio.h>

void main (void)
{
    int a;
    int *ptr_to_a; /*Decalre a pointer*/

    ptr_to_a = &a; /*Point the pointer to the memory address of teh variable a*/

    a = 5;
    printf ("The value of %d\n", a);

    *ptr_to_a = 6;
    printf ("The value of %d is %d\n", a);
    printf ("The value of ptr_to_a is %d\n", ptr_to_a);
    printf ("It address of a is %d\n", &a);
}
