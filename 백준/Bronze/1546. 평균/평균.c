#include <stdio.h>

int main() {
    int N, max = 0;
    scanf("%d", &N);
    int score[N];
    float new = 0;
    
    for(int i = 0; i < N; i++) {
        scanf("%d", &score[i]);
        if (max < score[i]) {
            max = score[i];
        }
    }
    
    for(int j = 0; j < N; j++) {
        new += (float)score[j] / max * 100;
    }
    
    printf("%.10f", new / N);
    
    return 0;
}