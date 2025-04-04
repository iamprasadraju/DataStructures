# Implementation of Selection Sort


# Algorithm Steps :


"""

1. Find a Largest number in prefix A[:i + 1] using Helper Function -> Max(arr)

2. swap it to A[i]

3. Sort 1,........, i - 1 

"""

# Method - 1: Recursive Approach -> Time complexity O(n**2)

def selection_sort(arr, i = None):
	if i is None:
		i = len(arr) - 1
	if i > 0:
		j = perfix_max(arr, i)
		arr[i], arr[j] = arr[j], arr[i]
		selection_sort(arr, i - 1)
	return arr

	
# Helper Function

def perfix_max(arr, i):
	if i > 0:
		j = perfix_max(arr, i - 1)
		if arr[i] < arr[j]:
			return j
	return i




"""

# Method - 2: Brute-Force Approach -> Time Complexity O(n**2aa)



def selection_sort(arr, ascending = True):
	for i in range(len(arr)):
		m = i
		for j in range(i + 1, len(arr)):
			if ascending:
				if arr[m] < arr[j]:
					m = j
			else:
				if arr[m] > arr[j]:
					m = j
		arr[m], arr[i] = arr[i], arr[m]
	return arr


"""