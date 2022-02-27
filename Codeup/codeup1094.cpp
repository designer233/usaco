// Online C compiler to run C program online
#include <stdio.h>

int main()
{
    int b;
    scanf("%d", &b);
    int a[b + 1];
    for(int i=0; i<b; i++)
    {
        scanf("%d", &a[i]);
    }
    for(int i=b-1; i >=0; i--)
    {
        printf("%d ", a[i]);
    }
}
