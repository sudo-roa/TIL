#include <stdio.h>
#include <string.h>

int main(void){
    char a[100];
    char b[100];
    char str[1000];
    scanf("%s", a);
    scanf("%s", b);
    if(strcmp(a,b)==0){
        printf("OK");
    }else{
        printf("NG");
    }
    return 0;
}