#include <stdio.h>

int main(){
    int number;
    printf("Please type a number to start:\n");
    scanf("%d", &number);

    int runner = 1;

    while(runner){
        
        if (number == 1){
            runner = 0;
        }
        else if (number % 2 == 0){
            number = number / 2 ;
            printf("%d\n", number);
        }
        else {
            number = 3 * number  + 1;
            printf("%d\n", number);
        }
    }
    
    return 0;
}