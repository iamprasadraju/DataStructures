#!/usr/bin/env python
import random
random.seed(10)

# Size of array
N = 10000

# Generates random integers of size N
arr = random.sample(range(1, N + N), N)



sorted_arr = sorted(arr)
target = sorted_arr[-1] # random integer


# Binary Search

def BinarySearch(arr, target):
    right_idx = len(arr)
    left_idx = 0
    while left_idx <= right_idx:
        mid = (left_idx + right_idx) // 2 # // floor division operator
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            left_idx = mid + 1
        else:
            right_idx = mid - 1
    return None

idx = BinarySearch(sorted_arr, target)

if idx == None:
    print("Target Not Found")
else:
    print("Target Found at", idx)

