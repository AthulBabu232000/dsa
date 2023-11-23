#include <stdio.h>
// function return a 1d array
int *returnArr(){

 int arr[5]={1,2,3,4,5};
// return &arr[0];
return arr;

// this program is not going to work
1. static or malloc 
}
int main(){


int* result=returnArr();
for(int i=0;i<5;i++){
    printf("%d ",result[i]);
}
    return 0;
}