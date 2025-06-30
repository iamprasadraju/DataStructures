#!/usr/bin/env python

import random
import time
import tracemalloc
from colorama import Fore, Back, Style


N = 700000
time_taken = []

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
	return (end - start) / 1e6 # to milliseconds

# Iterate Over list (Brute Force) -> Worse case: O(n)
def FindAnElement(values, target):
	for idx, element in enumerate(values):
		if element == target:
			print("Target Found at", idx, "- Linear Search")
			return
	print("Target Not Found.")

linear_time = time_function(FindAnElement, values, target)
time_taken.append(linear_time)



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
				print("Target Found at", left_id, "- Bidirectional Search")
				return
			left_id -= 1

		if right_id < size:
			if values[right_id] == target:
				print("Target Found at", right_id,  "- Bidirectional Search")
				return
			right_id += 1

	print("Target Not Found.")	
	
		

directional_time = time_function(BidirectionalSearch, values, target)
time_taken.append(directional_time)


print("----------------------------------------------------------")


def BinarySearch(values, target):

	low = 0
	high = len(values) - 1

	while low <= high:
		mid = (low + high) // 2
		if values[mid] == target:
			print("Target Found at", mid, "- Binary Search")
			return
		elif values[mid] < target:
			low = mid + 1
		else:
			high = mid - 1

	print("Target Not Found.") 


binary_time = time_function(BinarySearch, sorted(values), target)
time_taken.append(binary_time)


max_time = max(time_taken)

def print_bar(name, time_ms):
	max_time = max(time_taken)
	bar_length = int((time_ms / max_time) * 30)
	bar = "#" * bar_length
	print(f"{Fore.GREEN} {name}: {Fore.YELLOW} {bar} ({time_ms:.2f} ms) \n")



if __name__ == "__main__":
	print("\nPerformance: \n")
	print_bar("Linear Search", linear_time)
	print_bar("Bidirectional Search", directional_time)
	print_bar("Binary Search", binary_time)