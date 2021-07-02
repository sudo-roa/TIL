#include <stdio.h>
int main(void){
    int a,b = 0;
    char str[1000];
    fgets(str, sizeof(str), stdin);
    sscanf(str, "%d", &a);
    fgets(str, sizeof(str), stdin);
    sscanf(str, "%d", &b);
    printf("%d", a*b);
    return 0;
}