#include<stdio.h>
#include<stdlib.h>
#include<time.h>


// size of array
int N  = 100;

// Generates array (int) of size N 
int* randint(int a, int b, int size){
    int *arr = malloc(N * sizeof(int)); // Memory Allocation for array
    for(int i = 0; i < N; i++){
        arr[i] = rand() % (b - a + 1) + a;
    }
    return arr;
}

int LinearSearch(int *arr, int size, int target){
    for(int i = 0; i < size; i++){
        if(arr[i] == target){
            printf("Target Found at %d\n", i);
            return 0;
        }
    }
    printf("Target Not Found.\n");
    return 1;
}

int main(){
    srand(time(NULL));  // Seed the random number generator using time func
    int *arr = randint(1, N, N);
    
    // Choose a valid target from the array
    int random_index = rand() % N;
    int target = arr[random_index];

    LinearSearch(arr, N, target);
    free(arr);
    return 0;
}
