#include <stdio.h>
/*This program is an example from M.Ritchie's book "The C programming language" showing how to use symbolic constants*/

/*declaring symbolic constants*/
#define LOWER 0   /*lower limit*/
#define UPPER 300 /*upper limit*/
#define STEP 20   /*step */

void main (){
    printf("*F\t*C\n"); /*print "*F" and "*C" to mark each column and seperate them with a tab"*/

    int fahr; /*declare variable*/

    for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP) /*for each value of fahr between "LOWER" and "UPPER" increase the value of fahr by "STEP*/
    printf("%3d\t%6.2f\n", fahr, (5.0/9.0)*(fahr-32)); /*print out the value of fahr in the first column and the value calculated according to the formula in the second column. First column to be printed out as a 3 digit int and the second column to be printed as a 6 digit float with 2 digits after the "."*/  
}
