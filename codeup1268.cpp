#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, b, i, sum=0;
    scanf("%d", &a);
    for(int i=1; i<=a; i++)
    {
        scanf("%d", &b);
        if(b%2==0)
        {
            sum=sum+1;
        }
    }
    printf("%d", sum);
}
