int main()
{
    int n, a[500][500], i, j, k=0;
    scanf("%d", &n);
    for(i=1;i<=n;i++){
        for(j=n;j>=1;j--){
            k++;
            a[i][j]=k;
        }
    }
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            printf("%d ", a[i][j]);
        }
        printf("\n");
    }
    return 0;
}

