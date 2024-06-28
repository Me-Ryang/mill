#include <stdio.h>
#include <string.h>

int main() {
    int T, R;
    scanf("%d", &T);
    char test[20];
    
    for(int i = 0; i < T; i++) {
        scanf("%d %s", &R, test);
        for(int j = 0; j < strlen(test); j++) {
            for(int k = 0; k < R; k++) {
                printf("%c", test[j]);  
            }
        }
        printf("\n");
    }
    return 0;
}