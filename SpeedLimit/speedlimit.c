/*
Problem: https://open.kattis.com/problems/speedlimit
Author: Cian Kehoe
Submitted: July 1st, 2020
 */

#include <stdio.h>

int main() {
    while(1)
    {
        int n;
        scanf("%d", &n);
        
        if (n == -1) break;

        int total = 0;
        int time_passed = 0;

        for (int i = 0; i < n; i++)
        {
            int speed, time;
            scanf("%d %d", &speed, &time);
            total = total + speed * (time - time_passed);
            time_passed = time;
        }

        printf("%d miles\n", total);
    }
    return 0;
}