#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Insertion Sort function
void insertion_sort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
        // Move elements of arr[0..i-1] that are greater than key
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// Function to generate a random array of size n
void generate_random_array(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;  // Random numbers between 0 and 1000
    }
}

// Function to test insertion sort and measure execution time
double test_insertion_sort(int n) {
    int arr[n];
    generate_random_array(arr, n);
    
    clock_t start_time = clock();
    insertion_sort(arr, n);
    clock_t end_time = clock();
    
    return ((double)(end_time - start_time)) / CLOCKS_PER_SEC;
}

int main() {
    srand(time(NULL)); // Seed for random number generator
    int input_sizes[] = {100, 1000, 5000, 10000, 20000};
    
    for (int i = 0; i < 5; i++) {
        int size = input_sizes[i];
        double elapsed_time = test_insertion_sort(size);
        printf("Input size: %d, Time taken: %f seconds\n", size, elapsed_time);
    }
    
    return 0;
}
