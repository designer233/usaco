#include <stdio.h>

int main() 
{
    int a;
    scanf("%d", &a);
    for(int i=1; i<=a; i++)
    {
        for(int e=1; e<=i; e++)
        {
            printf("*");
        }
        printf("\n");
    }
}
