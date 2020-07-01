/*
Problem: https://open.kattis.com/problems/server
Author: Cian Kehoe
Submitted: July 1st, 2020
 */

#include <stdio.h>

int main() {
    int n, T;
    scanf("%d %d", &n, &T);

    // int track = 0;
    int count = 0;

    while ((T > 0) && (count < n))
    {
        int num;
        if (scanf("%d", &num) == 1)
        {
            T = T - num;
            if (T < 0) break;
            count++;
        }
    }
    printf("%d", count);
    return 0;
}