import time
import random

# Insertion Sort function
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generate a random list of size n
def generate_random_list(n):
    return [random.randint(0, 1000) for _ in range(n)]

# Testing the execution time for insertion sort
def test_insertion_sort(n):
    arr = generate_random_list(n)
    start_time = time.time()
    insertion_sort(arr)
    end_time = time.time()
    return end_time - start_time

# Test the performance with different input sizes
input_sizes = [100, 1000, 5000, 10000, 20000]
for size in input_sizes:
    elapsed_time = test_insertion_sort(size)
    print(f"Input size: {size}, Time taken: {elapsed_time:.6f} seconds")
