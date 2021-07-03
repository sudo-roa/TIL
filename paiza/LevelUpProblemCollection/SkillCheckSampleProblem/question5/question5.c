#include <stdio.h>
int main(void){
    int a=0;
    scanf("%d", &a);
    for(int i=1;i<a+1;i++){
        if(i%5==0 && i%3 ==0){
            printf("Fizz Buzz\n");
        }else if(i%3==0){
            printf("Fizz\n");
        }else if(i%5==0){
            printf("Buzz\n");
        }else{
            printf("%d\n", i);
        }
    }
    return 0;
}