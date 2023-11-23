#include <stdio.h>
// passing array to a function and print the array in funciton itself
void printArr(int *inputArr,int n){
    for(int i=0;i<n;i++){
        printf("%d ",*(inputArr+i));
    }
}

int main(){


int arr[5]={1,2,3,4,5};
int sizeArr=5;
// printArr(&arr[0],sizeArr);
// printArr(arr,sizeArr);



    return 0;
}