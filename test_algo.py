#!/usr/bin/env python

import random
import time
import tracemalloc


N = 1000000

tracemalloc.start()

# unique integer of size of N
values = random.sample(range(1, N + N), N)
target = random.sample(values, 1)[0]


current, peak = tracemalloc.get_traced_memory()
print(f"Memory used: {current / 1024**2:.2f} MB\n")
tracemalloc.stop()

def time_function(func, *args):
	start = time.monotonic_ns()
	func(*args)
	end = time.monotonic_ns()
	return end - start

# Iterate Over list (Brute Force) -> Worse case: O(n)
def FindAnElement(values, target):
	for idx, element in enumerate(values):
		if element == target:
			print("Target Found at", idx)
			return
	print("Target Not Found.")

time_taken = time_function(FindAnElement, values, target)


print("Time taken for linear search -",  time_taken, "ns")


print("----------------------------------------------------------")


def BidirectionalSearch(values, target):
	size = len(values)
	middle = size // 2
	left_id = middle
	right_id = middle + 1 
	if values[middle] == target:
		print("Target Found at", middle)
		return

	while left_id >= 0 or right_id < size:
		if left_id >= 0:
			if values[left_id] == target:
				print("Target Found at", left_id)
				return
			left_id -= 1

		if right_id < size:
			if values[right_id] == target:
				print("Target Found at", right_id)
				return
			right_id += 1

	print("Target Not Found.")	
	
		

time_taken = time_function(BidirectionalSearch, values, target)
print("Time taken BidirectionalSearch -",  time_taken, "ns")

print("----------------------------------------------------------")


def BinarySearch(values, target):

	low = 0
	high = len(values) - 1

	while low <= high:
		mid = (low + high) // 2
		if values[mid] == target:
			print("Target Found at", mid)
			return
		elif values[mid] < target:
			low = mid + 1
		else:
			high = mid - 1

	print("Target Not Found.") 


time_taken = time_function(BinarySearch, sorted(values), target)
print("Time taken BinarySearch -",  time_taken, "ns")