#include <stdio.h>

int main(){
    int A, B;
    double div;
    
    scanf("%d %d", &A, &B);
    div = (double)A/(double)B;
    printf("%.12f", div);
    return 0;
}