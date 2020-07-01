#include <stdio.h>

int main() {
    int n, T;
    scanf("%d %d", &n, &T);

    int track = 0;
    int count = 0;

    while ((track < T) && (count < n))
    {
        int num;
        if (scanf("%d", &num) == 1)
        {
            track = track + num;
            if (T < track) break;
            count++;
        }
    }
    printf("%d", count);
    return 0;
}