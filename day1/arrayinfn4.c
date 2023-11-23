#include<stdio.h>
# define ROW 3
# define COL 3

int** returnArr(){
static int arr[ROW][COL]={1,2,3,4,5,6,7,8,9};

return arr;

}
int main(){

int **result=returnArr();
for(int i=0;i<ROW;i++){
    for(int j=0;j<COL;j++){
        printf("%d ",result[i][j]);
    }
    printf("\n");
}
}