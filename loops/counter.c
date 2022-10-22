#include <stdio.h>

/**
 * main - prints integers from 0 - 99
 */
 int main(void)
 {
    int counter = 0;
    
    while (counter < 100)
    {
        printf("%d\n", counter);
        counter++;
    }
    return (0);
 }