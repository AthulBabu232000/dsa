#include <stdio.h>
# define ROW 3 
# define COL 3

void printArr(int inputArr[][COL]){

    for(int i=0;i<3;i++){
        puts("loops is working\n");
        for(int j=0;j<COL;j++){
            printf("%d ",*(*inputArr+i)+j);
        }
        printf("\n");
    }
}


int main(){

int arr[ROW][COL]={1,2,3,4,5,6,7,8,9};

printArr(arr);
   

    return 0;
}