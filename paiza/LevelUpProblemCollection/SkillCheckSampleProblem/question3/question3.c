#include <stdio.h>
int main(void){
    int a,tmp = 0;
    char str[1000];
    fgets(str, sizeof(str), stdin);
    sscanf(str, "%d", &a);

    for(int i = 0;i<4;i++){
        fgets(str, sizeof(str), stdin);
        sscanf(str, "%d", &tmp);
        if(a>tmp){
            a = tmp; 
        }
    }
    
    printf("%d", a);
    return 0;
}