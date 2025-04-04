# Implementation of Insertion Sort



# Algorithm Steps:

"""


Time Complexity - O(n**2)

"""


import random

def Insertion_Sort(arr):
	for i in range(1, len(arr)):
		j = i
		
		while j > 0 and arr[j] < arr[j - 1]:
			arr[j - 1], arr[j] = arr[j], arr[j - 1]
			j = j - 1

	return arr



