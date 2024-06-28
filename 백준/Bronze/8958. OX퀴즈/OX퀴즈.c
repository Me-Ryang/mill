#include <stdio.h>
#include <string.h>

int main() {
    int T, score, sum;
    scanf("%d", &T);
    char test[80];
    
    for(int i = 0; i < T; i++) {
        sum = 0;
        score = 1;
        scanf("%s", test);
        for(int j = 0; j < strlen(test); j++) {
            if (test[j] == 'O') {
                sum += score;
                score++;
            }
            else {
                score = 1;
            }
        }
        printf("%d\n", sum);
    }
    return 0;
}